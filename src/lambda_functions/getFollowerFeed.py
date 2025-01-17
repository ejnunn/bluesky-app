import json
import os

from atproto import Client
from dotenv import load_dotenv


def lambda_handler(event, context):
    print(event)
    try:
        email = os.environ["EMAIL"]
        password = os.environ["PASSWORD"]
    except:
        load_dotenv()
        email = os.getenv('BLUESKY_EMAIL')
        password = os.getenv('BLUESKY_PASSWORD')


    client = Client()
    profile = client.login(email, password)

    actor = 'ericnunn.bsky.social'
    print(f'Getting feed for {actor}...')
    client_feed = client.get_author_feed(actor=actor,
                    cursor=None,
                    filter=None,
                    limit=None)
    print(f'Got the feed!')
    return {
        'statusCode': 200,
        'body': json.dumps(client_feed)
    }


def main():
    event = {'text': "Getting the feed from actor 'ericnunn.bsky.social'"}
    context = None
    response = lambda_handler(event, context)
    print(f"response : {response}")

if __name__ == '__main__':
    main()