import inspect
import os
from BlueSkyClient import BlueSkyClient

from dotenv import load_dotenv


class BlueSkyApp:
    def __init__(self):
        '''
        Load email and password and spin up a client logged in to that account.
        Build a list of menu options for the user to choose from. Each option corresponds to an action with the BlueSky Client API.
        '''
        load_dotenv()
        self.email = os.getenv('BLUESKY_EMAIL')
        self.password = os.getenv('BLUESKY_PASSWORD')
        if not self.email or not self.password:
            raise ValueError("BLUESKY_EMAIL or BLUESKY_PASSWORD environment variable is missing.")
        self.client = BlueSkyClient(self.email, self.password)
        self.menu_options = [   ("1", "View Follows", self.client.get_follows),
                                ("2", "View Followers", self.client.get_followers),
                                ("3", "Get Follower Feed", self.client.get_follower_feed),
                                ("4", "Post Message", self.client.post_message),
                            ]
        
    def print_menu(self):
        for number, name, _ in self.menu_options:
            print(f"{number}. {name}")
        print(f"Type 'q' to quit.")

    def run(self):
        while True:
            self.print_menu()
            choice = input(f"Select an action (1-{len(self.menu_options)}): ")

            matched_option = next((func for number, name, func in self.menu_options if choice == number or choice.lower() == name.lower()), None)

            if matched_option:
                sig = inspect.signature(matched_option)
                param_values = []

                # Prompt user for each parameter
                for param_name, param in sig.parameters.items():
                    if param.default == inspect.Parameter.empty:
                        prompt_text = f" - Enter value for {param_name} (REQUIRED): "
                    else:
                        prompt_text = f" - Enter value for {param_name} (optional, default={param.default}): "

                    user_input = input(prompt_text)

                    # Use default if user skips an optional parameter
                    param_values.append(user_input if user_input else param.default)

                # Pass collected values as a single tuple
                matched_option(*param_values)

            elif choice.lower() == 'q':
                print(f"Goodbye, {self.client.profile.display_name}!")
                break
            else:
                print("Invalid choice. Please try again.")
            print("------------------------")





