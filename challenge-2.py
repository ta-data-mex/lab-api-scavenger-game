import requests
import pandas as pd
from pandas.io.json import json_normalize

#access commits page
ACCESS_TOKEN = '83ca47cf8d898a4d9722c56c784a140be276ab92'
madrid_commits = requests.get('http://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/commits', ACCESS_TOKEN)
#use attribute headers to check on the number of pages, total is 11
print(madrid_commits.headers)

#The challenge asks for the commits in the last week, but the last commit in this repo was made 4 months ago, so I will just get the total.
#Now that I know that I have 11 pages of commits, let's get the first one and then loop the request to get the others.
commit_pages = pd.DataFrame(madrid_commits.json())
for p in range(2,12):
    tmp = requests.get(f'http://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/commits?page={p}', ACCESS_TOKEN).json()
    tmp = pd.DataFrame(tmp)
    commit_pages = pd.concat([commit_pages, tmp], axis = 0)
#322 commits en total. Lo queria hacer mas bonito pero no quiero exceder el numero de requests :P
print(commit_pages.count())
