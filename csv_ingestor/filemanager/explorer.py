"""
Clases del Explorador de archivos
"""
from pathlib import Path, PurePath
from csv_ingestor.queue.scheduler import ingest
from csv_ingestor.conf import settings


class FileExplorer:
    """
    Explorador de archivos csv
    busca a partir de un path base en
    el arbol completo
    """
    def __init__(self):
        self.base_path = settings.FILE_BASE_PATH

    def _read_tree(self):
        base_object_path = Path(self.base_path)
        for subdirectory in base_object_path.iterdir():
            # Busca subdirectorios
            if subdirectory.is_dir():
                print("* Explorando directorio: {}".format(str(PurePath(subdirectory))))
                for file in subdirectory.iterdir():
                    # Busca archivos
                    if not file.is_dir():
                        path = str(PurePath(file))
                        # Solo archivos CSV
                        if '.csv' in path:
                            yield path

    def ingest(self):
        """
        Ingesta los archivos csv
        para mandarlos al datastore
        """
        for file in self._read_tree():
            print("   **** Procesando archivo: {}".format(file))
            result = ingest.delay(file=file)
            print(result.status)
