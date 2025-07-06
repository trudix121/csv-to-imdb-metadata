import time
import os
import pandas as pd
import requests as rq

base_url = 'https://rest.imdbapi.dev/v2'
df = pd.read_csv('movies.csv', nrows=10000)

def make():
    added = 0
    count = 0
    for i in range(len(df)):
        query = df.iloc[i]['title']
        res = rq.get(f'{base_url}/search/titles?query={query}')
        try:
            data = res.json()['titles'][0]
        except Exception as e:
            print(f"Error decoding JSON for query '{query}': {e}")
            print(res)
            data = {}

        pf = pd.DataFrame([data])
        pf.to_csv("imdb.csv", mode="a", header=not os.path.exists("imdb.csv"), index=False)
        df.drop(i, inplace=True)
        count += 1
        added += 1
        if count == 7:
            print('Limit Reached, Sleep 15 seconds')
            print(f'{added=}')
            time.sleep(15)
            print("Sleep ended")
            count = 0  

    print('Finished writing to imdb.csv')

if __name__ == '__main__':
    make()
