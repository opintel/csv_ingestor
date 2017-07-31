"""
Sistema de ingesta para
enviar datos al datapusher
"""
import os
import csv
from pathlib import Path, PurePath
import requests


class CkanClient:
    """
    Cliente python para el Datastore API
    Manejo basico de excepciones
    """
    def __init__(self, **kwargs):
        self.host_ckan_api = kwargs.get('host_ckan_api', None)
        self.data_pusher_api_url = '{}/api/3/action/datastore_create'
        self.access_token = kwargs.get('access_token', 'bef88ff3-f463-4a03-9595-f79fccba9c7d')

    def send_file_to_datapusher(self, id_resource=None, data=None, fields=None):
        """
        Recibe datos empaquetados del archivo
        asociado al recurso a actualizar,
        envia un POST al DataStore API para
        guardar el contenido del recurso.
        """
        return self._make_api_petition(id_resource=id_resource, data=data, fields=fields)

    def _make_api_petition(self, id_resource=None, data=None, fields=None):
        data_post = {
            'resource_id': id_resource,
            'force': True,
            'records': data,
            'fields': fields
        }

        response = requests.post(
            self.data_pusher_api_url,
            data=data_post,
            headers={
                'Authorization': self.access_token
            }
        )

        try:
            response.raise_for_status()
        except Exception as error:
            print(error)
            return False

        if response.status_code != 200:
            return False

        return True


class CSVManager:
    """
    Maneja la lectura y empaquetado
    de los datos que contiene un CSV
    """
    def __init__(self, **kwargs):
        self.delimiter = kwargs.get('separator', ',')
        self.quotechar = kwargs.get('endofline', '|')
        self.api_client = kwargs.get('api_client', None)
        self.max_lines_preview = kwargs.get('max_lines_preview', 150)
        self.fields = []
        self.raw_fields = []
        self.lines = []

    def _read_file(self, path_file=None):
        with open(path_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0

            for line in csv_reader:
                if count > self.max_lines_preview:
                    break

                if count == 0:
                    self._set_headers(self, line=line)

                if count > 0:
                    data_store_line = self._line_to_datastore_field(line=line)
                    self.lines.append(data_store_line)

                count += 1

    def _line_to_datastore_field(self, line=None):
        aux_dict = {}
        for index in xrange(0, len(self.raw_fields)):
            aux_dict[self.raw_fields[index]] = line[index]

        self.lines.append(aux_dict)

    def _set_headers(self, line=None):
        self.raw_fields = line
        for column in line:
            self.fields.append({'id': column})

    def _send_to_datastore(self, id_resource=None):
        self.api_client.send_file_to_datapusher(
            id_resource=id_resource,
            data=self.lines,
            fields=self.fields
        )

    def process_file(self, path_file=None, id_resource=None):
        """
        Procesa y formatea el contenido de un archivo
        para enviarlo al datapusher
        """
        self._read_file(path_file=path_file)
        self._send_to_datastore(id_resource=id_resource)


class Ingestor:
    """
    Clse que realiza tareas de lectura
    de los archivos
    """
    def __init__(self, **kwargs):
        self.base_path = kwargs.get('base_path', os.path.abspath(__file__))
        self.api_client = kwargs.get('api_client', None)
        self.csv_manager = kwargs.get('csv_manager', None)

    def _read_three(self):
        base_object_path = Path(self.base_path)
        for subdirectory in base_object_path.iterdir():
            # Busca subdirectorios
            if subdirectory.is_dir():
                for file in subdirectory.iterdir():
                    # Busca archivos
                    if not file.is_dir():
                        path = str(PurePath(file))
                        # Solo archivos CSV
                        if '.csv' in path:
                            yield path

    def _process_file(self, file=None):
        name = file.split('/')[-1]
        self.csv_manager.process_file(path_file=file, id_resource=name)

    def ingest(self):
        """
        Ingesta los archivos csv
        para mandarlos al datastore
        """
        for file in self._read_three():
            self._process_file(file=file)


if __name__ == "__main__":
    print(os.path.dirname(os.path.abspath(__file__)))
