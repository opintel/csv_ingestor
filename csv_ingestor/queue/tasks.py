"""
Tareas Celery para ingesta
de archivos CSV
"""
from csv_ingestor.filemanager.csvmanager import CSVManager


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
