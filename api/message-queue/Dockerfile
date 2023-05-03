FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /message-queue

COPY /constants /constants
COPY /api/message-queue /api/message-queue

RUN pip install -r /api/message-queue/requirements.txt

CMD ["python", "/api/message-queue/consumer-process-queue.py"]