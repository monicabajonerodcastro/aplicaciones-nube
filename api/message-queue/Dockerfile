FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY /constants /constants
COPY /api/message-queue /api/message-queue

RUN pip install -r /api/message-queue/requirements.txt

WORKDIR /api/message-queue

CMD gunicorn --bind 0.0.0.0:5003 app:app
