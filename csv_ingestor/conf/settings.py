import os

# CONFIGURACIONES DEL MANAGER DE CSV
CSV_DELIMITER = os.environ.get('CSV_DELIMITER', ',')
CSV_QUOTECHAR = os.environ.get('CSV_QUOTECHAR', '|')
CSV_MAX_ROWS_TO_PREVIEW = os.environ.get('CSV_MAX_ROWS_TO_PREVIEW', 150)

# CONFIGURACIONES DEL EXPLORADOR DE ARCHIVOS
FILE_BASE_PATH = os.environ.get('FILE_BASE_PATH', '.')

# CONFIGURACIONES DEL CLIENTE CKAN API
CKAN_BASE_URL = os.environ.get('CKAN_BASE_URL', 'http://10.20.55.7/busca/')
CKAN_ACCESS_TOKEN = os.environ.get('CKAN_ACCESS_TOKEN', 'bef88ff3-f463-4a03-9595-f79fccba9c7d')

# CONFIGURACIONES DE CELERY
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'pyamqp://0.0.0.0')
CELERY_BACKEND_URL = os.environ.get('CELERY_BACKEND_URL', 'redis://0.0.0.0')

CELERY_SCHEDULER_CONFIG = {
    'result_expires': os.environ.get('CELERY_RESULT_EXIPRES', 3600),
    'task_annotations': {
        'tasks.add': {
            'rate_limit': os.environ.get('CELERY_RATE_LIMIT', '10/s')
        }
    },
    'timezone': os.environ.get('CELERY_TIMEZONE', 'UTC')
}
