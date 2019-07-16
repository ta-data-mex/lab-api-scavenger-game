# enter your code below
import requests
import pandas as pd
from pandas.io.json import json_normalize


#keep token in a variable, connect to fork url using token, transform it in json
ACCESS_TOKEN = '83ca47cf8d898a4d9722c56c784a140be276ab92'
madrid = requests.get('http://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/forks', ACCESS_TOKEN).json()

#transform json into pandas dataframe
madrid_df = pd.DataFrame(madrid)

#get unique list of language names by accessing the language column, making it into a set and then a list.
fork_languages = list(set(madrid_df['language']))
print(f'There are forks in these languages {fork_languages}.')

