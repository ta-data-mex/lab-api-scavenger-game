#Importar las librerías necesarias
import sys
!{sys.executable} -m pip install requests pandas
import requests
import pandas as pd
from pandas.io.json import json_normalize


iron_scavenger = requests.get('https://api.github.com/repos/ironhack-datalabs/scavenger')
iron_scavenger.json()