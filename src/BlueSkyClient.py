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

    def print_actors(self, actors):
        """Prints follower information in a readable format."""
        if not actors:
            print("No actors found.")
            return

        print(f"Found {len(actors)} actor(s):\n")
        for actor in actors:
            print(f"🆔 DID: {actor.did}")
            print(f"👤 Handle: @{actor.handle}")
            print(f"📛 Display Name: {actor.display_name or 'N/A'}")
            print(f"📅 Joined: {actor.createdAt}")
            print(f"🔗 Avatar URL: {actor.avatar or 'N/A'}")
            print(f"📝 Description: {actor.description or 'N/A'}")
            print(f"👥 Following You: {'✅ Yes' if actor.viewer.followed_by else '❌ No'}")
            print(f"📌 You Follow: {'✅ Yes' if actor.viewer.following else '❌ No'}")
            print("-" * 50)

    def get_followers(self):
        followers_response = self.client.get_followers(actor=self.profile.handle)
        
        followers = followers_response['followers']
        self.print_actors(followers)

    def get_follows(self):
        follow_response = self.client.get_follows(actor=self.profile.handle)
        follows = follow_response['follows']
        
        self.print_actors(follows)


    def get_actor_feed(self, actor: str, cursor: str = None, filter: str = None, limit: int = None):
        response = self.client.get_author_feed(actor, cursor, filter, limit)
        print(f'DEBUG response = {feed_response}')

        feed = response['feed']
        print(f'DEBUG feed = {feed}')

        