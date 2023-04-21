FROM python:3.9.0b4-alpine3.12

COPY /services/conversion_cron/conversion_cron /bin/conversion_cron
COPY /services/conversion_cron/requirements.txt /bin/requirements.txt
COPY /constants /constants 

COPY /services/conversion_cron/root /var/spool/cron/crontabs/root

RUN chmod +x /bin/conversion_cron
RUN pip install -r /bin/requirements.txt

CMD crond -l 2 -f