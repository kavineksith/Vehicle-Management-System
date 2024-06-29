import sqlite3
import re
import sys

class DriversApp:
    def __init__(self):
        self.db_connection = sqlite3.connect("vms_db.db")
        
    def insert_driver(self, driver_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''INSERT INTO Drivers (DriverID, DriverName, DriverGender, DriverEmail, DriverTelNo)
                              VALUES (?, ?, ?, ?, ?)''', driver_data)
            self.db_connection.commit()
            print("Driver data inserted successfully!")
        except Exception as e:
            print(f"Failed to insert driver data: {str(e)}")

    def update_driver(self, driver_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''UPDATE Drivers SET DriverName=?, DriverGender=?, DriverEmail=?, DriverTelNo=?, 
                              WHERE DriverID=?''', driver_data[1:] + [driver_data[0]])
            self.db_connection.commit()
            print("Driver data updated successfully!")
        except Exception as e:
            print(f"Failed to update driver data: {str(e)}")

    def delete_driver(self, driver_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''DELETE FROM Drivers WHERE DriverID=?''', (driver_id,))
            self.db_connection.commit()
            print("Driver data deleted successfully!")
        except Exception as e:
            print(f"Failed to delete driver data: {str(e)}")

    def search_driver(self, driver_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM Drivers WHERE DriverID=?''', (driver_id,))
            driver_data = cursor.fetchone()
            if driver_data:
                print("Driver data found:")
                print(driver_data)
            else:
                print("Driver not found!")
        except Exception as e:
            print(f"Failed to search for delete: {str(e)}")

    def filter_drivers(self, criteria):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(f'''SELECT * FROM Drivers WHERE {criteria}''')
            filtered_data = cursor.fetchall()
            if filtered_data:
                print("Filtered drivers:")
                for driver in filtered_data:
                    print(driver)
            else:
                print("No drivers match the filter criteria!")
        except Exception as e:
            print(f"Failed to filter drivers: {str(e)}")

    def view_drivers(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM Drivers''')
            all_drivers = cursor.fetchall()
            if all_drivers:
                print("All drivers:")
                for driver in all_drivers:
                    print(driver)
            else:
                print("No drivers found in the database!")
        except Exception as e:
            print(f"Failed to fetch drivers: {str(e)}")

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
                print("1. Insert a new driver")
                print("2. Update driver details")
                print("3. Delete a driver")
                print("4. Search for a driver")
                print("5. Filter drivers")
                print("6. View all drivers")
                print("7. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    driver_data = self.get_driver_data_from_input()
                    self.insert_driver(driver_data)
                elif choice == 2:
                    driver_id = input("Enter Driver ID to update: ")
                    driver_data = self.get_driver_data_from_input()
                    self.update_driver(driver_data)
                elif choice == 3:
                    driver_id = input("Enter Driver ID to delete: ")
                    self.delete_driver(driver_id)
                elif choice == 4:
                    driver_id = input("Enter Driver ID to search: ")
                    self.search_driver(driver_id)
                elif choice == 5:
                    criteria = input("Enter filter criteria: ")
                    self.filter_drivers(criteria)
                elif choice == 6:
                    self.view_drivers()
                elif choice == 7:
                    self.close_connection()
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice! Please enter a number from 1 to 7.")
            except ValueError:
                print("Invalid input. Please enter enter a number from 1 to 7.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_driver_data_from_input(self):
        driver_id = self.get_valid_id()
        driver_name = self.get_valid_name()
        driver_gender = self.get_valid_gender()
        driver_email = self.get_valid_email()
        driver_telno = self.get_valid_telno()
        return (driver_id, driver_name, driver_gender, driver_email, driver_telno)

    def get_valid_id(self):
        while True:
            try:
                driver_id = input("Enter Driver ID: ")
                if re.match(r'^[A-Za-z0-9_-]*$', driver_id):
                    return driver_id
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
                driver_name = input("Enter Driver Name: ")
                if re.match(r'^[A-Za-z\s]+$', driver_name):
                    return driver_name
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
                gender = input("Enter Driver Gender (male/female/other): ").lower()
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
                email = input("Enter Driver Email: ")
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
                telno = input("Enter Driver Tel No: ")
                if re.match(r'^\d{10}$', telno):
                    return int(telno)
                else:
                    print("Invalid phone number format! Please enter a 10-digit number.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

