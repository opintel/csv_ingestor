#!/bin/bash
touch /var/run/supervisor.sock
chmod 777 /var/run/supervisor.sock
service supervisor restart

supervisorctl reread

python3 /csv_ingestor/csv_ingestor/ingestor.py