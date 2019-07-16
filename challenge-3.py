import requests
import pandas as pd
from pandas.io.json import json_normalize

#access contents page
ACCESS_TOKEN = '83ca47cf8d898a4d9722c56c784a140be276ab92'
scavenger_contents = requests.get('http://api.github.com/repos/ironhack-datalabs/scavenger/contents', ACCESS_TOKEN).json()
print(scavenger_contents)

#turn it into dataframe to read better:
scavenger_contents = pd.DataFrame(scavenger_contents)
scavenger_contents

#get the list of urls to iterate over
links = scavenger_contents['url']
links

#get contents of all links that are directories (ignore loose files) and get them into a files dataframe
files = requests.get(f'{links[0]}', ACCESS_TOKEN).json()
files = pd.DataFrame(files)
for a in range(1,len(scavenger_contents['type'])):
    if scavenger_contents['type'][a] == 'dir':
        files = pd.concat([files, pd.DataFrame(requests.get(f'{links[a]}', ACCESS_TOKEN).json())], axis=0)

#from those, get all the files that are from the game, then sort them
scavenger = [file for file in files['name'] if file.endswith('.scavengerhunt')]
scavenger = sorted(scavenger)
scavenger

#use the file names and order to request the files again, now with the exact url
message_json = []
for l in files['url']:
    for n in scavenger:
        if n in l:
            message_json.append(requests.get(f'{l}', ACCESS_TOKEN).json())

message_df = pd.DataFrame(message_json)

#the message is in a column called "content". Get that column to a list.
message = message_df['content'].tolist()

#Cannot read, coding is base64. convert every element in the list to read.
import base64
for mes in message:
    print(base64.b64decode(mes))