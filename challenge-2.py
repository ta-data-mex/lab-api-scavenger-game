#Importar las librerías necesarias
import sys
!{sys.executable} -m pip install requests pandas
import requests
import pandas as pd
from pandas.io.json import json_normalize

#obtener la última información de los commits en stats/commit_activity y transformarla a json
iron_commits = requests.get('https://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/stats/commit_activity')
iron_commits = iron_commits.json()

#Regresa una lista de los commits de las últimas semanas, el último realizado en marzo de este año
iron_commits

#A través de un f string imprimir el último valor, el cual representa la última semana: 0
total = f"Number of commits last week: {iron_commits[-1]['total']}"
print(total)
