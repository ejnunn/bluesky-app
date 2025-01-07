import os
from atproto import Client
from dotenv import load_dotenv

class BlueSkyClient:
    def __init__(self, email, password):
        self.client = Client()
        self.profile = self.login(email, password)
    
    def login(self, email, password):
        try:
            profile = self.client.login(email, password)
            print(f"Welcome, {profile.display_name}")
            return profile
        except Exception as e:
            raise ValueError(f"Failed to login: {e}")

    def post_message(self):
        text = input("Post a message: ")
        if text:
            self.client.send_post(text)
            print("Post sent!")
        else:
            print("No message to send.")

    def print_followers(self):
        followers_response = self.client.get_followers(actor=self.profile.handle)
        followers = followers_response['followers']
        if followers:
            for i, follower in enumerate(followers):
                print(f"{i+1}. {follower.display_name}")
        else:
            print("No followers found.")

class BlueSkyApp:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv('BLUESKY_EMAIL')
        self.password = os.getenv('BLUESKY_PASSWORD')
        if not self.email or not self.password:
            raise ValueError("BLUESKY_EMAIL or BLUESKY_PASSWORD environment variable is missing.")
        self.client = BlueSkyClient(self.email, self.password)
        
    def print_menu(self):
        options = ['View Followers', 'Post a Message']
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

    def run(self):
        self.print_menu()
        selection = input("Select an action: ")

        if selection == '1':
            print("Getting your followers...")
            self.client.print_followers()
        elif selection == '2':
            self.client.post_message()
        else:
            print("Invalid selection. Please choose a valid option.")

def main():
    try:
        app = BlueSkyApp()
        app.run()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
