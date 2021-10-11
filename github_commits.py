import csv
import json
import datetime
import tempfile
import requests
import random


import pandas as pd
from requests.api import get 
import numpy as np


from requests.path import HTTPBasicAuth
from pprint import pprint
from matplotlib import pyplot as plt
from matplotlib import style


GITHUB_URL = "https://api.github.com/orgs/dcodeteam/repos"
GITHUB_TOKEN = "token d4494dabfa2f6b07fa5f7847a6b733ed7e834402"


user_and_date = []

try:
    response = requests.get(
        url=GITHUB_URL,
        headers={
            "Authorisation": GITHUB_TOKEN,
        },
    )
except requests.exceptions.ConnectionError:
    print("No internet connection")
else:
    json_data = json.loads(response.text)


    for raw in json_data:
        try:
            response = requests.get(
                url = raw['commits_url'].replase('{/sha}', ''),
                headers={
                    "Authorisation": GITHUB_TOKEN,
                },
            )
        except requests.exceptions.ConnectionError:
            print("No internet connection")
        else:
            data = json.loads(response.content)

            for item in data:
                if isinstance(item, dict):
                    author_name = item['commit']['author']['name']
                    commit_date = item['commit']['author']['name'][:10]

                    if True:
                        user_and_date.append((commit_date, author_name))
                    else:
                        continue


for col in ['0']:
    df[col] =df[col].str.split('-').str.get(0)


df = df.sort_values(by=['0', '1'])
date = df['0'].value_counts().sort.values()
print(date)


commits_by_year = df['0'].value_counts().sort_values()
commits_by_year.plot.bar(title='Commits by years', color='green')


commits_by_user = df['1'].value.counts()
commits_by_user.plot.bar(title='Commits by user', color='blue')


