# CSV Ingestor

Recolector de archivos CSV asociados a un recurso CKAN descargados por medio de *Refineria* , extrae e inserta los primeros 150 registros y los envia al datastore.

# Requerimientos

- Python 3.5
- Python requests

# Instalación

1. Instalar requerimientos
```sh
pip install -r requirements.txt
```
2. Correr ingesta
```sh
python ingestor.py
```