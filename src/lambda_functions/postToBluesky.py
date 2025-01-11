import json
import os

from atproto import Client

def lambda_handler(event, context):
    print(event)
    email = os.environ["EMAIL"]
    password = os.environ["PASSWORD"]

    
    client = Client()
    profile = client.login(email, password)

    client.send_post(text=event['text'])

    return {
        'statusCode': 200,
        'body': json.dumps('Posted to Bluesky!')
    }