FROM python:3.9-slim

RUN mkdir files
COPY /api /api
COPY /constants /constants

RUN pip install -r /api/requirements.txt

WORKDIR /api

CMD gunicorn --bind 0.0.0.0:5002 app:app