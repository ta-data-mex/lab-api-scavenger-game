#Importar las librerías necesarias
import sys
!{sys.executable} -m pip install requests pandas
import requests
import pandas as pd
from pandas.io.json import json_normalize

#Generar token

TOKEN = 'bb0470c5f072588a4c60dd7c4f72cbf98e7f193'

#Validat token e ingreso Git APIs
#curl -u eduarde1:bb0470c5f072588a4c60dd7c4f72cbf98e7f1932 https://api.github.com/user # > output.json


#Obtener los forks y languages
iron_forks = requests.get('https://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/forks')
iron_forks = iron_forks.json()
iron_forks

iron_languages = requests.get('https://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/languages')
iron_languages = iron_languages.json()
iron_languages

languages = []
for key, values in iron_languages.items():
    languages.append(key)
languages = set(languages)
print(list(languages))