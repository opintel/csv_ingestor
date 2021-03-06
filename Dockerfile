FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y supervisor cron python3 python3-pip

RUN mkdir -p /var/log/ingestor \
    && mkdir -p /data/ingestor

COPY . /csv_ingestor

RUN pip3 install setuptools
RUN cd /csv_ingestor && python3 /csv_ingestor/setup.py develop
RUN pip3 install -r /csv_ingestor/requirements.txt

ADD ingest-celery.conf /etc/supervisor/conf.d/ingest-celery.conf
ADD start.sh /start.sh
RUN chmod +x /start.sh
RUN which celery

ENTRYPOINT ["/start.sh"]