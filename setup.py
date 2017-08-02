from setuptools import setup, find_packages


description = """
    Recolector de archivos CSV asociados a un recurso CKAN descargados por medio de Refineria,
    extrae e inserta los primeros 150 registros y los envia al datastore.
"""


setup(
    name='csv_ingestor',
    description='Recolector de archivos CKAN-CSV',
    long_description=description,
    version='0.1.0',
    license='MIT',
    author='Francisco Vaquero',
    author_email='f.vaquero@opianalytics.com',
    install_requirements=[
        'celery[redis]==4.1.0',
        'requests==2.18.2'
    ],
    packages=find_packages(),
    include_package_data=True
)
