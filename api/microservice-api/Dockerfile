FROM python:3.9-slim

COPY /api/microservice-api /api/microservice-api
COPY /constants /constants

RUN pip install -r /api/microservice-api/requirements.txt
RUN mkdir -p /files
RUN cd files
RUN touch gcloud.json

WORKDIR /api/microservice-api

CMD gunicorn --bind 0.0.0.0:5002 app:app