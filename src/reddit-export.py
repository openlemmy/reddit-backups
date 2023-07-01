import datetime
import html
import pymongo
import requests
import time
from dotenv import dotenv_values

subreddit = 'CHANGE_ME' # TODO: Change to env variablex
sort = 'asc'
sort_type = 'created_utc'
size = 100

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.subredditArchiveDB
collection = db[subreddit]

def main():
    query_params = {
        'subreddit': subreddit,
        'sort': sort,
        'sort_type': sort_type,
        'size': size,
        'after': 1646299223, # use this to start the search after a specific timestamp
    }

    while True:
        r = requests.get('https://api.pushshift.io/reddit/search/submission/', params=query_params)
        r.raise_for_status()

        j = r.json()
        for post in j['data']:
            id = post['id']
            timestamp = datetime.datetime.utcfromtimestamp(post['created_utc'])
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M")

            reddit_r = requests.get(f'https://www.reddit.com/comments/{id}/.json', headers={'User-Agent': 'Subreddit archiver', 'Cookie': 'Paste your Reddit browser cookie here (needed to access quarantined subreddit)' })
            reddit_r.raise_for_status()
            reddit_json = reddit_r.json()

            post_archive = {
                'id': id,
                'timestamp': timestamp,
                'json': reddit_json
            }

            collection.insert_one(post_archive)
            print(f'Added {id} from {timestamp_str} to the collection')

        query_params['after'] = timestamp


if __name__ == '__main__':
    main()
