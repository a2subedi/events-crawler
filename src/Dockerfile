FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app/ .
CMD ["python", "script.py"]