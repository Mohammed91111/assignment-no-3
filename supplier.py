import pickle  # Importing the pickle module for serialization

class Supplier:
    # Define a class to represent a supplier
    def __init__(self, supplier_id, name, address, contact, service_provided, min_guests, max_guests):
        # Initialize supplier attributes
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact = contact
        self.service_provided = service_provided
        self.min_guests = min_guests
        self.max_guests = max_guests

    @classmethod
    def add_supplier(cls, supplier_id, name, address, contact, service_provided, min_guests, max_guests):
        # Class method to add a new supplier to the database
        # Create a new supplier object
        new_supplier = cls(supplier_id, name, address, contact, service_provided, min_guests, max_guests)
        # Open the supplier database file in binary append mode
        with open("supplier_database.pickle", "ab") as file:
            # Serialize and write the new supplier object to the file
            pickle.dump(new_supplier, file)

    @classmethod
    def display_all_suppliers(cls):
        # Class method to display all suppliers from the database
        suppliers = []
        # Open the supplier database file in binary read mode
        with open("supplier_database.pickle", "rb") as file:
            # Read and deserialize supplier objects from the file
            while True:
                try:
                    supplier = pickle.load(file)
                    # Append the supplier object to the list
                    suppliers.append(supplier)
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return suppliers

    @classmethod
    def display_supplier_with_id(cls, supplier_id):
        # Class method to display supplier with a specific ID from the database
        with open("supplier_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize supplier objects from the file
                    supplier = pickle.load(file)
                    # Check if supplier ID matches the specified ID
                    if supplier.supplier_id == supplier_id:
                        # Return the supplier object
                        return supplier
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def get_all_suppliers(cls):
        # Class method to retrieve all suppliers from the database
        suppliers = []
        try:
            # Try to open the supplier database file in binary read mode
            with open("supplier_database.pickle", "rb") as file:
                # Read and deserialize supplier objects from the file
                while True:
                    try:
                        supplier = pickle.load(file)
                        suppliers.append(supplier)
                    except EOFError:
                        # Break the loop when end of file is reached
                        break
        except FileNotFoundError:
            pass
        return suppliers

    @classmethod
    def delete_supplier(cls, supplier_id):
        # Class method to delete a supplier with specified ID from the database
        suppliers = cls.get_all_suppliers()
        found = False
        # Iterate through the list of suppliers
        for supplier in suppliers:
            if supplier.supplier_id == supplier_id:
                # Remove the supplier with specified ID from the list
                suppliers.remove(supplier)
                found = True
                break
        if not found:
            # Raise ValueError if supplier with specified ID is not found
            raise ValueError("Supplier with specified ID not found!")
        # Open the supplier database file in binary write mode
        with open("supplier_database.pickle", "wb") as file:
            # Serialize and write each supplier object back to the file
            for supplier in suppliers:
                pickle.dump(supplier, file)

    @classmethod
    def retrieve_supplier(cls, supplier_id):
        # Class method to retrieve a supplier with specified ID from the database
        with open("supplier_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize supplier objects from the file
                    supplier = pickle.load(file)
                    # Check if supplier ID matches the specified ID
                    if supplier.supplier_id == supplier_id:
                        # Return the supplier object
                        return supplier
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None

    @classmethod
    def update_supplier(cls, supplier_id, name, address, contact, service_provided, min_guests, max_guests):
        # Class method to update supplier information in the database
        suppliers = cls.display_all_suppliers()
        for supplier in suppliers:
            if supplier.supplier_id == supplier_id:
                # Update supplier attributes with new values
                supplier.name = name
                supplier.address = address
                supplier.contact = contact
                supplier.service_provided = service_provided
                supplier.min_guests = min_guests
                supplier.max_guests = max_guests
                break
        else:
            # Raise ValueError if supplier with specified ID is not found
            raise ValueError("Supplier with specified ID not found!")
        
        # Save the updated supplier list back to the pickle file
        with open("supplier_database.pickle", "wb") as file:
            # Serialize and write each supplier object back to the file
            for supplier in suppliers:
                pickle.dump(supplier, file)
