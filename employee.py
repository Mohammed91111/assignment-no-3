import pickle  # Importing the pickle module for serialization

class Employee:
    # Define a class to represent an employee
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id):
        # Initialize employee attributes
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details
        self.manager_id = manager_id

    @classmethod
    def add_employee(cls, name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id):
        # Class method to add a new employee to the database
        # Create a new employee object
        new_employee = cls(name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id)
        # Open the employee database file in binary append mode
        with open("employee_database.pickle", "ab") as file:  # Changed file name to "employee_database.pickle"
            # Serialize and write the new employee object to the file
            pickle.dump(new_employee, file)

    @classmethod
    def display_all_employees(cls):
        # Class method to display all employees from the database
        employees = []
        # Open the employee database file in binary read mode
        with open("employee_database.pickle", "rb") as file:
            # Read and deserialize employee objects from the file
            while True:
                try:
                    employee = pickle.load(file)
                    # Append the employee object to the list
                    employees.append(employee)
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return employees

    @classmethod
    def display_employee_with_id(cls, emp_id):
        # Class method to display employee with a specific ID from the database
        with open("employee_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize employee objects from the file
                    employee = pickle.load(file)
                    # Check if employee ID matches the specified ID
                    if employee.emp_id == emp_id:
                        # Return the employee object
                        return employee
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None
    
    @classmethod
    def get_all_employees(cls):
        # Class method to retrieve all employees from the database
        employees = []
        try:
            # Try to open the employee database file in binary read mode
            with open("employee_database.pickle", "rb") as file:
                # Read and deserialize employee objects from the file
                while True:
                    try:
                        employee = pickle.load(file)
                        employees.append(employee)
                    except EOFError:
                        # Break the loop when end of file is reached
                        break
        except FileNotFoundError:
            pass
        return employees

    @classmethod
    def delete_employee(cls, emp_id):
        # Class method to delete an employee with specified ID from the database
        employees = cls.get_all_employees()
        found = False
        # Iterate through the list of employees
        for employee in employees:
            if employee.emp_id == emp_id:
                # Remove the employee with specified ID from the list
                employees.remove(employee)
                found = True
                break
        if not found:
            # Raise ValueError if employee with specified ID is not found
            raise ValueError("Employee with specified ID not found!")
        # Open the employee database file in binary write mode
        with open("employee_database.pickle", "wb") as file:
            # Serialize and write each employee object back to the file
            for employee in employees:
                pickle.dump(employee, file)

    @classmethod
    def retrieve_employee(cls, emp_id):
        # Class method to retrieve an employee with specified ID from the database
        with open("employee_database.pickle", "rb") as file:
            while True:
                try:
                    # Deserialize employee objects from the file
                    employee = pickle.load(file)
                    # Check if employee ID matches the specified ID
                    if employee.emp_id == emp_id:
                        # Return the employee object
                        return employee
                except EOFError:
                    # Break the loop when end of file is reached
                    break
        return None
    
    @classmethod
    def update_employee(cls, emp_id, name, department, job_title, basic_salary, age, dob, passport_details, manager_id):
        # Class method to update employee information in the database
        employees = cls.display_all_employees()
        for employee in employees:
            if employee.emp_id == emp_id:
                # Update employee attributes with new values
                employee.name = name
                employee.department = department
                employee.job_title = job_title
                employee.basic_salary = basic_salary
                employee.age = age
                employee.dob = dob
                employee.passport_details = passport_details
                employee.manager_id = manager_id
                break
        else:
            # Raise ValueError if employee with specified ID is not found
            raise ValueError("Employee with specified ID not found!")
        
        # Save the updated employee list back to the pickle file
        with open("employee_database.pickle", "wb") as file:
            # Serialize and write each employee object back to the file
            for employee in employees:
                pickle.dump(employee, file)
