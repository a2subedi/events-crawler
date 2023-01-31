def text_stripper(elem_list):
    '''Strips all white spaces form parsed html text'''
    temp = []
    for elem in elem_list:
        temp.append(''.join(elem.text.split()))
    return temp

create_stmt = '''
DROP TABLE IF EXISTS events;
CREATE TABLE IF NOT EXISTS events
(
    id serial primary key NOT NULL,
    event_time character varying(100) COLLATE pg_catalog."default",
    event_location character varying(200) COLLATE pg_catalog."default",
    event_title character varying(500) COLLATE pg_catalog."default",
    artists text[],
    works text[],
    image_link character varying(500) COLLATE pg_catalog."default",
    event_date character varying(10) COLLATE pg_catalog."default"
)'''

insert_stmt = '''INSERT INTO events(event_time, event_location, event_title, artists, works, image_link, event_date)
	VALUES ('{}', '{}', '{}', ARRAY {}, ARRAY {}, '{}', '{}');'''