FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir files
COPY /constants /constants
COPY /worker/message-queue /worker/message-queue

RUN pip install -r /worker/message-queue/requirements.txt

WORKDIR /worker/message-queue

CMD gunicorn --bind 0.0.0.0:5003 app:app
