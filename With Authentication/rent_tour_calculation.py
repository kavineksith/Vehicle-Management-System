import re
import sqlite3
import sys
from datetime import datetime

class RentCalculationApp:
    def __init__(self):
        self.con = sqlite3.connect("vms_db.db")
 
    def start(self):
        while True:
            try:
                print("\nWhat would you like to do?")
                print("1. Search Rent")
                print("2. Search Customer")
                print("3. Search Vehicle")
                print("4. Search Driver")
                print("5. View Customers")
                print("6. View Vehicles")
                print("7. View Drivers")
                print("8. View Rent Calculations")
                print("9. Insert Data")
                print("10. Update Data")
                print("11. Delete Data")
                print("12. Process Data")
                print("13. Filter Data")
                print("14. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.search_rent()
                elif choice == "2":
                    self.search_customer()
                elif choice == "3":
                    self.search_vehicle()
                elif choice == "4":
                    self.search_driver()
                elif choice == "5":
                    self.view_customers()
                elif choice == "6":
                    self.view_vehicles()
                elif choice == "7":
                    self.view_drivers()
                elif choice == "8":
                    self.view_rent_calculations()
                elif choice == "9":
                    self.insert_data()
                elif choice == "10":
                    self.update_data()
                elif choice == "11":
                    self.delete_data()
                elif choice == "12":
                    self.process_data()
                elif choice == "13":
                    self.filter_data()
                elif choice == "14":
                    print("Exiting the application...")
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

    def search_customer(self):
        try:
            search_id = input("Enter Customer ID to search: ")
            search_query = "SELECT * FROM Customers WHERE CustomerID = ?"
            cmd_search = self.con.cursor()
            cmd_search.execute(search_query, (search_id,))
            result = cmd_search.fetchone()
            if result:
                print("Customer Email:", result[3])
            else:
                print("No data found.")
        except Exception as ex:
            print(f"Data previewed unsuccessfully. Please try again...! {ex}")

    def search_vehicle(self):
        try:
            search_id = input("Enter Vehicle ID to search: ")
            search_query = "SELECT * FROM Vehicles WHERE VehicleID = ?"
            cmd_search = self.con.cursor()
            cmd_search.execute(search_query, (search_id,))
            result = cmd_search.fetchone()
            if result:
                print("Vehicle No:", result[1])
                print("Vehicle Traffies:", result[6])
                print("Vehicle Value:", result[7])
            else:
                print("No data found.")
        except Exception as ex:
            print(f"Data previewed unsuccessfully. Please try again...! {ex}")

    def search_driver(self):
        try:
            search_id = input("Enter Driver ID to search: ")
            search_query = "SELECT * FROM Drivers WHERE DriverID = ?"
            cmd_search = self.con.cursor()
            cmd_search.execute(search_query, (search_id,))
            result = cmd_search.fetchone()
            if result:
                print("Driver Email:", result[3])
            else:
                print("No data found.")
        except Exception as ex:
            print(f"Data previewed unsuccessfully. Please try again...! {ex}")

    def view_customers(self):
        try:
            command = "SELECT * FROM Customers"
            cursor = self.con.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            self.print_data("Customers", data)
        except Exception as ex:
            print(f"Error viewing customers: {ex}")

    def view_vehicles(self):
        try:
            command = "SELECT * FROM Vehicles"
            cursor = self.con.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            self.print_data("Vehicles", data)
        except Exception as ex:
            print(f"Error viewing vehicles: {ex}")

    def view_drivers(self):
        try:
            command = "SELECT * FROM Drivers"
            cursor = self.con.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            self.print_data("Drivers", data)
        except Exception as ex:
            print(f"Error viewing drivers: {ex}")

    def view_rent_calculations(self):
        try:
            command = "SELECT * FROM RentCalculations"
            cursor = self.con.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            self.print_data("Rent Calculations", data)
        except Exception as ex:
            print(f"Error viewing rent calculations: {ex}")

    def insert_data(self):
        try:
            customer_email = self.get_valid_customer_email()
            rent_date = self.get_valid_date("Rent Date")
            vehicle_no = self.get_valid_vehicle_no()
            vehicle_traffies = self.get_valid_float("Vehicle Traffies")
            vehicle_value = self.get_valid_float("Vehicle Value")
            driver_condition = self.get_valid_driver_condition()
            driver_email = self.get_valid_driver_email()
            driver_cost = self.get_valid_float("Driver Cost")
            return_date = self.get_valid_date("Return Date")

            total_days = (datetime.strptime(return_date, "%Y-%m-%d") - datetime.strptime(rent_date, "%Y-%m-%d")).days
            rent_total = ((vehicle_traffies * 10) + vehicle_value + driver_cost) * total_days

            insert_query = "INSERT INTO RentCalculations (CustomerEmail, RentDate, VehicleNo, VehicleTraffies, VehicleValue, DriverCondition, DriverEmail, DriverCost, ReturnDate, TotalDays, RentTotal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cmd_insert = self.con.cursor()
            cmd_insert.execute(insert_query, (customer_email, rent_date, vehicle_no, vehicle_traffies, vehicle_value, driver_condition, driver_email, driver_cost, return_date, total_days, rent_total))
            self.con.commit()

            print("Data stored successfully...!")

        except Exception as ex:
            print(f"Error storing data: {ex}")

    def update_data(self):
        try:
            search_id = input("Enter Rent ID to update: ")

            customer_email = self.get_valid_customer_email()
            rent_date = self.get_valid_date("Rent Date")
            vehicle_no = self.get_valid_vehicle_no()
            vehicle_traffies = self.get_valid_float("Vehicle Traffies")
            vehicle_value = self.get_valid_float("Vehicle Value")
            driver_condition = self.get_valid_driver_condition()
            driver_email = self.get_valid_driver_email()
            driver_cost = self.get_valid_float("Driver Cost")
            return_date = self.get_valid_date("Return Date")

            total_days = (datetime.strptime(return_date, "%Y-%m-%d") - datetime.strptime(rent_date, "%Y-%m-%d")).days
            rent_total = ((vehicle_traffies * 10) + vehicle_value + driver_cost) * total_days

            update_query = "UPDATE RentCalculations SET CustomerEmail=?, RentDate=?, VehicleNo=?, VehicleTraffies=?, VehicleValue=?, DriverCondition=?, DriverEmail=?, DriverCost=?, ReturnDate=?, TotalDays=?, RentTotal=? WHERE RentID=?"
            cmd_update = self.con.cursor()
            cmd_update.execute(update_query, (customer_email, rent_date, vehicle_no, vehicle_traffies, vehicle_value, driver_condition, driver_email, driver_cost, return_date, total_days, rent_total, search_id))
            self.con.commit()

            print("Data updated successfully...!")
        except Exception as ex:
            print(f"Error updating data: {ex}")

    def delete_data(self):
        try:
            search_id = input("Enter Rent ID to delete: ")

            delete_query = "DELETE FROM RentCalculations WHERE RentID=?"
            cmd_delete = self.con.cursor()
            cmd_delete.execute(delete_query, (search_id,))
            self.con.commit()

            print("Data deleted successfully...!")
        except Exception as ex:
            print(f"Error deleting data: {ex}")

    def process_data(self):
        try:
            traffies = float(input("Enter Vehicle Traffies: "))
            vehicle_value = float(input("Enter Vehicle Value: "))
            driver_cost = float(input("Enter Driver Cost: "))

            rent_date_str = input("Enter Rent Date (YYYY-MM-DD): ")
            return_date_str = input("Enter Return Date (YYYY-MM-DD): ")

            rent_date = datetime.strptime(rent_date_str, "%Y-%m-%d")
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")

            total_days = (return_date - rent_date).days

            print("Total Days:", total_days)

            rent_total = ((traffies * 10) + vehicle_value + driver_cost) * total_days

            print("Rent Total:", rent_total)
            print("Data processed successfully...!")
        except Exception as ex:
            print(f"Error processing data: {ex}")

    def filter_data(self):
        try:
            search_date = self.get_valid_date("Rent Date to filter")

            filter_query = "SELECT * FROM RentCalculations WHERE RentDate = ?"
            cmd_filter = self.con.cursor()
            cmd_filter.execute(filter_query, (search_date,))

            data = cmd_filter.fetchall()
            self.print_data("Filtered Rent Calculations", data)

        except Exception as ex:
            print(f"Error filtering data: {ex}")

    def search_rent(self):
        try:
            search_id = input("Enter Rent ID to search: ")
            search_query = "SELECT * FROM RentCalculations WHERE RentID = ?"
            cmd_search = self.con.cursor()
            cmd_search.execute(search_query, (search_id,))
            result = cmd_search.fetchone()
            if result:
                print("Rent ID:", result[0])
                print("Customer Email:", result[1])
                print("Rent Date:", result[2])
                print("Vehicle No:", result[3])
                print("Vehicle Traffies:", result[4])
                print("Vehicle Value:", result[5])
                print("Driver Condition:", result[6])
                print("Driver Email:", result[7])
                print("Driver Cost:", result[8])
                print("Return Date:", result[9])
                print("Total Days:", result[10])
                print("Rent Total:", result[11])
            else:
                print("Rent ID not found")
        except ValueError:
            print("Rent ID must be an integer")

    def get_valid_customer_email(self):
        while True:
            try:
                customer_email = input("Enter Customer Email: ")
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', customer_email):
                    return customer_email
                else:
                    print("Invalid email format! Please enter a valid email.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_date(self, field_name):
        while True:
            try:
                date_str = input(f"Enter {field_name} (YYYY-MM-DD): ")
                datetime.strptime(date_str, "%Y-%m-%d")
                return date_str
            except ValueError:
                print("Invalid date format! Please enter a date in YYYY-MM-DD format.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_vehicle_no(self):
        while True:
            try:
                vehicle_no = input("Enter Vehicle No: ")
                if re.match(r'^[A-Za-z0-9_-]*$', vehicle_no):
                    return vehicle_no
                else:
                    print("Invalid vehicle number format! Please enter a valid number.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_float(self, field_name):
        while True:
            try:
                value = input(f"Enter {field_name}: ")
                if re.match(r'^\d+(\.\d+)?$', value):
                    return float(value)
                else:
                    print(f"Invalid {field_name}! Please enter a valid number.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_driver_condition(self):
        while True:
            try:
                condition = input("Enter Driver Condition: ")
                if condition.lower() in ['good', 'average', 'bad']:
                    return condition
                else:
                    print("Invalid driver condition! Please enter 'Good', 'Average', or 'Bad'.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_driver_email(self):
        while True:
            try:
                driver_email = input("Enter Driver Email (optional, press Enter to skip): ")
                if driver_email == "":
                    return None
                elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', driver_email):
                    return driver_email
                else:
                    print("Invalid email format! Please enter a valid email.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def print_data(self, table_name, data):
        if not data:
            print(f"No data found in {table_name}.")
            return

        print(f"\n{table_name}:\n")
        for row in data:
            print(row)

    def close_connection(self):
        try:
            self.con.close()
            print("Database connection closed successfully!")
        except Exception as e:
            print(f"Failed to close the database connection: {str(e)}")

