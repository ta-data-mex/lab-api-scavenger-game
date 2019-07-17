#Importar las librerías necesarias
import sys
!{sys.executable} -m pip install requests pandas
import requests
import pandas as pd
from pandas.io.json import json_normalize

#importar base64 para decodificar los la info de los requests
import base64

#Realizar un doble requests del url, transformarlo a json y leer content_url en específico
iron_scavenger = requests.get(requests.get('https://api.github.com/repos/ironhack-datalabs/scavenger', verify=False).json()['contents_url'][:-7], verify=False).json()

#Crear dos listas vacías para agregar los nombres de los archivos y el mensaje de broma
cold_joke = []
names = []

#Iterar sobre la variable de doble request y sobre un nuevo request que en específico tenga las url de los archivos secretos
for inf in iron_scavenger:
    for sec_files in requests.get(inf['url'], verify=False).json():
        if type(sec_files) == str:
            pass
        elif 'scavengerhunt' in sec_files['name']:
            names.append(sec_files['name'])
            cold_joke.append(base64.b64decode(requests.get(sec_files['url'], verify=False).json()['content'])