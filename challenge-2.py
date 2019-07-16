#Importar las librerías necesarias
import sys
!{sys.executable} -m pip install requests pandas
import requests
import pandas as pd
from pandas.io.json import json_normalize

#obtener la última información de los commits
iron_commits = requests.get('https://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/commits/master')
iron_commits.json()

iron_commits.headers
#Last modified = Thu, 07 Mar 2019 15:49:16 GMT
#Desde el 7 marzo de 2019 no hay commits