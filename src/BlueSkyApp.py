import os
from BlueSkyClient import BlueSkyClient

from dotenv import load_dotenv


class BlueSkyApp:
    def __init__(self):
        '''
            - Load email and password and spin up a client logged in to that account
        '''
        load_dotenv()
        self.email = os.getenv('BLUESKY_EMAIL')
        self.password = os.getenv('BLUESKY_PASSWORD')
        if not self.email or not self.password:
            raise ValueError("BLUESKY_EMAIL or BLUESKY_PASSWORD environment variable is missing.")
        self.client = BlueSkyClient(self.email, self.password)
        self.menu_options = [   ("1", "View Follows", self.client.get_follows),
                                ("2", "View Followers", self.client.get_followers),
                                ("3", "Post Message", self.client.post_message),
                            ]
        
    def print_menu(self):
        for number, name, _ in self.menu_options:
            print(f"{number}. {name}")
        print(f"Type 'q' to quit.")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Select an action: ")

            matched_option = next((func for number, name, func in self.menu_options if choice == number or choice.lower() == name.lower()), None)

            if matched_option:
                matched_option()
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice. Please try again.")
            print("------------------------")



