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

    client.send_post(text=event['text'])

    return {
        'statusCode': 200,
        'body': json.dumps('Posted to Bluesky!')
    }

def main():
    event = {'text': "Test text from an event."}
    context = None
    _ = lambda_handler(event, context)

if __name__ == '__main__':
    main()