#!/bin/bash
sudo touch /var/run/supervisor.sock
sudo chmod 777 /var/run/supervisor.sock
sudo service supervisor restart

sudo supervisorctl reread

python3 /csv_ingestor/csv_ingestor/ingestor.py