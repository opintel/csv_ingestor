FROM ubuntu:16:10

RUN apt-get update && \
    apt-get install -y supervisor cron python3.6

RUN mkdir -p /var/log/ingestor \
    && mkdir -p /data/ingestor

COPY . .

RUN python setup.py develop
RUN pip install -r requirements.txt

ADD ingest-celery.conf /etc/supervisor/conf.d/ingest-celery.conf
ADD start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]