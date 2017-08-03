"""
Sistema de ingesta para
enviar datos al datapusher
"""
import datetime
import time
from csv_ingestor.filemanager.explorer import FileExplorer


if __name__ == "__main__":
    print("CSV INGEST")
    print("COMENZANDO PROCESO:")

    explorer = FileExplorer()
    explorer.ingest()
    print("FIN DEL PROCESO DE INGESTA")
