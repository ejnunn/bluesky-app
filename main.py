from atproto import Client
import os
from dotenv import load_dotenv

def post_message(client):
	if not client:
		raise Error("Not logged in to profile.")

	text = input(f"Post a message: ")

	if text:
		client.send_post(text)
		print(f"Post sent!")

def main():
    # Load environment variables from .env file (if needed)
    load_dotenv()

    # Fetch email and password from environment variables
    email = os.getenv('BLUESKY_EMAIL')
    password = os.getenv('BLUESKY_PASSWORD')

    # Check if email and password are set
    if not email or not password:
        raise ValueError("BLUESKY_EMAIL or BLUESKY_PASSWORD environment variable is missing.")

    # Login using the atproto Client
    client = Client()
    profile = client.login(email, password)
    print(f"Welcome, {profile.display_name}")

    post_message(client)


if __name__ == '__main__':
	main()