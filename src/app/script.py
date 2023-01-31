import requests
from bs4 import BeautifulSoup as bs
import psycopg2
from helpers.helpers import text_stripper, create_stmt, insert_stmt

from config.config import db_host,db_name,db_pass,db_port,db_user

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(db_host,db_name,db_user,db_pass)
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

src = 'https://www.lucernefestival.ch/en/program/summer-festival-23'
base_url = 'https://www.lucernefestival.ch/'


def get_event_details(event_url):
    '''Returns event detail as a dict'''
    _res = requests.get(base_url+event_url)
    _res.close()

    details = {}

    soup = bs(_res.text,'html.parser')
    header = soup.find('header',{'class':'page-header clip-path clr-pri'})
    info = header.findAll('div',{'class':'cell large-6 subtitle'})
    date_venue_list = info[0].find('br').next.text.split('|')
    details['date'] = date_venue_list[0].strip()
    details['time'] = date_venue_list[1].strip()
    details['location'] = date_venue_list[2].strip()
    details['title'] = header.find('h1').text.strip()

    cast = soup.find('section',{'id':'cast'})
    details['artists'] = text_stripper(cast.findAll('li',{'class':'cell medium-6 p'}))
    
    program = soup.find('section',{'id':'program'}).find('div',{'class':'cell medium-9'})
    details['works'] = text_stripper(program.findAll('div',{'class':'program-item p'}))

    details['img_src'] = base_url + soup.find('main',{'class':'fl-clr yellow content-container'}).find('img')['src']

    return (details)


res = requests.get(src)
res.close()

soup = bs(res.text,'html.parser')

events_items = soup.findAll('li',{'class':'event-item fl-clr yellow'})

event_url_list = []
# cur.execute(create_stmt)
count = 0
for event in events_items:
    # list all event urls
    event_url_list.append(event.find('p',{'class':'event-title h3'}).find('a')['href'])

for event in event_url_list:
    info = get_event_details(event)
    astr = insert_stmt.format(info['time'],info['location'],info['title'],info['artists'],info['works'],info['img_src'],info['date'])
    cur.execute(insert_stmt.format(info['time'],info['location'],info['title'],info['artists'],info['works'],info['img_src'],info['date']))
    count += 1

conn.commit()
cur.close()
conn.close()
print('Crawled events: ',count)
