FROM python:3.9-slim

COPY /api/microservice-api /api/microservice-api
COPY /constants /constants

RUN pip install -r /api/microservice-api/requirements.txt
RUN mkdir -p /api/microservice-api/processed-files
RUN mkdir -p /api/microservice-api/uploaded-files

WORKDIR /api/microservice-api

CMD gunicorn --bind 0.0.0.0:5002 app:app