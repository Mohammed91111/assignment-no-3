import pickle  # Importing the pickle module for serialization

class Event:
    # Define a class to represent an event
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice):
        # Initialize event attributes
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.suppliers_company = suppliers_company
        self.invoice = invoice

    @classmethod
    def add_event(cls, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice):
        # Class method to add a new event to the database
        # Create a new event object
        new_event = cls(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice)
        # Open the event database file in binary append mode
        with open("event_database.pickle", "ab") as file:
            # Serialize and write the new event object to the file
            pickle.dump(new_event, file)

    @classmethod
    def display_all_events(cls):
        # Class method to display all events from the database
        events = []
        # Open the event database file in binary read mode
        with open("event_database.pickle", "rb") as file:
            # Read and deserialize event objects from the file
            while True:
                try:
                    event = pickle.load(file)
                    # Append the event object to the list
                    events.append(event)
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return events

    @classmethod
    def display_event_with_id(cls, event_id):
        # Class method to display event with a specific ID from the database
        with open("event_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize event objects from the file
                    event = pickle.load(file)
                    # Check if event ID matches the specified ID
                    if event.event_id == event_id:
                        # Return the event object
                        return event
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def get_all_events(cls):
        # Class method to retrieve all events from the database
        events = []
        try:
            # Try to open the event database file in binary read mode
            with open("event_database.pickle", "rb") as file:
                # Read and deserialize event objects from the file
                while True:
                    try:
                        event = pickle.load(file)
                        events.append(event)
                    except EOFError:
                        # Break the loop when end of file is reached
                        break
        except FileNotFoundError:
            pass
        return events

    @classmethod
    def delete_event(cls, event_id):
        # Class method to delete an event with specified ID from the database
        events = cls.get_all_events()
        found = False
        # Iterate through the list of events
        for event in events:
            if event.event_id == event_id:
                # Remove the event with specified ID from the list
                events.remove(event)
                found = True
                break
        if not found:
            # Raise ValueError if event with specified ID is not found
            raise ValueError("Event with specified ID not found!")
        # Open the event database file in binary write mode
        with open("event_database.pickle", "wb") as file:
            # Serialize and write each event object back to the file
            for event in events:
                pickle.dump(event, file)

    @classmethod
    def retrieve_event(cls, event_id):
        # Class method to retrieve an event with specified ID from the database
        with open("event_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize event objects from the file
                    event = pickle.load(file)
                    # Check if event ID matches the specified ID
                    if event.event_id == event_id:
                        # Return the event object
                        return event
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def update_event(cls, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice):
        # Class method to update event information in the database
        events = cls.display_all_events()
        for event in events:
            if event.event_id == event_id:
                # Update event attributes with new values
                event.event_type = event_type
                event.theme = theme
                event.date = date
                event.time = time
                event.duration = duration
                event.venue_address = venue_address
                event.client_id = client_id
                event.guest_list = guest_list
                event.suppliers_company = suppliers_company
                event.invoice = invoice
                break
        else:
            # Raise ValueError if event with specified ID is not found
            raise ValueError("Event with specified ID not found!")
        
        # Save the updated event list back to the pickle file
        with open("event_database.pickle", "wb") as file:
            # Serialize and write each event object back to the file
            for event in events:
                pickle.dump(event, file)
