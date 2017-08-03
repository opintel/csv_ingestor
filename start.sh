#!/bin/bash
# touch /var/run/supervisor.sock
# chmod 777 /var/run/supervisor.sock
# service supervisor restart

# supervisorctl reread
echo "INICIANDO CELERY"
C_FORCE_ROOT=1 celery -A csv_ingestor worker --app=csv_ingestor.queue.scheduler --logfile="/var/log/ingestor/celery_error.log"
echo "CELERY INICIADO"
