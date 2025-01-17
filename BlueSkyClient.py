from atproto import Client

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

    def get_followers(self):
        followers_response = self.client.get_followers(actor=self.profile.handle)
        followers = followers_response['followers']
        if followers:
            for i, follower in enumerate(followers):
                print(f"{i+1}. {follower.display_name}")
        else:
            print("No followers found.")

    def get_follows(self):
        follow_response = self.client.get_follows(actor=self.profile.handle)
        follows = follow_response['follows']
        if follows:
            for i, follow in enumerate(follows):
                print(f"{i+1}. {follow.display_name}")
        else:
            print("No follows found.")


    def get_follower_feed(self, actor: str, cursor: str | None = None, filter: str | None = None, limit: int | None = None):
        response = self.client.get_actor_feed(actor, cursor, filter, limit)
        print(f'DEBUG response = {feed_response}')

        feed = response['feed']
        print(f'DEBUG feed = {feed}')

        