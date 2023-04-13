FROM python:3.9-slim

WORKDIR /microservice-api

COPY /constants /constants
COPY /microservice-api /microservice-api/

RUN pip install -r requirements.txt
RUN mkdir -p /microservice-api/processed-files
RUN mkdir -p /microservice-api/uploaded-files

CMD gunicorn --bind 0.0.0.0:5002 app:app