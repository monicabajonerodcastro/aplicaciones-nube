FROM python:3.9-slim

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5002 app:app