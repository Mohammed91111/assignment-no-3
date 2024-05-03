# Import pickle module
import pickle
# Import tkinter module
import tkinter as tk
from tkinter import ttk, messagebox
# Import Classes from other files
from auth import Authentication
from employee import Employee 
from client import Client 
from event import Event 
from guest import Guest 
from venue import Venue 
from supplier import Supplier 


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#E0F2F1")  # Light green background color

        # Authentication
        self.auth = Authentication()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.root, text="Event Management System", font=("Arial", 24, "bold"), bg="#E0F2F1")
        title_label.pack(pady=20)

        # Exit button
        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
        exit_button.place(x=10, y=10)

        # Username label and entry
        username_label = tk.Label(self.root, text="Username:", font=("Arial", 12), bg="#E0F2F1")
        username_label.place(x=50, y=100)
        self.username_entry = ttk.Entry(self.root, font=("Arial", 12), width=30)
        self.username_entry.place(x=200, y=100)

        # Password label and entry
        password_label = tk.Label(self.root, text="Password:", font=("Arial", 12), bg="#E0F2F1")
        password_label.place(x=50, y=150)
        self.password_entry = ttk.Entry(self.root, show="*", font=("Arial", 12), width=30)
        self.password_entry.place(x=200, y=150)

        # Sign up button
        signup_button = tk.Button(self.root, text="Sign Up", command=self.signup, bg="#FFAB91", fg="white", font=("Arial", 12, "bold"))
        signup_button.place(x=200, y=200)

        # Sign in button
        signin_button = tk.Button(self.root, text="Sign In", command=self.signin, bg="#FFAB91", fg="white", font=("Arial", 12, "bold"))
        signin_button.place(x=300, y=200)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth.signup(username, password):
            tk.messagebox.showinfo("Success", "Sign Up successful!")
        else:
            tk.messagebox.showerror("Error", "Username already exists!")

    def signin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth.signin(username, password):
            tk.messagebox.showinfo("Success", "Sign In successful!")
            self.main_menu_of_tkinter()
        else:
            tk.messagebox.showerror("Error", "Invalid username or password!")

    def main_menu_of_tkinter(self):
        self.root.destroy()  # Close the sign-in window
        main_menu_window = tk.Tk()
        main_menu_window.title("Main Menu")
        main_menu_window.geometry("600x400")
        main_menu_window.configure(bg="#E0F2F1")  # Same background color as the sign-in window

        def exit_app():
            main_menu_window.destroy()

        # Exit button
        exit_button = tk.Button(main_menu_window, text="Exit", command=exit_app, bg="#FFAB91", fg="white", font=("Arial", 12, "bold"))
        exit_button.place(x=10, y=10)

        # Main menu buttons
        button_width = 30  # Set width for all buttons
        button_font = ("Arial", 12, "bold")  # Set font for all buttons

        # Employee Management button
        employee_button = tk.Button(main_menu_window, text="Employee Management", bg="#FFAB91", fg="white", font=button_font, width=button_width, command=lambda: self.open_submenu("Employee Management"))
        employee_button.pack(pady=10)

        # Client Management button
        client_button = tk.Button(main_menu_window, text="Client Management", bg="#FFAB91", fg="white", font=button_font, width=button_width, command=lambda: self.open_submenu("Client Management"))
        client_button.pack(pady=10)

        # Venue Management button
        venue_button = tk.Button(main_menu_window, text="Venue Management", bg="#FFAB91", fg="white", font=button_font, width=button_width, command=lambda: self.open_submenu("Venue Management"))
        venue_button.pack(pady=10)

        # Supplier Management button
        supplier_button = tk.Button(main_menu_window, text="Supplier Management", bg="#FFAB91", fg="white", font=button_font, width=button_width, command=lambda: self.open_submenu("Supplier Management"))
        supplier_button.pack(pady=10)

        # Event Management button
        event_button = tk.Button(main_menu_window, text="Event Management", bg="#FFAB91", fg="white", font=button_font, width=button_width, command=lambda: self.open_submenu("Event Management"))
        event_button.pack(pady=10)

        # Guest Management button
        guest_button = tk.Button(main_menu_window, text="Guest Management", bg="#FFAB91", fg="white", font=button_font, width=button_width, command=lambda: self.open_submenu("Guest Management"))
        guest_button.pack(pady=10)

        # Revenue Management button
        revenue_button = tk.Button(main_menu_window, text="Revenue Management", bg="#FFAB91", fg="white", font=button_font, width=button_width, command=self.revenue_menu)
        revenue_button.pack(pady=10)


        main_menu_window.mainloop()

    def open_submenu(self, menu_title):
        submenu_window = tk.Toplevel()
        submenu_window.title(menu_title)
        submenu_window.geometry("400x350")
        submenu_window.configure(bg="#E0F2F1")  # Same background color as the main menu

        def add_data(data_type):
            if data_type == "Employee Management":
                add_employee()
            elif data_type == "Client Management":
                add_client()
            elif data_type == "Venue Management":
                add_venue()
            elif data_type == "Supplier Management":
                add_supplier()
            elif data_type == "Event Management":
                add_event()
            elif data_type == "Guest Management":
                add_guest()

        def edit_data(data_type):
            if data_type == "Employee Management":
                edit_item()
            elif data_type == "Client Management":
                edit_client()
            elif data_type == "Venue Management":
                edit_venue()
            elif data_type == "Supplier Management":
                edit_supplier()
            elif data_type == "Event Management":
                edit_event()
            elif data_type == "Guest Management":
                edit_guest()

        def delete_data(data_type):
            if data_type == "Employee Management":
                delete_item()
            elif data_type == "Client Management":
                delete_client()
            elif data_type == "Venue Management":
                delete_venue()
            elif data_type == "Supplier Management":
                delete_supplier()
            elif data_type == "Event Management":
                delete_event()
            elif data_type == "Guest Management":
                delete_guest()

        def display_all_data(data_type):
            if data_type == "Employee Management":
                display_all_employees()
            elif data_type == "Client Management":
                display_all_clients()
            elif data_type == "Venue Management":
                display_all_venues()
            elif data_type == "Supplier Management":
                display_all_suppliers()
            elif data_type == "Event Management":
                display_all_events()
            elif data_type == "Guest Management":
                display_all_guests()

        def display_data_with_id(data_type):
            if data_type == "Employee Management":
                display_item_with_id()
            elif data_type == "Client Management":
                display_client_with_id()
            elif data_type == "Venue Management":
                display_venue_with_id()
            elif data_type == "Supplier Management":
                display_supplier_with_id()
            elif data_type == "Event Management":
                display_event_with_id()
            elif data_type == "Guest Management":
                display_guest_with_id()




        def add_employee():  # Add Employee functionality
            # Create the Employee Add menu
            add_employee_window = tk.Toplevel()
            add_employee_window.title("Add Employee")
            add_employee_window.geometry("280x350")
            add_employee_window.configure(bg="#E0F2F1")

            # Function to save employee data
            def save_employee():
                # Get data from entry fields
                name = name_entry.get()
                emp_id = emp_id_entry.get()
                department = department_entry.get()
                job_title = job_title_entry.get()
                basic_salary = basic_salary_entry.get()
                age = age_entry.get()
                dob = dob_entry.get()
                passport_details = passport_details_entry.get()
                manager_id = manager_id_entry.get()

                # Validate fields
                if not (name and emp_id and department and job_title and basic_salary and age and dob and passport_details and manager_id):
                    tk.messagebox.showerror("Error", "All fields are required!")
                    return

                # Validate name (assuming it should contain only alphabetic characters)
                if not name.isalpha():
                    tk.messagebox.showerror("Error", "Name should contain only alphabetic characters!")
                    return
                # Validate employee ID (assuming it should be numeric)
                if not emp_id.isdigit():
                    tk.messagebox.showerror("Error", "Employee ID should contain only digits!")
                    return
                # Call add_employee method from Employee class to save data
                Employee.add_employee(name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id)
                tk.messagebox.showinfo("Success", "Employee added successfully!")
                add_employee_window.destroy()  # Close the Add Employee window

            # Labels and Entry fields for Employee details
            tk.Label(add_employee_window, text="Name:", bg="#E0F2F1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
            name_entry = tk.Entry(add_employee_window)
            name_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Employee ID:", bg="#E0F2F1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
            emp_id_entry = tk.Entry(add_employee_window)
            emp_id_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Department:", bg="#E0F2F1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
            department_entry = tk.Entry(add_employee_window)
            department_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Job Title:", bg="#E0F2F1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
            job_title_entry = tk.Entry(add_employee_window)
            job_title_entry.grid(row=3, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Basic Salary:", bg="#E0F2F1").grid(row=4, column=0, padx=10, pady=5, sticky="e")
            basic_salary_entry = tk.Entry(add_employee_window)
            basic_salary_entry.grid(row=4, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Age:", bg="#E0F2F1").grid(row=5, column=0, padx=10, pady=5, sticky="e")
            age_entry = tk.Entry(add_employee_window)
            age_entry.grid(row=5, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Date of Birth:", bg="#E0F2F1").grid(row=6, column=0, padx=10, pady=5, sticky="e")
            dob_entry = tk.Entry(add_employee_window)
            dob_entry.grid(row=6, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Passport Details:", bg="#E0F2F1").grid(row=7, column=0, padx=10, pady=5, sticky="e")
            passport_details_entry = tk.Entry(add_employee_window)
            passport_details_entry.grid(row=7, column=1, padx=10, pady=5)

            tk.Label(add_employee_window, text="Manager ID:", bg="#E0F2F1").grid(row=8, column=0, padx=10, pady=5, sticky="e")
            manager_id_entry = tk.Entry(add_employee_window)
            manager_id_entry.grid(row=8, column=1, padx=10, pady=5)

            # Save button
            save_button = tk.Button(add_employee_window, text="Save", bg="#FFAB91", fg="white", font=("Arial", 10, "bold"), command=save_employee)
            save_button.grid(row=9, column=0, columnspan=2, pady=10)

        def edit_item():
            edit_employee_window = tk.Toplevel()
            edit_employee_window.title("Edit Employee")
            edit_employee_window.geometry("280x700")
            edit_employee_window.configure(bg="#E0F2F1")

            def search_employee():
                emp_id = emp_id_entry.get()
                employee = Employee.display_employee_with_id(emp_id)
                if employee:
                    # Populate entry fields with existing employee data for editing
                    name_entry.delete(0, tk.END)
                    name_entry.insert(0, employee.name)
                    department_entry.delete(0, tk.END)
                    department_entry.insert(0, employee.department)
                    job_title_entry.delete(0, tk.END)
                    job_title_entry.insert(0, employee.job_title)
                    basic_salary_entry.delete(0, tk.END)
                    basic_salary_entry.insert(0, employee.basic_salary)
                    age_entry.delete(0, tk.END)
                    age_entry.insert(0, employee.age)
                    dob_entry.delete(0, tk.END)
                    dob_entry.insert(0, employee.dob)
                    passport_details_entry.delete(0, tk.END)
                    passport_details_entry.insert(0, employee.passport_details)
                    manager_id_entry.delete(0, tk.END)
                    manager_id_entry.insert(0, employee.manager_id)
                else:
                    tk.messagebox.showinfo("Error", "Employee with specified ID not found!")

            def save_changes():
                # Get updated data from entry fields
                emp_id = emp_id_entry.get()  # Retrieve the employee ID again
                name = name_entry.get()
                department = department_entry.get()
                job_title = job_title_entry.get()
                basic_salary = basic_salary_entry.get()
                age = age_entry.get()
                dob = dob_entry.get()
                passport_details = passport_details_entry.get()
                manager_id = manager_id_entry.get()
                
                # Update employee data
                try:
                    Employee.update_employee(emp_id, name, department, job_title, basic_salary, age, dob, passport_details, manager_id)
                    tk.messagebox.showinfo("Success", "Employee details updated successfully!")
                    edit_employee_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"Failed to update employee details: {str(e)}")

            tk.Label(edit_employee_window, text="Enter Employee ID:", bg="#E0F2F1").pack(pady=5)
            emp_id_entry = tk.Entry(edit_employee_window)
            emp_id_entry.pack(pady=5)
            search_button = tk.Button(edit_employee_window, text="Search", command=search_employee, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            search_button.pack(pady=5)

            # Labels and Entry fields for Employee details
            tk.Label(edit_employee_window, text="Name:", bg="#E0F2F1").pack(pady=5)
            name_entry = tk.Entry(edit_employee_window)
            name_entry.pack(pady=5)

            tk.Label(edit_employee_window, text="Department:", bg="#E0F2F1").pack(pady=5)
            department_entry = tk.Entry(edit_employee_window)
            department_entry.pack(pady=5)

            tk.Label(edit_employee_window, text="Job Title:", bg="#E0F2F1").pack(pady=5)
            job_title_entry = tk.Entry(edit_employee_window)
            job_title_entry.pack(pady=5)

            tk.Label(edit_employee_window, text="Basic Salary:", bg="#E0F2F1").pack(pady=5)
            basic_salary_entry = tk.Entry(edit_employee_window)
            basic_salary_entry.pack(pady=5)

            tk.Label(edit_employee_window, text="Age:", bg="#E0F2F1").pack(pady=5)
            age_entry = tk.Entry(edit_employee_window)
            age_entry.pack(pady=5)

            tk.Label(edit_employee_window, text="Date of Birth:", bg="#E0F2F1").pack(pady=5)
            dob_entry = tk.Entry(edit_employee_window)
            dob_entry.pack(pady=5)

            tk.Label(edit_employee_window, text="Passport Details:", bg="#E0F2F1").pack(pady=5)
            passport_details_entry = tk.Entry(edit_employee_window)
            passport_details_entry.pack(pady=5)

            tk.Label(edit_employee_window, text="Manager ID:", bg="#E0F2F1").pack(pady=5)
            manager_id_entry = tk.Entry(edit_employee_window)
            manager_id_entry.pack(pady=5)

            save_button = tk.Button(edit_employee_window, text="Save Changes", command=save_changes, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            save_button.pack(pady=10)

        def delete_item():
            # Create the Delete Employee menu
            delete_employee_window = tk.Toplevel()
            delete_employee_window.title("Delete Employee")
            delete_employee_window.geometry("400x150")
            delete_employee_window.configure(bg="#E0F2F1")

            # Function to delete employee
            def delete_employee():
                emp_id = emp_id_entry.get()
                try:
                    Employee.delete_employee(emp_id)
                    tk.messagebox.showinfo("Success", "Employee deleted successfully!")
                    delete_employee_window.destroy()
                except ValueError:
                    tk.messagebox.showerror("Error", "Employee with specified ID not found!")

            tk.Label(delete_employee_window, text="Enter Employee ID:", bg="#E0F2F1").pack(pady=5)
            emp_id_entry = tk.Entry(delete_employee_window)
            emp_id_entry.pack(pady=5)
            delete_button = tk.Button(delete_employee_window, text="Delete", command=delete_employee, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            delete_button.pack(pady=5)

        def display_all_employees():  # Display All Employees functionality
            # Create the Display All Employees menu
            display_employees_window = tk.Toplevel()
            display_employees_window.title("Display All Employees")
            display_employees_window.geometry("1050x400")
            display_employees_window.configure(bg="#E0F2F1")

            # Retrieve all employees data
            employees = Employee.display_all_employees()

            # Display employee data
            for i, employee in enumerate(employees):
                tk.Label(display_employees_window, text=f"Name: {employee.name}").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Employee ID: {employee.emp_id}").grid(row=i, column=1, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Department: {employee.department}").grid(row=i, column=2, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Job Title: {employee.job_title}").grid(row=i, column=3, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Basic Salary: {employee.basic_salary}").grid(row=i, column=4, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Age: {employee.age}").grid(row=i, column=5, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Date of Birth: {employee.dob}").grid(row=i, column=6, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Passport Details: {employee.passport_details}").grid(row=i, column=7, padx=10, pady=5, sticky="w")
                tk.Label(display_employees_window, text=f"Manager ID: {employee.manager_id}").grid(row=i, column=8, padx=10, pady=5, sticky="w")

        def display_item_with_id():  # Display Employee with ID functionality
        # Create the Display Employee with ID menu
            display_employee_with_id_window = tk.Toplevel()
            display_employee_with_id_window.title("Display Employee with ID")
            display_employee_with_id_window.geometry("1050x400")
            display_employee_with_id_window.configure(bg="#E0F2F1")

            # Function to display employee with ID
            def display_employee():
                emp_id = emp_id_entry.get()
                employee = Employee.display_employee_with_id(emp_id)  # Use Employee class instead of employee object
                if employee:
                    # Display employee details in table-like format
                    tree = ttk.Treeview(display_employee_with_id_window)
                    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
                    tree.heading("#0", text="Name")
                    tree.heading("1", text="Employee ID", anchor=tk.CENTER)
                    tree.heading("2", text="Department", anchor=tk.CENTER)
                    tree.heading("3", text="Job Title", anchor=tk.CENTER)
                    tree.heading("4", text="Basic Salary", anchor=tk.CENTER)
                    tree.heading("5", text="Age", anchor=tk.CENTER)
                    tree.heading("6", text="Date of Birth", anchor=tk.CENTER)
                    tree.heading("7", text="Passport Details", anchor=tk.CENTER)
                    tree.heading("8", text="Manager ID", anchor=tk.CENTER)

                    tree.column("#0", width=150)
                    tree.column("1", width=100)
                    tree.column("2", width=100)
                    tree.column("3", width=100)
                    tree.column("4", width=100)
                    tree.column("5", width=100)
                    tree.column("6", width=100)
                    tree.column("7", width=150)
                    tree.column("8", width=100)

                    tree.insert("", "end", text=employee.name, values=(employee.emp_id, employee.department, employee.job_title, employee.basic_salary, employee.age, employee.dob, employee.passport_details, employee.manager_id))
                    tree.pack(expand=True, fill=tk.BOTH)

                else:
                    tk.messagebox.showinfo("Error", "Employee with specified ID not found!")

            tk.Label(display_employee_with_id_window, text="Enter Employee ID:", bg="#E0F2F1").pack(pady=5)
            emp_id_entry = tk.Entry(display_employee_with_id_window)
            emp_id_entry.pack(pady=5)
            display_button = tk.Button(display_employee_with_id_window, text="Display", command=display_employee, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            display_button.pack(pady=5)




        def add_client():  # Add Client functionality
            # Create the Client Add menu
            add_client_window = tk.Toplevel()
            add_client_window.title("Add Client")
            add_client_window.geometry("280x350")
            add_client_window.configure(bg="#E0F2F1")

            # Function to save client data
            def save_client():
                # Get data from entry fields
                client_id = client_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()
                budget = budget_entry.get()

                # Validate fields
                if not (client_id and name and address and contact and budget):
                    tk.messagebox.showerror("Error", "All fields are required!")
                    return

                # Validate client ID (assuming it should be numeric)
                if not client_id.isdigit():
                    tk.messagebox.showerror("Error", "Client ID should contain only digits!")
                    return
                
                # Call add_client method from Client class to save data
                Client.add_client(client_id, name, address, contact, budget)
                tk.messagebox.showinfo("Success", "Client added successfully!")
                add_client_window.destroy()  # Close the Add Client window

            # Labels and Entry fields for Client details
            tk.Label(add_client_window, text="Client ID:", bg="#E0F2F1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
            client_id_entry = tk.Entry(add_client_window)
            client_id_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(add_client_window, text="Name:", bg="#E0F2F1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
            name_entry = tk.Entry(add_client_window)
            name_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(add_client_window, text="Address:", bg="#E0F2F1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
            address_entry = tk.Entry(add_client_window)
            address_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(add_client_window, text="Contact:", bg="#E0F2F1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
            contact_entry = tk.Entry(add_client_window)
            contact_entry.grid(row=3, column=1, padx=10, pady=5)

            tk.Label(add_client_window, text="Budget:", bg="#E0F2F1").grid(row=4, column=0, padx=10, pady=5, sticky="e")
            budget_entry = tk.Entry(add_client_window)
            budget_entry.grid(row=4, column=1, padx=10, pady=5)

            # Save button
            save_button = tk.Button(add_client_window, text="Save", bg="#FFAB91", fg="white", font=("Arial", 10, "bold"), command=save_client)
            save_button.grid(row=5, column=0, columnspan=2, pady=10)

        def edit_client():
            edit_client_window = tk.Toplevel()
            edit_client_window.title("Edit Client")
            edit_client_window.geometry("280x700")
            edit_client_window.configure(bg="#E0F2F1")

            def search_client():
                client_id = client_id_entry.get()
                client = Client.display_client_with_id(client_id)
                if client:
                    name_entry.delete(0, tk.END)
                    name_entry.insert(0, client.name)
                    address_entry.delete(0, tk.END)
                    address_entry.insert(0, client.address)
                    contact_entry.delete(0, tk.END)
                    contact_entry.insert(0, client.contact)
                    budget_entry.delete(0, tk.END)
                    budget_entry.insert(0, client.budget)
                else:
                    tk.messagebox.showinfo("Error", "Client with specified ID not found!")

            def save_changes():
                client_id = client_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()
                budget = budget_entry.get()
                
                try:
                    Client.update_client(client_id, name, address, contact, budget)
                    tk.messagebox.showinfo("Success", "Client details updated successfully!")
                    edit_client_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"Failed to update client details: {str(e)}")

            tk.Label(edit_client_window, text="Enter Client ID:", bg="#E0F2F1").pack(pady=5)
            client_id_entry = tk.Entry(edit_client_window)
            client_id_entry.pack(pady=5)
            search_button = tk.Button(edit_client_window, text="Search", command=search_client, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            search_button.pack(pady=5)

            tk.Label(edit_client_window, text="Name:", bg="#E0F2F1").pack(pady=5)
            name_entry = tk.Entry(edit_client_window)
            name_entry.pack(pady=5)

            tk.Label(edit_client_window, text="Address:", bg="#E0F2F1").pack(pady=5)
            address_entry = tk.Entry(edit_client_window)
            address_entry.pack(pady=5)

            tk.Label(edit_client_window, text="Contact:", bg="#E0F2F1").pack(pady=5)
            contact_entry = tk.Entry(edit_client_window)
            contact_entry.pack(pady=5)

            tk.Label(edit_client_window, text="Budget:", bg="#E0F2F1").pack(pady=5)
            budget_entry = tk.Entry(edit_client_window)
            budget_entry.pack(pady=5)

            save_button = tk.Button(edit_client_window, text="Save Changes", command=save_changes, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            save_button.pack(pady=10)

        def delete_client():  # Delete Client functionality
            # Create the Delete Client menu
            delete_client_window = tk.Toplevel()
            delete_client_window.title("Delete Client")
            delete_client_window.geometry("280x150")
            delete_client_window.configure(bg="#E0F2F1")

            # Function to delete client
            def delete_client():
                client_id = client_id_entry.get()
                try:
                    Client.delete_client(client_id)
                    tk.messagebox.showinfo("Success", "Client deleted successfully!")
                    delete_client_window.destroy()
                except ValueError:
                    tk.messagebox.showerror("Error", "Client with specified ID not found!")

            tk.Label(delete_client_window, text="Enter Client ID:", bg="#E0F2F1").pack(pady=5)
            client_id_entry = tk.Entry(delete_client_window)
            client_id_entry.pack(pady=5)
            delete_button = tk.Button(delete_client_window, text="Delete", command=delete_client, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            delete_button.pack(pady=5)

        def display_all_clients():  # Display All Clients functionality
            # Create the Display All Clients menu
            display_clients_window = tk.Toplevel()
            display_clients_window.title("Display All Clients")
            display_clients_window.geometry("1050x400")
            display_clients_window.configure(bg="#E0F2F1")

            # Retrieve all clients data
            clients = Client.get_all_clients()

            # Display client data
            for i, client in enumerate(clients):
                tk.Label(display_clients_window, text=f"Name: {client.name}").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                tk.Label(display_clients_window, text=f"Client ID: {client.client_id}").grid(row=i, column=1, padx=10, pady=5, sticky="w")
                tk.Label(display_clients_window, text=f"Address: {client.address}").grid(row=i, column=2, padx=10, pady=5, sticky="w")
                tk.Label(display_clients_window, text=f"Contact: {client.contact}").grid(row=i, column=3, padx=10, pady=5, sticky="w")
                tk.Label(display_clients_window, text=f"Budget: {client.budget}").grid(row=i, column=4, padx=10, pady=5, sticky="w")

        def display_client_with_id():  # Display Client with ID functionality
            # Create the Display Client with ID menu
            display_client_with_id_window = tk.Toplevel()
            display_client_with_id_window.title("Display Client with ID")
            display_client_with_id_window.geometry("1050x400")
            display_client_with_id_window.configure(bg="#E0F2F1")

            # Function to display client with ID
            def display_client():
                client_id = client_id_entry.get()
                client = Client.display_client_with_id(client_id)  # Use Client class instead of client object
                if client:
                    # Display client details in table-like format
                    tree = ttk.Treeview(display_client_with_id_window)
                    tree["columns"] = ("1", "2", "3", "4", "5")
                    tree.heading("#0", text="Name")
                    tree.heading("1", text="Client ID", anchor=tk.CENTER)
                    tree.heading("2", text="Address", anchor=tk.CENTER)
                    tree.heading("3", text="Contact", anchor=tk.CENTER)
                    tree.heading("4", text="Budget", anchor=tk.CENTER)

                    tree.column("#0", width=150)
                    tree.column("1", width=100)
                    tree.column("2", width=200)
                    tree.column("3", width=150)
                    tree.column("4", width=100)

                    tree.insert("", "end", text=client.name, values=(client.client_id, client.address, client.contact, client.budget))
                    tree.pack(expand=True, fill=tk.BOTH)

                else:
                    tk.messagebox.showinfo("Error", "Client with specified ID not found!")

            tk.Label(display_client_with_id_window, text="Enter Client ID:", bg="#E0F2F1").pack(pady=5)
            client_id_entry = tk.Entry(display_client_with_id_window)
            client_id_entry.pack(pady=5)
            display_button = tk.Button(display_client_with_id_window, text="Display", command=display_client, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            display_button.pack(pady=5)




        def add_venue():  # Add Venue functionality
            # Create the Venue Add menu
            add_venue_window = tk.Toplevel()
            add_venue_window.title("Add Venue")
            add_venue_window.geometry("280x350")
            add_venue_window.configure(bg="#E0F2F1")

            # Function to save venue data
            def save_venue():
                # Get data from entry fields
                venue_id = venue_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()
                min_guests = min_guests_entry.get()
                max_guests = max_guests_entry.get()

                # Validate fields
                if not (venue_id and name and address and contact and min_guests and max_guests):
                    tk.messagebox.showerror("Error", "All fields are required!")
                    return

                # Validate venue ID (assuming it should be numeric)
                if not venue_id.isdigit():
                    tk.messagebox.showerror("Error", "Venue ID should contain only digits!")
                    return

                # Call add_venue method from Venue class to save data
                Venue.add_venue(venue_id, name, address, contact, min_guests, max_guests)
                tk.messagebox.showinfo("Success", "Venue added successfully!")
                add_venue_window.destroy()  # Close the Add Venue window

            # Labels and Entry fields for Venue details
            tk.Label(add_venue_window, text="Venue ID:", bg="#E0F2F1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
            venue_id_entry = tk.Entry(add_venue_window)
            venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(add_venue_window, text="Name:", bg="#E0F2F1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
            name_entry = tk.Entry(add_venue_window)
            name_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(add_venue_window, text="Address:", bg="#E0F2F1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
            address_entry = tk.Entry(add_venue_window)
            address_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(add_venue_window, text="Contact:", bg="#E0F2F1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
            contact_entry = tk.Entry(add_venue_window)
            contact_entry.grid(row=3, column=1, padx=10, pady=5)

            tk.Label(add_venue_window, text="Min Guests:", bg="#E0F2F1").grid(row=4, column=0, padx=10, pady=5, sticky="e")
            min_guests_entry = tk.Entry(add_venue_window)
            min_guests_entry.grid(row=4, column=1, padx=10, pady=5)

            tk.Label(add_venue_window, text="Max Guests:", bg="#E0F2F1").grid(row=5, column=0, padx=10, pady=5, sticky="e")
            max_guests_entry = tk.Entry(add_venue_window)
            max_guests_entry.grid(row=5, column=1, padx=10, pady=5)

            # Save button
            save_button = tk.Button(add_venue_window, text="Save", bg="#FFAB91", fg="white", font=("Arial", 10, "bold"), command=save_venue)
            save_button.grid(row=6, column=0, columnspan=2, pady=10)

        def edit_venue():
            edit_venue_window = tk.Toplevel()
            edit_venue_window.title("Edit Venue")
            edit_venue_window.geometry("280x700")
            edit_venue_window.configure(bg="#E0F2F1")

            def search_venue():
                venue_id = venue_id_entry.get()
                venue = Venue.display_venue_with_id(venue_id)
                if venue:
                    name_entry.delete(0, tk.END)
                    name_entry.insert(0, venue.name)
                    address_entry.delete(0, tk.END)
                    address_entry.insert(0, venue.address)
                    contact_entry.delete(0, tk.END)
                    contact_entry.insert(0, venue.contact)
                    min_guests_entry.delete(0, tk.END)
                    min_guests_entry.insert(0, venue.min_guests)
                    max_guests_entry.delete(0, tk.END)
                    max_guests_entry.insert(0, venue.max_guests)
                else:
                    tk.messagebox.showinfo("Error", "Venue with specified ID not found!")

            def save_changes():
                venue_id = venue_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()
                min_guests = min_guests_entry.get()
                max_guests = max_guests_entry.get()
                
                try:
                    Venue.update_venue(venue_id, name, address, contact, min_guests, max_guests)
                    tk.messagebox.showinfo("Success", "Venue details updated successfully!")
                    edit_venue_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"Failed to update venue details: {str(e)}")

            tk.Label(edit_venue_window, text="Enter Venue ID:", bg="#E0F2F1").pack(pady=5)
            venue_id_entry = tk.Entry(edit_venue_window)
            venue_id_entry.pack(pady=5)
            search_button = tk.Button(edit_venue_window, text="Search", command=search_venue, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            search_button.pack(pady=5)

            tk.Label(edit_venue_window, text="Name:", bg="#E0F2F1").pack(pady=5)
            name_entry = tk.Entry(edit_venue_window)
            name_entry.pack(pady=5)

            tk.Label(edit_venue_window, text="Address:", bg="#E0F2F1").pack(pady=5)
            address_entry = tk.Entry(edit_venue_window)
            address_entry.pack(pady=5)

            tk.Label(edit_venue_window, text="Contact:", bg="#E0F2F1").pack(pady=5)
            contact_entry = tk.Entry(edit_venue_window)
            contact_entry.pack(pady=5)

            tk.Label(edit_venue_window, text="Min Guests:", bg="#E0F2F1").pack(pady=5)
            min_guests_entry = tk.Entry(edit_venue_window)
            min_guests_entry.pack(pady=5)

            tk.Label(edit_venue_window, text="Max Guests:", bg="#E0F2F1").pack(pady=5)
            max_guests_entry = tk.Entry(edit_venue_window)
            max_guests_entry.pack(pady=5)

            save_button = tk.Button(edit_venue_window, text="Save Changes", command=save_changes, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            save_button.pack(pady=10)

        def delete_venue():  # Delete Venue functionality
            # Create the Delete Venue menu
            delete_venue_window = tk.Toplevel()
            delete_venue_window.title("Delete Venue")
            delete_venue_window.geometry("280x150")
            delete_venue_window.configure(bg="#E0F2F1")

            # Function to delete venue
            def delete_venue():
                venue_id = venue_id_entry.get()
                try:
                    Venue.delete_venue(venue_id)
                    tk.messagebox.showinfo("Success", "Venue deleted successfully!")
                    delete_venue_window.destroy()
                except ValueError:
                    tk.messagebox.showerror("Error", "Venue with specified ID not found!")

            tk.Label(delete_venue_window, text="Enter Venue ID:", bg="#E0F2F1").pack(pady=5)
            venue_id_entry = tk.Entry(delete_venue_window)
            venue_id_entry.pack(pady=5)
            delete_button = tk.Button(delete_venue_window, text="Delete", command=delete_venue, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            delete_button.pack(pady=5)

        def display_all_venues():  # Display All Venues functionality
            # Create the Display All Venues menu
            display_venues_window = tk.Toplevel()
            display_venues_window.title("Display All Venues")
            display_venues_window.geometry("1050x400")
            display_venues_window.configure(bg="#E0F2F1")

            # Retrieve all venues data
            venues = Venue.get_all_venues()

            # Display venue data
            for i, venue in enumerate(venues):
                tk.Label(display_venues_window, text=f"Name: {venue.name}").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                tk.Label(display_venues_window, text=f"Venue ID: {venue.venue_id}").grid(row=i, column=1, padx=10, pady=5, sticky="w")
                tk.Label(display_venues_window, text=f"Address: {venue.address}").grid(row=i, column=2, padx=10, pady=5, sticky="w")
                tk.Label(display_venues_window, text=f"Contact: {venue.contact}").grid(row=i, column=3, padx=10, pady=5, sticky="w")
                tk.Label(display_venues_window, text=f"Min Guests: {venue.min_guests}").grid(row=i, column=4, padx=10, pady=5, sticky="w")
                tk.Label(display_venues_window, text=f"Max Guests: {venue.max_guests}").grid(row=i, column=5, padx=10, pady=5, sticky="w")

        def display_venue_with_id():  # Display Venue with ID functionality
            # Create the Display Venue with ID menu
            display_venue_with_id_window = tk.Toplevel()
            display_venue_with_id_window.title("Display Venue with ID")
            display_venue_with_id_window.geometry("1050x400")
            display_venue_with_id_window.configure(bg="#E0F2F1")

            # Function to display venue with ID
            def display_venue():
                venue_id = venue_id_entry.get()
                venue = Venue.display_venue_with_id(venue_id)  # Use Venue class instead of venue object
                if venue:
                    # Display venue details in table-like format
                    tree = ttk.Treeview(display_venue_with_id_window)
                    tree["columns"] = ("1", "2", "3", "4", "5", "6")
                    tree.heading("#0", text="Name")
                    tree.heading("1", text="Venue ID", anchor=tk.CENTER)
                    tree.heading("2", text="Address", anchor=tk.CENTER)
                    tree.heading("3", text="Contact", anchor=tk.CENTER)
                    tree.heading("4", text="Min Guests", anchor=tk.CENTER)
                    tree.heading("5", text="Max Guests", anchor=tk.CENTER)

                    tree.column("#0", width=150)
                    tree.column("1", width=100)
                    tree.column("2", width=200)
                    tree.column("3", width=150)
                    tree.column("4", width=100)
                    tree.column("5", width=100)

                    tree.insert("", "end", text=venue.name, values=(venue.venue_id, venue.address, venue.contact, venue.min_guests, venue.max_guests))
                    tree.pack(expand=True, fill=tk.BOTH)

                else:
                    tk.messagebox.showinfo("Error", "Venue with specified ID not found!")

            tk.Label(display_venue_with_id_window, text="Enter Venue ID:", bg="#E0F2F1").pack(pady=5)
            venue_id_entry = tk.Entry(display_venue_with_id_window)
            venue_id_entry.pack(pady=5)
            display_button = tk.Button(display_venue_with_id_window, text="Display", command=display_venue, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            display_button.pack(pady=5)
     



        def add_supplier():  # Add Supplier functionality
            # Create the Supplier Add menu
            add_supplier_window = tk.Toplevel()
            add_supplier_window.title("Add Supplier")
            add_supplier_window.geometry("280x350")
            add_supplier_window.configure(bg="#E0F2F1")

            # Function to save supplier data
            def save_supplier():
                # Get data from entry fields
                supplier_id = supplier_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()
                service_provided = service_provided_entry.get()
                min_guests = min_guests_entry.get()
                max_guests = max_guests_entry.get()

                # Validate fields
                if not (supplier_id and name and address and contact and service_provided and min_guests and max_guests):
                    tk.messagebox.showerror("Error", "All fields are required!")
                    return

                # Validate supplier ID (assuming it should be numeric)
                if not supplier_id.isdigit():
                    tk.messagebox.showerror("Error", "Supplier ID should contain only digits!")
                    return
                
                # Call add_supplier method from Supplier class to save data
                Supplier.add_supplier(supplier_id, name, address, contact, service_provided, min_guests, max_guests)
                tk.messagebox.showinfo("Success", "Supplier added successfully!")
                add_supplier_window.destroy()  # Close the Add Supplier window

            # Labels and Entry fields for Supplier details
            tk.Label(add_supplier_window, text="Supplier ID:", bg="#E0F2F1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
            supplier_id_entry = tk.Entry(add_supplier_window)
            supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(add_supplier_window, text="Name:", bg="#E0F2F1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
            name_entry = tk.Entry(add_supplier_window)
            name_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(add_supplier_window, text="Address:", bg="#E0F2F1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
            address_entry = tk.Entry(add_supplier_window)
            address_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(add_supplier_window, text="Contact:", bg="#E0F2F1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
            contact_entry = tk.Entry(add_supplier_window)
            contact_entry.grid(row=3, column=1, padx=10, pady=5)

            tk.Label(add_supplier_window, text="Service Provided:", bg="#E0F2F1").grid(row=4, column=0, padx=10, pady=5, sticky="e")
            service_provided_entry = tk.Entry(add_supplier_window)
            service_provided_entry.grid(row=4, column=1, padx=10, pady=5)

            tk.Label(add_supplier_window, text="Min Guests:", bg="#E0F2F1").grid(row=5, column=0, padx=10, pady=5, sticky="e")
            min_guests_entry = tk.Entry(add_supplier_window)
            min_guests_entry.grid(row=5, column=1, padx=10, pady=5)

            tk.Label(add_supplier_window, text="Max Guests:", bg="#E0F2F1").grid(row=6, column=0, padx=10, pady=5, sticky="e")
            max_guests_entry = tk.Entry(add_supplier_window)
            max_guests_entry.grid(row=6, column=1, padx=10, pady=5)

            # Save button
            save_button = tk.Button(add_supplier_window, text="Save", bg="#FFAB91", fg="white", font=("Arial", 10, "bold"), command=save_supplier)
            save_button.grid(row=7, column=0, columnspan=2, pady=10)

        def edit_supplier():
            edit_supplier_window = tk.Toplevel()
            edit_supplier_window.title("Edit Supplier")
            edit_supplier_window.geometry("280x700")
            edit_supplier_window.configure(bg="#E0F2F1")

            def search_supplier():
                supplier_id = supplier_id_entry.get()
                supplier = Supplier.display_supplier_with_id(supplier_id)
                if supplier:
                    name_entry.delete(0, tk.END)
                    name_entry.insert(0, supplier.name)
                    address_entry.delete(0, tk.END)
                    address_entry.insert(0, supplier.address)
                    contact_entry.delete(0, tk.END)
                    contact_entry.insert(0, supplier.contact)
                    service_provided_entry.delete(0, tk.END)
                    service_provided_entry.insert(0, supplier.service_provided)
                    min_guests_entry.delete(0, tk.END)
                    min_guests_entry.insert(0, supplier.min_guests)
                    max_guests_entry.delete(0, tk.END)
                    max_guests_entry.insert(0, supplier.max_guests)
                else:
                    tk.messagebox.showinfo("Error", "Supplier with specified ID not found!")

            def save_changes():
                supplier_id = supplier_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()
                service_provided = service_provided_entry.get()
                min_guests = min_guests_entry.get()
                max_guests = max_guests_entry.get()
                
                try:
                    Supplier.update_supplier(supplier_id, name, address, contact, service_provided, min_guests, max_guests)
                    tk.messagebox.showinfo("Success", "Supplier details updated successfully!")
                    edit_supplier_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"Failed to update supplier details: {str(e)}")

            tk.Label(edit_supplier_window, text="Enter Supplier ID:", bg="#E0F2F1").pack(pady=5)
            supplier_id_entry = tk.Entry(edit_supplier_window)
            supplier_id_entry.pack(pady=5)
            search_button = tk.Button(edit_supplier_window, text="Search", command=search_supplier, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            search_button.pack(pady=5)

            tk.Label(edit_supplier_window, text="Name:", bg="#E0F2F1").pack(pady=5)
            name_entry = tk.Entry(edit_supplier_window)
            name_entry.pack(pady=5)

            tk.Label(edit_supplier_window, text="Address:", bg="#E0F2F1").pack(pady=5)
            address_entry = tk.Entry(edit_supplier_window)
            address_entry.pack(pady=5)

            tk.Label(edit_supplier_window, text="Contact:", bg="#E0F2F1").pack(pady=5)
            contact_entry = tk.Entry(edit_supplier_window)
            contact_entry.pack(pady=5)

            tk.Label(edit_supplier_window, text="Service Provided:", bg="#E0F2F1").pack(pady=5)
            service_provided_entry = tk.Entry(edit_supplier_window)
            service_provided_entry.pack(pady=5)

            tk.Label(edit_supplier_window, text="Min Guests:", bg="#E0F2F1").pack(pady=5)
            min_guests_entry = tk.Entry(edit_supplier_window)
            min_guests_entry.pack(pady=5)

            tk.Label(edit_supplier_window, text="Max Guests:", bg="#E0F2F1").pack(pady=5)
            max_guests_entry = tk.Entry(edit_supplier_window)
            max_guests_entry.pack(pady=5)

            save_button = tk.Button(edit_supplier_window, text="Save Changes", command=save_changes, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            save_button.pack(pady=10)

        def delete_supplier():  # Delete Supplier functionality
            # Create the Delete Supplier menu
            delete_supplier_window = tk.Toplevel()
            delete_supplier_window.title("Delete Supplier")
            delete_supplier_window.geometry("280x150")
            delete_supplier_window.configure(bg="#E0F2F1")

            # Function to delete supplier
            def delete_supplier():
                supplier_id = supplier_id_entry.get()
                try:
                    Supplier.delete_supplier(supplier_id)
                    tk.messagebox.showinfo("Success", "Supplier deleted successfully!")
                    delete_supplier_window.destroy()
                except ValueError:
                    tk.messagebox.showerror("Error", "Supplier with specified ID not found!")

            tk.Label(delete_supplier_window, text="Enter Supplier ID:", bg="#E0F2F1").pack(pady=5)
            supplier_id_entry = tk.Entry(delete_supplier_window)
            supplier_id_entry.pack(pady=5)
            delete_button = tk.Button(delete_supplier_window, text="Delete", command=delete_supplier, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            delete_button.pack(pady=5)

        def display_all_suppliers():  # Display All Suppliers functionality
            # Create the Display All Suppliers menu
            display_suppliers_window = tk.Toplevel()
            display_suppliers_window.title("Display All Suppliers")
            display_suppliers_window.geometry("1050x400")
            display_suppliers_window.configure(bg="#E0F2F1")

            # Retrieve all suppliers data
            suppliers = Supplier.get_all_suppliers()

            # Display supplier data
            for i, supplier in enumerate(suppliers):
                tk.Label(display_suppliers_window, text=f"Name: {supplier.name}").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                tk.Label(display_suppliers_window, text=f"Supplier ID: {supplier.supplier_id}").grid(row=i, column=1, padx=10, pady=5, sticky="w")
                tk.Label(display_suppliers_window, text=f"Address: {supplier.address}").grid(row=i, column=2, padx=10, pady=5, sticky="w")
                tk.Label(display_suppliers_window, text=f"Contact: {supplier.contact}").grid(row=i, column=3, padx=10, pady=5, sticky="w")
                tk.Label(display_suppliers_window, text=f"Service Provided: {supplier.service_provided}").grid(row=i, column=4, padx=10, pady=5, sticky="w")
                tk.Label(display_suppliers_window, text=f"Min Guests: {supplier.min_guests}").grid(row=i, column=5, padx=10, pady=5, sticky="w")
                tk.Label(display_suppliers_window, text=f"Max Guests: {supplier.max_guests}").grid(row=i, column=6, padx=10, pady=5, sticky="w")

        def display_supplier_with_id():  # Display Supplier with ID functionality
            # Create the Display Supplier with ID menu
            display_supplier_with_id_window = tk.Toplevel()
            display_supplier_with_id_window.title("Display Supplier with ID")
            display_supplier_with_id_window.geometry("1050x400")
            display_supplier_with_id_window.configure(bg="#E0F2F1")

            # Function to display supplier with ID
            def display_supplier():
                supplier_id = supplier_id_entry.get()
                supplier = Supplier.display_supplier_with_id(supplier_id)  # Use Supplier class instead of supplier object
                if supplier:
                    # Display supplier details in table-like format
                    tree = ttk.Treeview(display_supplier_with_id_window)
                    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
                    tree.heading("#0", text="Name")
                    tree.heading("1", text="Supplier ID", anchor=tk.CENTER)
                    tree.heading("2", text="Address", anchor=tk.CENTER)
                    tree.heading("3", text="Contact", anchor=tk.CENTER)
                    tree.heading("4", text="Service Provided", anchor=tk.CENTER)
                    tree.heading("5", text="Min Guests", anchor=tk.CENTER)
                    tree.heading("6", text="Max Guests", anchor=tk.CENTER)

                    tree.column("#0", width=150)
                    tree.column("1", width=100)
                    tree.column("2", width=200)
                    tree.column("3", width=150)
                    tree.column("4", width=150)
                    tree.column("5", width=100)
                    tree.column("6", width=100)

                    tree.insert("", "end", text=supplier.name, values=(supplier.supplier_id, supplier.address, supplier.contact, supplier.service_provided, supplier.min_guests, supplier.max_guests))
                    tree.pack(expand=True, fill=tk.BOTH)

                else:
                    tk.messagebox.showinfo("Error", "Supplier with specified ID not found!")

            tk.Label(display_supplier_with_id_window, text="Enter Supplier ID:", bg="#E0F2F1").pack(pady=5)
            supplier_id_entry = tk.Entry(display_supplier_with_id_window)
            supplier_id_entry.pack(pady=5)
            display_button = tk.Button(display_supplier_with_id_window, text="Display", command=display_supplier, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            display_button.pack(pady=5)




        def add_event():  # Add Event functionality
            # Create the Event Add menu
            add_event_window = tk.Toplevel()
            add_event_window.title("Add Event")
            add_event_window.geometry("280x700")
            add_event_window.configure(bg="#E0F2F1")

            # Function to save event data
            def save_event():
                # Get data from entry fields
                event_id = event_id_entry.get()
                event_type = event_type_entry.get()
                theme = theme_entry.get()
                date = date_entry.get()
                time = time_entry.get()
                duration = duration_entry.get()
                venue_address = venue_address_entry.get()
                client_id = client_id_entry.get()
                guest_list = guest_list_entry.get()
                suppliers_company = suppliers_company_entry.get()
                invoice = invoice_entry.get()

                # Validate fields
                if not (event_id and event_type and theme and date and time and duration and venue_address and client_id and guest_list and suppliers_company and invoice):
                    tk.messagebox.showerror("Error", "All fields are required!")
                    return

                # Validate event ID (assuming it should be numeric)
                if not event_id.isdigit():
                    tk.messagebox.showerror("Error", "Event ID should contain only digits!")
                    return
                
                # Call add_event method to save data
                Event.add_event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice)
                tk.messagebox.showinfo("Success", "Event added successfully!")
                add_event_window.destroy()  # Close the Add Event window

            # Labels and Entry fields for Event details
            tk.Label(add_event_window, text="Event ID:", bg="#E0F2F1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
            event_id_entry = tk.Entry(add_event_window)
            event_id_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Event Type:", bg="#E0F2F1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
            event_type_entry = tk.Entry(add_event_window)
            event_type_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Theme:", bg="#E0F2F1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
            theme_entry = tk.Entry(add_event_window)
            theme_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Date:", bg="#E0F2F1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
            date_entry = tk.Entry(add_event_window)
            date_entry.grid(row=3, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Time:", bg="#E0F2F1").grid(row=4, column=0, padx=10, pady=5, sticky="e")
            time_entry = tk.Entry(add_event_window)
            time_entry.grid(row=4, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Duration:", bg="#E0F2F1").grid(row=5, column=0, padx=10, pady=5, sticky="e")
            duration_entry = tk.Entry(add_event_window)
            duration_entry.grid(row=5, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Venue Address:", bg="#E0F2F1").grid(row=6, column=0, padx=10, pady=5, sticky="e")
            venue_address_entry = tk.Entry(add_event_window)
            venue_address_entry.grid(row=6, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Client ID:", bg="#E0F2F1").grid(row=7, column=0, padx=10, pady=5, sticky="e")
            client_id_entry = tk.Entry(add_event_window)
            client_id_entry.grid(row=7, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Guest List:", bg="#E0F2F1").grid(row=8, column=0, padx=10, pady=5, sticky="e")
            guest_list_entry = tk.Entry(add_event_window)
            guest_list_entry.grid(row=8, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Suppliers Company:", bg="#E0F2F1").grid(row=9, column=0, padx=10, pady=5, sticky="e")
            suppliers_company_entry = tk.Entry(add_event_window)
            suppliers_company_entry.grid(row=9, column=1, padx=10, pady=5)

            tk.Label(add_event_window, text="Invoice:", bg="#E0F2F1").grid(row=10, column=0, padx=10, pady=5, sticky="e")
            invoice_entry = tk.Entry(add_event_window)
            invoice_entry.grid(row=10, column=1, padx=10, pady=5)

            # Save button
            save_button = tk.Button(add_event_window, text="Save", bg="#FFAB91", fg="white", font=("Arial", 10, "bold"), command=save_event)
            save_button.grid(row=11, column=0, columnspan=2, pady=10)

        def edit_event():
            edit_event_window = tk.Toplevel()
            edit_event_window.title("Edit Event")
            edit_event_window.geometry("400x500")
            edit_event_window.configure(bg="#E0F2F1")

            def search_event():
                event_id = event_id_entry.get()
                event = Event.display_event_with_id(event_id)
                if event:
                    event_type_entry.delete(0, tk.END)
                    event_type_entry.insert(0, event.event_type)
                    theme_entry.delete(0, tk.END)
                    theme_entry.insert(0, event.theme)
                    date_entry.delete(0, tk.END)
                    date_entry.insert(0, event.date)
                    time_entry.delete(0, tk.END)
                    time_entry.insert(0, event.time)
                    duration_entry.delete(0, tk.END)
                    duration_entry.insert(0, event.duration)
                    venue_address_entry.delete(0, tk.END)
                    venue_address_entry.insert(0, event.venue_address)
                    client_id_entry.delete(0, tk.END)
                    client_id_entry.insert(0, event.client_id)
                    guest_list_entry.delete(0, tk.END)
                    guest_list_entry.insert(0, event.guest_list)
                    suppliers_company_entry.delete(0, tk.END)
                    suppliers_company_entry.insert(0, event.suppliers_company)
                    invoice_entry.delete(0, tk.END)
                    invoice_entry.insert(0, event.invoice)
                else:
                    tk.messagebox.showinfo("Error", "Event with specified ID not found!")

            def save_changes():
                event_id = event_id_entry.get()
                event_type = event_type_entry.get()
                theme = theme_entry.get()
                date = date_entry.get()
                time = time_entry.get()
                duration = duration_entry.get()
                venue_address = venue_address_entry.get()
                client_id = client_id_entry.get()
                guest_list = guest_list_entry.get()
                suppliers_company = suppliers_company_entry.get()
                invoice = invoice_entry.get()
                
                try:
                    Event.update_event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice)
                    tk.messagebox.showinfo("Success", "Event details updated successfully!")
                    edit_event_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"Failed to update event details: {str(e)}")

            tk.Label(edit_event_window, text="Enter Event ID:", bg="#E0F2F1").pack(pady=5)
            event_id_entry = tk.Entry(edit_event_window)
            event_id_entry.pack(pady=5)
            search_button = tk.Button(edit_event_window, text="Search", command=search_event, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            search_button.pack(pady=5)

            tk.Label(edit_event_window, text="Event Type:", bg="#E0F2F1").pack(pady=5)
            event_type_entry = tk.Entry(edit_event_window)
            event_type_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Theme:", bg="#E0F2F1").pack(pady=5)
            theme_entry = tk.Entry(edit_event_window)
            theme_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Date:", bg="#E0F2F1").pack(pady=5)
            date_entry = tk.Entry(edit_event_window)
            date_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Time:", bg="#E0F2F1").pack(pady=5)
            time_entry = tk.Entry(edit_event_window)
            time_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Duration:", bg="#E0F2F1").pack(pady=5)
            duration_entry = tk.Entry(edit_event_window)
            duration_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Venue Address:", bg="#E0F2F1").pack(pady=5)
            venue_address_entry = tk.Entry(edit_event_window)
            venue_address_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Client ID:", bg="#E0F2F1").pack(pady=5)
            client_id_entry = tk.Entry(edit_event_window)
            client_id_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Guest List:", bg="#E0F2F1").pack(pady=5)
            guest_list_entry = tk.Entry(edit_event_window)
            guest_list_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Suppliers Company:", bg="#E0F2F1").pack(pady=5)
            suppliers_company_entry = tk.Entry(edit_event_window)
            suppliers_company_entry.pack(pady=5)

            tk.Label(edit_event_window, text="Invoice:", bg="#E0F2F1").pack(pady=5)
            invoice_entry = tk.Entry(edit_event_window)
            invoice_entry.pack(pady=5)

            save_button = tk.Button(edit_event_window, text="Save Changes", command=save_changes, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            save_button.pack(pady=10)

        def delete_event():  # Delete Event functionality
            # Create the Delete Event menu
            delete_event_window = tk.Toplevel()
            delete_event_window.title("Delete Event")
            delete_event_window.geometry("280x150")
            delete_event_window.configure(bg="#E0F2F1")

            # Function to delete event
            def delete_event():
                event_id = event_id_entry.get()
                try:
                    Event.delete_event(event_id)
                    tk.messagebox.showinfo("Success", "Event deleted successfully!")
                    delete_event_window.destroy()
                except ValueError:
                    tk.messagebox.showerror("Error", "Event with specified ID not found!")

            tk.Label(delete_event_window, text="Enter Event ID:", bg="#E0F2F1").pack(pady=5)
            event_id_entry = tk.Entry(delete_event_window)
            event_id_entry.pack(pady=5)
            delete_button = tk.Button(delete_event_window, text="Delete", command=delete_event, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            delete_button.pack(pady=5)

        def display_all_events():  # Display All Events functionality
            # Create the Display All Events menu
            display_events_window = tk.Toplevel()
            display_events_window.title("Display All Events")
            display_events_window.geometry("1050x400")
            display_events_window.configure(bg="#E0F2F1")

            # Retrieve all events data
            events = Event.get_all_events()

            # Display event data
            for i, event in enumerate(events):
                tk.Label(display_events_window, text=f"Event Type: {event.event_type}").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Event ID: {event.event_id}").grid(row=i, column=1, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Theme: {event.theme}").grid(row=i, column=2, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Date: {event.date}").grid(row=i, column=3, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Time: {event.time}").grid(row=i, column=4, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Duration: {event.duration}").grid(row=i, column=5, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Venue Address: {event.venue_address}").grid(row=i, column=6, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Client ID: {event.client_id}").grid(row=i, column=7, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Guest List: {event.guest_list}").grid(row=i, column=8, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Suppliers Company: {event.suppliers_company}").grid(row=i, column=9, padx=10, pady=5, sticky="w")
                tk.Label(display_events_window, text=f"Invoice: {event.invoice}").grid(row=i, column=10, padx=10, pady=5, sticky="w")

        def display_event_with_id():  # Display Event with ID functionality
            # Create the Display Event with ID menu
            display_event_with_id_window = tk.Toplevel()
            display_event_with_id_window.title("Display Event with ID")
            display_event_with_id_window.geometry("1050x400")
            display_event_with_id_window.configure(bg="#E0F2F1")

            # Function to display event with ID
            def display_event():
                event_id = event_id_entry.get()
                event = Event.display_event_with_id(event_id)
                if event:
                    # Display event details in table-like format
                    tree = ttk.Treeview(display_event_with_id_window)
                    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
                    tree.heading("#0", text="Event Type")
                    tree.heading("1", text="Event ID", anchor=tk.CENTER)
                    tree.heading("2", text="Theme", anchor=tk.CENTER)
                    tree.heading("3", text="Date", anchor=tk.CENTER)
                    tree.heading("4", text="Time", anchor=tk.CENTER)
                    tree.heading("5", text="Duration", anchor=tk.CENTER)
                    tree.heading("6", text="Venue Address", anchor=tk.CENTER)
                    tree.heading("7", text="Client ID", anchor=tk.CENTER)
                    tree.heading("8", text="Guest List", anchor=tk.CENTER)
                    tree.heading("9", text="Suppliers Company", anchor=tk.CENTER)
                    tree.heading("10", text="Invoice", anchor=tk.CENTER)

                    tree.column("#0", width=100)
                    tree.column("1", width=100)
                    tree.column("2", width=100)
                    tree.column("3", width=100)
                    tree.column("4", width=100)
                    tree.column("5", width=100)
                    tree.column("6", width=100)
                    tree.column("7", width=100)
                    tree.column("8", width=100)
                    tree.column("9", width=100)
                    tree.column("10", width=100)

                    tree.insert("", "end", text=event.event_type, values=(event.event_id, event.theme, event.date, event.time, event.duration, event.venue_address, event.client_id, event.guest_list, event.suppliers_company, event.invoice))
                    tree.pack(expand=True, fill=tk.BOTH)

                else:
                    tk.messagebox.showinfo("Error", "Event with specified ID not found!")

            tk.Label(display_event_with_id_window, text="Enter Event ID:", bg="#E0F2F1").pack(pady=5)
            event_id_entry = tk.Entry(display_event_with_id_window)
            event_id_entry.pack(pady=5)
            display_button = tk.Button(display_event_with_id_window, text="Display", command=display_event, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            display_button.pack(pady=5)




        def add_guest():  # Add Guest functionality
            # Create the Guest Add menu
            add_guest_window = tk.Toplevel()
            add_guest_window.title("Add Guest")
            add_guest_window.geometry("280x350")
            add_guest_window.configure(bg="#E0F2F1")

            # Function to save guest data
            def save_guest():
                # Get data from entry fields
                guest_id = guest_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()

                # Validate fields
                if not (guest_id and name and address and contact):
                    tk.messagebox.showerror("Error", "All fields are required!")
                    return

                # Validate guest ID (assuming it should be numeric)
                if not guest_id.isdigit():
                    tk.messagebox.showerror("Error", "Guest ID should contain only digits!")
                    return
                
                # Call add_guest method from Guest class to save data
                Guest.add_guest(guest_id, name, address, contact)
                tk.messagebox.showinfo("Success", "Guest added successfully!")
                add_guest_window.destroy()  # Close the Add Guest window

            # Labels and Entry fields for Guest details
            tk.Label(add_guest_window, text="Guest ID:", bg="#E0F2F1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
            guest_id_entry = tk.Entry(add_guest_window)
            guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(add_guest_window, text="Name:", bg="#E0F2F1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
            name_entry = tk.Entry(add_guest_window)
            name_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(add_guest_window, text="Address:", bg="#E0F2F1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
            address_entry = tk.Entry(add_guest_window)
            address_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(add_guest_window, text="Contact:", bg="#E0F2F1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
            contact_entry = tk.Entry(add_guest_window)
            contact_entry.grid(row=3, column=1, padx=10, pady=5)

            # Save button
            save_button = tk.Button(add_guest_window, text="Save", bg="#FFAB91", fg="white", font=("Arial", 10, "bold"), command=save_guest)
            save_button.grid(row=4, column=0, columnspan=2, pady=10)

        def edit_guest():
            edit_guest_window = tk.Toplevel()
            edit_guest_window.title("Edit Guest")
            edit_guest_window.geometry("280x700")
            edit_guest_window.configure(bg="#E0F2F1")

            def search_guest():
                guest_id = guest_id_entry.get()
                guest = Guest.display_guest_with_id(guest_id)
                if guest:
                    name_entry.delete(0, tk.END)
                    name_entry.insert(0, guest.name)
                    address_entry.delete(0, tk.END)
                    address_entry.insert(0, guest.address)
                    contact_entry.delete(0, tk.END)
                    contact_entry.insert(0, guest.contact)
                else:
                    tk.messagebox.showinfo("Error", "Guest with specified ID not found!")

            def save_changes():
                guest_id = guest_id_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                contact = contact_entry.get()
                
                try:
                    Guest.update_guest(guest_id, name, address, contact)
                    tk.messagebox.showinfo("Success", "Guest details updated successfully!")
                    edit_guest_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"Failed to update guest details: {str(e)}")

            tk.Label(edit_guest_window, text="Enter Guest ID:", bg="#E0F2F1").pack(pady=5)
            guest_id_entry = tk.Entry(edit_guest_window)
            guest_id_entry.pack(pady=5)
            search_button = tk.Button(edit_guest_window, text="Search", command=search_guest, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            search_button.pack(pady=5)

            tk.Label(edit_guest_window, text="Name:", bg="#E0F2F1").pack(pady=5)
            name_entry = tk.Entry(edit_guest_window)
            name_entry.pack(pady=5)

            tk.Label(edit_guest_window, text="Address:", bg="#E0F2F1").pack(pady=5)
            address_entry = tk.Entry(edit_guest_window)
            address_entry.pack(pady=5)

            tk.Label(edit_guest_window, text="Contact:", bg="#E0F2F1").pack(pady=5)
            contact_entry = tk.Entry(edit_guest_window)
            contact_entry.pack(pady=5)

            save_button = tk.Button(edit_guest_window, text="Save Changes", command=save_changes, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            save_button.pack(pady=10)

        def delete_guest():  # Delete Guest functionality
            # Create the Delete Guest menu
            delete_guest_window = tk.Toplevel()
            delete_guest_window.title("Delete Guest")
            delete_guest_window.geometry("280x150")
            delete_guest_window.configure(bg="#E0F2F1")

            # Function to delete guest
            def delete_guest():
                guest_id = guest_id_entry.get()
                try:
                    Guest.delete_guest(guest_id)
                    tk.messagebox.showinfo("Success", "Guest deleted successfully!")
                    delete_guest_window.destroy()
                except ValueError:
                    tk.messagebox.showerror("Error", "Guest with specified ID not found!")

            tk.Label(delete_guest_window, text="Enter Guest ID:", bg="#E0F2F1").pack(pady=5)
            guest_id_entry = tk.Entry(delete_guest_window)
            guest_id_entry.pack(pady=5)
            delete_button = tk.Button(delete_guest_window, text="Delete", command=delete_guest, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            delete_button.pack(pady=5)

        def display_all_guests():  # Display All Guests functionality
            # Create the Display All Guests menu
            display_guests_window = tk.Toplevel()
            display_guests_window.title("Display All Guests")
            display_guests_window.geometry("1050x400")
            display_guests_window.configure(bg="#E0F2F1")

            # Retrieve all guests data
            guests = Guest.get_all_guests()

            # Display guest data
            for i, guest in enumerate(guests):
                tk.Label(display_guests_window, text=f"Name: {guest.name}").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                tk.Label(display_guests_window, text=f"Guest ID: {guest.guest_id}").grid(row=i, column=1, padx=10, pady=5, sticky="w")
                tk.Label(display_guests_window, text=f"Address: {guest.address}").grid(row=i, column=2, padx=10, pady=5, sticky="w")
                tk.Label(display_guests_window, text=f"Contact: {guest.contact}").grid(row=i, column=3, padx=10, pady=5, sticky="w")

        def display_guest_with_id():  # Display Guest with ID functionality
            # Create the Display Guest with ID menu
            display_guest_with_id_window = tk.Toplevel()
            display_guest_with_id_window.title("Display Guest with ID")
            display_guest_with_id_window.geometry("1050x400")
            display_guest_with_id_window.configure(bg="#E0F2F1")

            # Function to display guest with ID
            def display_guest():
                guest_id = guest_id_entry.get()
                guest = Guest.display_guest_with_id(guest_id)  # Use Guest class instead of guest object
                if guest:
                    # Display guest details in table-like format
                    tree = ttk.Treeview(display_guest_with_id_window)
                    tree["columns"] = ("1", "2", "3", "4")
                    tree.heading("#0", text="Name")
                    tree.heading("1", text="Guest ID", anchor=tk.CENTER)
                    tree.heading("2", text="Address", anchor=tk.CENTER)
                    tree.heading("3", text="Contact", anchor=tk.CENTER)

                    tree.column("#0", width=150)
                    tree.column("1", width=100)
                    tree.column("2", width=200)
                    tree.column("3", width=150)

                    tree.insert("", "end", text=guest.name, values=(guest.guest_id, guest.address, guest.contact))
                    tree.pack(expand=True, fill=tk.BOTH)

                else:
                    tk.messagebox.showinfo("Error", "Guest with specified ID not found!")

            tk.Label(display_guest_with_id_window, text="Enter Guest ID:", bg="#E0F2F1").pack(pady=5)
            guest_id_entry = tk.Entry(display_guest_with_id_window)
            guest_id_entry.pack(pady=5)
            display_button = tk.Button(display_guest_with_id_window, text="Display", command=display_guest, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"))
            display_button.pack(pady=5)

        def exit_submenu():
            submenu_window.destroy()

        # Main menu buttons
        button_width = 15  # Set width for all buttons
        button_height = 2  # Set height for all buttons
        button_font = ("Arial", 10, "bold")  # Set font for all buttons
        # Add button
        add_button = tk.Button(submenu_window, text="Add", bg="#FFAB91", fg="white", font=button_font, width=button_width, height=button_height, command=lambda: add_data(menu_title))
        add_button.pack(pady=5, padx=10)

        # Edit button
        edit_button = tk.Button(submenu_window, text="Edit", bg="#FFAB91", fg="white", font=button_font, width=button_width, height=button_height, command=lambda: edit_data(menu_title))
        edit_button.pack(pady=5, padx=10)

        # Delete button
        delete_button = tk.Button(submenu_window, text="Delete", bg="#FFAB91", fg="white", font=button_font, width=button_width, height=button_height, command=lambda: delete_data(menu_title))
        delete_button.pack(pady=5, padx=10)

        # Display All button
        display_button = tk.Button(submenu_window, text="Display All", bg="#FFAB91", fg="white", font=button_font, width=button_width, height=button_height, command=lambda: display_all_data(menu_title))
        display_button.pack(pady=5, padx=10)

        # Display with ID button
        display_with_id_button = tk.Button(submenu_window, text="Display with ID", bg="#FFAB91", fg="white", font=button_font, width=button_width, height=button_height, command=lambda: display_data_with_id(menu_title))
        display_with_id_button.pack(pady=5, padx=10)

        # Exit button
        exit_button = tk.Button(submenu_window, text="Exit", command=exit_submenu, bg="#FFAB91", fg="white", font=("Arial", 10, "bold"), width=button_width)
        exit_button.pack(side="bottom", pady=5, padx=10)

        submenu_window.mainloop()

    def revenue_menu(self):
            try:
                with open("revenue.pkl", "rb") as f:
                    revenue_data = pickle.load(f)
                    revenue_window = tk.Toplevel()
                    revenue_window.title("Revenue Management")
                    revenue_window.geometry("600x400")
                    revenue_window.configure(bg="#E0F2F1")

                    title_label = tk.Label(revenue_window, text="Revenue Information", font=("Arial", 16, "bold"), bg="#E0F2F1")
                    title_label.pack(pady=10)

                    tree = ttk.Treeview(revenue_window, columns=("Key", "Value"), show="headings", height=10)
                    tree.heading("Key", text="Key")
                    tree.heading("Value", text="Value")
                    tree.pack(pady=10)

                    for key, value in revenue_data.items():
                        tree.insert("", "end", values=(key, value))

                    close_button = tk.Button(revenue_window, text="Close", command=revenue_window.destroy, bg="#FFAB91", fg="white", font=("Arial", 12, "bold"))
                    close_button.pack(pady=10)

            except FileNotFoundError:
                tk.messagebox.showerror("Error", "Revenue data not found!")


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()