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

