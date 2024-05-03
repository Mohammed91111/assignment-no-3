import pickle  # Import the pickle module for serialization

class Client:
    # Define a class to represent a client
    def __init__(self, client_id, name, address, contact, budget):
        # Initialize client attributes
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact = contact
        self.budget = budget

    @classmethod
    def add_client(cls, client_id, name, address, contact, budget):
        # Class method to add a new client to the database
        # Create a new client object
        new_client = cls(client_id, name, address, contact, budget)
        # Open the client database file in binary append mode
        with open("client_database.pickle", "ab") as file:
            # Serialize and write the new client object to the file
            pickle.dump(new_client, file)

    @classmethod
    def display_all_clients(cls):
        # Class method to display all clients from the database
        clients = []
        # Open the client database file in binary read mode
        with open("client_database.pickle", "rb") as file:
            # Read and deserialize client objects from the file
            while True:
                try:
                    client = pickle.load(file)
                    # Append the client object to the list
                    clients.append(client)
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return clients

    @classmethod
    def display_client_with_id(cls, client_id):
        # Class method to display client with a specific ID from the database
        with open("client_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize client objects from the file
                    client = pickle.load(file)
                    # Check if client ID matches the specified ID
                    if client.client_id == client_id:
                        # Return the client object
                        return client
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def get_all_clients(cls):
        # Class method to retrieve all clients from the database
        clients = []
        try:
            # Try to open the client database file in binary read mode
            with open("client_database.pickle", "rb") as file:
                # Read and deserialize client objects from the file
                while True:
                    try:
                        client = pickle.load(file)
                        clients.append(client)
                    except EOFError:
                        # Break the loop when end of file is reached
                        break
        except FileNotFoundError:
            pass
        return clients

    @classmethod
    def delete_client(cls, client_id):
        # Class method to delete a client with specified ID from the database
        clients = cls.get_all_clients()
        found = False
        # Iterate through the list of clients
        for client in clients:
            if client.client_id == client_id:
                # Remove the client with specified ID from the list
                clients.remove(client)
                found = True
                break
        if not found:
            # Raise ValueError if client with specified ID is not found
            raise ValueError("Client with specified ID not found!")
        # Open the client database file in binary write mode
        with open("client_database.pickle", "wb") as file:
            # Serialize and write each client object back to the file
            for client in clients:
                pickle.dump(client, file)

    @classmethod
    def retrieve_client(cls, client_id):
        # Class method to retrieve a client with specified ID from the database
        with open("client_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize client objects from the file
                    client = pickle.load(file)
                    # Check if client ID matches the specified ID
                    if client.client_id == client_id:
                        # Return the client object
                        return client
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def update_client(cls, client_id, name, address, contact, budget):
        # Class method to update client information in the database
        clients = cls.display_all_clients()
        for client in clients:
            if client.client_id == client_id:
                # Update client attributes with new values
                client.name = name
                client.address = address
                client.contact = contact
                client.budget = budget
                break
        else:
            # Raise ValueError if client with specified ID is not found
            raise ValueError("Client with specified ID not found!")

        # Save the updated client list back to the pickle file
        with open("client_database.pickle", "wb") as file:
            # Serialize and write each client object back to the file
            for client in clients:
                pickle.dump(client, file)
