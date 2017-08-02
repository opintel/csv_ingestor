import csv
from csv_ingestor.conf import settings
from csv_ingestor.api.client import CkanClient


class CSVManager:
    """
    Maneja la lectura y empaquetado
    de los datos que contiene un CSV
    """
    def __init__(self):
        self.delimiter = settings.CSV_DELIMITER
        self.quotechar = settings.CSV_QUOTECHAR
        self.max_lines_preview = settings.CSV_MAX_ROWS_TO_PREVIEW

        self.api_client = CkanClient()
        self.fields = []
        self.raw_fields = []
        self.lines = []
        self.response = None

    def _read_file(self, path_file=None):
        with open(path_file, 'r', newline="\n", encoding='iso-8859-1') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0

            for line in csv_reader:
                if count > self.max_lines_preview:
                    break

                if count == 0:
                    self._set_headers(line=line)

                if count > 0:
                    data_store_line = self._line_to_datastore_field(line=line)
                    self.lines.append(data_store_line)

                count += 1

    def _line_to_datastore_field(self, line=None):
        aux_dict = {}
        for index in range(0, len(self.raw_fields)):
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
        self.response = self.api_client.response

    def process_file(self, path_file=None, id_resource=None):
        """
        Procesa y formatea el contenido de un archivo
        para enviarlo al datapusher
        """
        self._read_file(path_file=path_file)
        self._send_to_datastore(id_resource=id_resource)
