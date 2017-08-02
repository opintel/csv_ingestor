"""
Manejo de las tareas en la cola
para cargar contenido de forma
asincrona
"""
from celery import Celery
from csv_ingestor.conf import settings
from csv_ingestor.filemanager.csvmanager import CSVManager


ingestor_scheduler = Celery(
    'csv_ingestor',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BACKEND_URL
)

ingestor_scheduler.conf.update(
    **settings.CELERY_SCHEDULER_CONFIG
)


@ingestor_scheduler.task
def ingest(file=None):
    """
    Crea una nueva tarea de ingesta
    en la cola de trabajo
    """
    print("Estoy en la cola: {0}".format(file))
    csv_manager = CSVManager()
    name = file.split('/')[-1]

    csv_manager.process_file(path_file=file, id_resource=name)

    return csv_manager.response


if __name__ == '__main__':
    #print("Startea")
    ingestor_scheduler.start()
