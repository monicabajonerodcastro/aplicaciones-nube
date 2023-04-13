FROM python:3.9.0b4-alpine3.12

COPY /conversion_cron/conversion_cron /bin/conversion_cron
COPY /conversion_cron/requirements.txt /bin/requirements.txt
COPY /constants /constants 

COPY /conversion_cron/root /var/spool/cron/crontabs/root

RUN chmod +x /bin/conversion_cron
RUN pip install -r /bin/requirements.txt

CMD crond -l 2 -f