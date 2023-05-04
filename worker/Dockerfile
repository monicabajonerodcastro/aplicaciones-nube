FROM python:3.9-slim

COPY /worker /worker
COPY /constants /constants

RUN pip install -r /worker/requirements.txt

WORKDIR /worker

CMD gunicorn --bind 0.0.0.0:5004 app:app