FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /message-queue

COPY /constants /constants
COPY /api/message-queue /api/message-queue

RUN pip install -r /api/message-queue/requirements.txt

CMD gunicorn --bind 0.0.0.0:5003 app:app
