import pickle  # Importing the pickle module for serialization

class Venue:
    # Define a class to represent a venue
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        # Initialize venue attributes
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    @classmethod
    def add_venue(cls, venue_id, name, address, contact, min_guests, max_guests):
        # Class method to add a new venue to the database
        # Create a new venue object
        new_venue = cls(venue_id, name, address, contact, min_guests, max_guests)
        # Open the venue database file in binary append mode
        with open("venue_database.pickle", "ab") as file:
            # Serialize and write the new venue object to the file
            pickle.dump(new_venue, file)

    @classmethod
    def display_all_venues(cls):
        # Class method to display all venues from the database
        venues = []
        # Open the venue database file in binary read mode
        with open("venue_database.pickle", "rb") as file:
            # Read and deserialize venue objects from the file
            while True:
                try:
                    venue = pickle.load(file)
                    # Append the venue object to the list
                    venues.append(venue)
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return venues

    @classmethod
    def display_venue_with_id(cls, venue_id):
        # Class method to display venue with a specific ID from the database
        with open("venue_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize venue objects from the file
                    venue = pickle.load(file)
                    # Check if venue ID matches the specified ID
                    if venue.venue_id == venue_id:
                        # Return the venue object
                        return venue
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def get_all_venues(cls):
        # Class method to retrieve all venues from the database
        venues = []
        try:
            # Try to open the venue database file in binary read mode
            with open("venue_database.pickle", "rb") as file:
                # Read and deserialize venue objects from the file
                while True:
                    try:
                        venue = pickle.load(file)
                        venues.append(venue)
                    except EOFError:
                        # Break the loop when end of file is reached
                        break
        except FileNotFoundError:
            pass
        return venues

    @classmethod
    def delete_venue(cls, venue_id):
        # Class method to delete a venue with specified ID from the database
        venues = cls.get_all_venues()
        found = False
        # Iterate through the list of venues
        for venue in venues:
            if venue.venue_id == venue_id:
                # Remove the venue with specified ID from the list
                venues.remove(venue)
                found = True
                break
        if not found:
            # Raise ValueError if venue with specified ID is not found
            raise ValueError("Venue with specified ID not found!")
        # Open the venue database file in binary write mode
        with open("venue_database.pickle", "wb") as file:
            # Serialize and write each venue object back to the file
            for venue in venues:
                pickle.dump(venue, file)

    @classmethod
    def retrieve_venue(cls, venue_id):
        # Class method to retrieve a venue with specified ID from the database
        with open("venue_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize venue objects from the file
                    venue = pickle.load(file)
                    # Check if venue ID matches the specified ID
                    if venue.venue_id == venue_id:
                        # Return the venue object
                        return venue
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def update_venue(cls, venue_id, name, address, contact, min_guests, max_guests):
        # Class method to update venue information in the database
        venues = cls.display_all_venues()
        for venue in venues:
            if venue.venue_id == venue_id:
                # Update venue attributes with new values
                venue.name = name
                venue.address = address
                venue.contact = contact
                venue.min_guests = min_guests
                venue.max_guests = max_guests
                break
        else:
            # Raise ValueError if venue with specified ID is not found
            raise ValueError("Venue with specified ID not found!")
        
        # Save the updated venue list back to the pickle file
        with open("venue_database.pickle", "wb") as file:
            # Serialize and write each venue object back to the file
            for venue in venues:
                pickle.dump(venue, file)
