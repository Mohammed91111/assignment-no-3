import pickle  # Importing the pickle module for serialization

class Guest:
    # Define a class to represent a guest
    def __init__(self, guest_id, name, address, contact):
        # Initialize guest attributes
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact = contact

    @classmethod
    def add_guest(cls, guest_id, name, address, contact):
        # Class method to add a new guest to the database
        # Create a new guest object
        new_guest = cls(guest_id, name, address, contact)
        # Open the guest database file in binary append mode
        with open("guest_database.pickle", "ab") as file:
            # Serialize and write the new guest object to the file
            pickle.dump(new_guest, file)

    @classmethod
    def display_all_guests(cls):
        # Class method to display all guests from the database
        guests = []
        try:
            # Try to open the guest database file in binary read mode
            with open("guest_database.pickle", "rb") as file:
                # Read and deserialize guest objects from the file
                while True:
                    try:
                        guest = pickle.load(file)
                        guests.append(guest)
                    except EOFError:
                        # Break the loop when end of file is reached
                        break
        except FileNotFoundError:
            pass
        return guests

    @classmethod
    def display_guest_with_id(cls, guest_id):
        # Class method to display guest with a specific ID from the database
        with open("guest_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize guest objects from the file
                    guest = pickle.load(file)
                    # Check if guest ID matches the specified ID
                    if guest.guest_id == guest_id:
                        # Return the guest object
                        return guest
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def delete_guest(cls, guest_id):
        # Class method to delete a guest with specified ID from the database
        guests = cls.display_all_guests()
        found = False
        # Iterate through the list of guests
        for guest in guests:
            if guest.guest_id == guest_id:
                # Remove the guest with specified ID from the list
                guests.remove(guest)
                found = True
                break
        if not found:
            # Raise ValueError if guest with specified ID is not found
            raise ValueError("Guest with specified ID not found!")
        # Open the guest database file in binary write mode
        with open("guest_database.pickle", "wb") as file:
            # Serialize and write each guest object back to the file
            for guest in guests:
                pickle.dump(guest, file)

    @classmethod
    def retrieve_guest(cls, guest_id):
        # Class method to retrieve a guest with specified ID from the database
        with open("guest_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize guest objects from the file
                    guest = pickle.load(file)
                    # Check if guest ID matches the specified ID
                    if guest.guest_id == guest_id:
                        # Return the guest object
                        return guest
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def update_guest(cls, guest_id, name, address, contact):
        # Class method to update guest information in the database
        guests = cls.display_all_guests()
        for guest in guests:
            if guest.guest_id == guest_id:
                # Update guest attributes with new values
                guest.name = name
                guest.address = address
                guest.contact = contact
                break
        else:
            # Raise ValueError if guest with specified ID is not found
            raise ValueError("Guest with specified ID not found!")
        
        # Save the updated guest list back to the pickle file
        with open("guest_database.pickle", "wb") as file:
            # Serialize and write each guest object back to the file
            for guest in guests:
                pickle.dump(guest, file)
