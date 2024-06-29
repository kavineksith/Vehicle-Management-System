import sqlite3
import re
import sys

class CustomersApp:
    def __init__(self):
        self.db_connection = sqlite3.connect("vms_db.db")
        
    def insert_customer(self, customer_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''INSERT INTO Customers (CustomerID, CustomerName, CustomerGender, CustomerEmail, CustomerTelNo, CustomerCategory)
                              VALUES (?, ?, ?, ?, ?, ?)''', customer_data)
            self.db_connection.commit()
            print("Customer data inserted successfully!")
        except Exception as e:
            print(f"Failed to insert customer data: {str(e)}")

    def update_customer(self, customer_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''UPDATE Customers SET CustomerName=?, CustomerGender=?, CustomerEmail=?, CustomerTelNo=?, CustomerCategory=? 
                              WHERE CustomerID=?''', customer_data[1:] + [customer_data[0]])
            self.db_connection.commit()
            print("Customer data updated successfully!")
        except Exception as e:
            print(f"Failed to update customer data: {str(e)}")

    def delete_customer(self, customer_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''DELETE FROM Customers WHERE CustomerID=?''', (customer_id,))
            self.db_connection.commit()
            print("Customer data deleted successfully!")
        except Exception as e:
            print(f"Failed to delete customer data: {str(e)}")

    def search_customer(self, customer_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM Customers WHERE CustomerID=?''', (customer_id,))
            customer_data = cursor.fetchone()
            if customer_data:
                print("Customer data found:")
                print(customer_data)
            else:
                print("Customer not found!")
        except Exception as e:
            print(f"Failed to search for customer: {str(e)}")

    def filter_customers(self, criteria):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(f'''SELECT * FROM Customers WHERE {criteria}''')
            filtered_data = cursor.fetchall()
            if filtered_data:
                print("Filtered customers:")
                for customer in filtered_data:
                    print(customer)
            else:
                print("No customers match the filter criteria!")
        except Exception as e:
            print(f"Failed to filter customers: {str(e)}")

    def view_customers(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM Customers''')
            all_customers = cursor.fetchall()
            if all_customers:
                print("All customers:")
                for customer in all_customers:
                    print(customer)
            else:
                print("No customers found in the database!")
        except Exception as e:
            print(f"Failed to fetch customers: {str(e)}")

    def close_connection(self):
        try:
            self.db_connection.close()
            print("Database connection closed successfully!")
        except Exception as e:
            print(f"Failed to close the database connection: {str(e)}")

    def interact(self):
        while True:
            try:
                print("\nWhat would you like to do?")
                print("1. Insert a new customer")
                print("2. Update customer details")
                print("3. Delete a customer")
                print("4. Search for a customer")
                print("5. Filter customers")
                print("6. View all customers")
                print("7. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    customer_data = self.get_customer_data_from_input()
                    self.insert_customer(customer_data)
                elif choice == '2':
                    customer_id = input("Enter Customer ID to update: ")
                    customer_data = self.get_customer_data_from_input()
                    self.update_customer(customer_data)
                elif choice == '3':
                    customer_id = input("Enter Customer ID to delete: ")
                    self.delete_customer(customer_id)
                elif choice == '4':
                    customer_id = input("Enter Customer ID to search: ")
                    self.search_customer(customer_id)
                elif choice == '5':
                    criteria = input("Enter filter criteria: ")
                    self.filter_customers(criteria)
                elif choice == '6':
                    self.view_customers()
                elif choice == '7':
                    self.close_connection()
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice! Please enter a number from 1 to 7.")
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 7.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_customer_data_from_input(self):
        customer_id = self.get_valid_id()
        customer_name = self.get_valid_name()
        customer_gender = self.get_valid_gender()
        customer_email = self.get_valid_email()
        customer_telno = self.get_valid_telno()
        customer_category = self.get_valid_category()
        return (customer_id, customer_name, customer_gender, customer_email, customer_telno, customer_category)

    def get_valid_id(self):
        while True:
            try:
                customer_id = input("Enter Customer ID: ")
                if re.match(r'^[A-Za-z0-9_-]*$', customer_id):
                    return customer_id
                else:
                    print("Invalid ID format! Please enter a valid ID.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_name(self):
        while True:
            try:
                customer_name = input("Enter Customer Name: ")
                if re.match(r'^[A-Za-z\s]+$', customer_name):
                    return customer_name
                else:
                    print("Invalid name format! Please enter a valid name.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_gender(self):
        while True:
            try:
                gender = input("Enter Customer Gender (male/female/other): ").lower()
                if gender in ('male', 'female', 'other'):
                    return gender
                else:
                    print("Invalid input! Please enter 'male', 'female', or 'other'.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_email(self):
        while True:
            try:
                email = input("Enter Customer Email: ")
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    return email
                else:
                    print("Invalid email format! Please enter a valid email address.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_telno(self):
        while True:
            try:
                telno = input("Enter Customer Tel No: ")
                if re.match(r'^\d{10}$', telno):
                    return int(telno)
                else:
                    print("Invalid phone number format! Please enter a 10-digit number.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_category(self):
        while True:
            try:
                category = input("Enter Customer Category (super/normal): ").lower()
                if category in ('super', 'normal'):
                    return category
                else:
                    print("Invalid input! Please enter 'super' or 'normal'.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

