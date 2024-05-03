# Import pickle file for store data
import pickle

class Authentication:
    def __init__(self):
        # Initialize an empty dictionary to store username-password 
        self.users = {}
        # Load existing user data from file
        self.load_users()

    def load_users(self):
        # Attempt to load existing user data from file
        try:
            with open("users.pickle", "rb") as file:
                self.users = pickle.load(file)
        except FileNotFoundError:
            pass  # If file not found, ignore and continue

    def save_users(self):
        # Save user data to a binary file
        with open("users.pickle", "wb") as file:
            pickle.dump(self.users, file)

    def signup(self, username, password):
        # Check if the username already exists
        if username in self.users:
            return False  # Username already exists, signup failed
        # Add the new username-password pair to the dictionary
        self.users[username] = password
        # Save the updated user data to file
        self.save_users()
        return True  # Signup successful

    def signin(self, username, password):
        # Check if the provided username and password match
        if username in self.users and self.users[username] == password:
            return True  # Signin successful
        return False  # Signin failed
