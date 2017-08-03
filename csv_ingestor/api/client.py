"""
Clases con logica de cliente
para el API de CKAN
"""
import requests
import json
from csv_ingestor.conf import settings


class CkanClient:
    """
    Cliente python para el Datastore API
    Manejo basico de excepciones
    """
    def __init__(self):
        self.host_ckan_api = settings.CKAN_BASE_URL
        self.data_pusher_api_url = '{}api/3/action/datastore_create'.format(
            settings.CKAN_BASE_URL
        )
        self.access_token = settings.CKAN_ACCESS_TOKEN
        self.response = None

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
            "resource_id": id_resource,
            "force": True,
            "records": data,
            "fields": fields
        }

        print("Post data")
        try:
            print(data_post)
            response = requests.post(
                self.data_pusher_api_url,
                json=data_post,
                headers={
                    'Authorization': self.access_token
                }
            )
        except Exception as othererror:
            print(othererror)
            return False

        try:
            response.raise_for_status()
        except Exception as error:
            print(error)
            #print(response.text)
            #print(response.request.body)
            return False

        if response.status_code != 200:
            return False

        self.response = response

        return True
