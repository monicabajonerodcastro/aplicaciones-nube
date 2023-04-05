FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /message-queue

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5003 app:app