FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /message-queue

COPY /constants /constants
COPY /services/message-queue /services/message-queue

RUN pip install -r /services/message-queue/requirements.txt

CMD gunicorn --bind 0.0.0.0:5003 app:app
