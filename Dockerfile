FROM python:3.5.3

RUN apt-get update && \
    apt-get install -y supervisor cron

RUN mkdir -p /var/log/ingestor \
    && mkdir -p /data/ingestor

COPY . .

RUN python setup.py develop
RUN pip install -r requirements.txt

ADD ingest-celery.conf /etc/supervisor/conf.d/ingest-celery.conf
RUN chmod 0600 /start.sh

ENTRYPOINT ["/start.sh"]