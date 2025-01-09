import re
import sqlite3
from datetime import datetime
import sys

class DayTourCalculationApp:
    def __init__(self):
        self.con = sqlite3.connect("vms_db.db")

    def start(self):
        while True:
            try:
                print("\nWhat would you like to do?")
                print("1. Search Day Tour")
                print("2. Insert Day Tour")
                print("3. Update Day Tour")
                print("4. Delete Day Tour")
                print("5. Search Customers")
                print("6. Search Drivers")
                print("7. Search Vehicles")
                print("8. Search Packages")
                print("9. View Customers")
                print("10. View Drivers")
                print("11. View Vehicles")
                print("12. View Packages")
                print("13. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    self.search_day_tour()
                elif choice == "2":
                    self.insert_data()
                elif choice == "3":
                    self.update_data()
                elif choice == "4":
                    self.delete_data()
                elif choice == "5":
                    self.search_customer()
                elif choice == "6":
                    self.search_driver()
                elif choice == "7":
                    self.search_vehicle()
                elif choice == "8":
                    self.search_package()
                elif choice == "9":
                    self.view_customers()
                elif choice == "10":
                    self.view_drivers()
                elif choice == "11":
                    self.view_vehicles()
                elif choice == "12":
                    self.view_packages()
                elif choice == "13":
                    self.close_connection()
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

    def search_day_tour(self):
        try:
            search_id = int(input("Enter Day Tour ID to search: "))
            search_query = "SELECT * FROM DayTourCalculations WHERE DayTourID = ?"
            cursor = self.con.cursor()
            cursor.execute(search_query, (search_id,))
            result = cursor.fetchone()
            if result:
                self.print_data("Day Tour", result)
            else:
                print("Day Tour ID not found")
        except ValueError:
            print("Day Tour ID must be an integer")

    def search_customer(self):
        try:
            search_email = input("Enter Customer Email to search: ")
            search_query = "SELECT * FROM Customers WHERE CustomerEmail = ?"
            cursor = self.con.cursor()
            cursor.execute(search_query, (search_email,))
            result = cursor.fetchone()
            if result:
                self.print_data("Customer", result)
            else:
                print("Customer not found")
        except Exception as ex:
            print(f"Error searching customer: {ex}")

    def search_driver(self):
        try:
            search_email = input("Enter Driver Email to search: ")
            search_query = "SELECT * FROM Drivers WHERE DriverEmail = ?"
            cursor = self.con.cursor()
            cursor.execute(search_query, (search_email,))
            result = cursor.fetchone()
            if result:
                self.print_data("Driver", result)
            else:
                print("Driver not found")
        except Exception as ex:
            print(f"Error searching driver: {ex}")

    def search_vehicle(self):
        try:
            search_vehicle_no = input("Enter Vehicle No to search: ")
            search_query = "SELECT * FROM Vehicles WHERE VehicleNo = ?"
            cursor = self.con.cursor()
            cursor.execute(search_query, (search_vehicle_no,))
            result = cursor.fetchone()
            if result:
                self.print_data("Vehicle", result)
            else:
                print("Vehicle not found")
        except Exception as ex:
            print(f"Error searching vehicle: {ex}")

    def search_package(self):
        try:
            search_id = self.get_integer_input("Enter Package ID to search: ")
            search_query = "SELECT * FROM PerDayTourPackages WHERE PerDayPackageID = ?"
            cursor = self.con.cursor()
            cursor.execute(search_query, (search_id,))
            result = cursor.fetchone()
            if result:
                self.print_data("Package", result)
            else:
                print("Package not found")
        except Exception as ex:
            print(f"Error searching package: {ex}")

    def view_customers(self):
        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM Customers")
            results = cursor.fetchall()
            if results:
                for row in results:
                    self.print_data("Customer", row)
            else:
                print("No customers found")
        except Exception as ex:
            print(f"Error viewing customers: {ex}")

    def view_drivers(self):
        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM Drivers")
            results = cursor.fetchall()
            if results:
                for row in results:
                    self.print_data("Driver", row)
            else:
                print("No drivers found")
        except Exception as ex:
            print(f"Error viewing drivers: {ex}")

    def view_vehicles(self):
        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM Vehicles")
            results = cursor.fetchall()
            if results:
                for row in results:
                    self.print_data("Vehicle", row)
            else:
                print("No vehicles found")
        except Exception as ex:
            print(f"Error viewing vehicles: {ex}")

    def view_packages(self):
        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM PerDayTourPackages")
            results = cursor.fetchall()
            if results:
                for row in results:
                    self.print_data("Package", row)
            else:
                print("No packages found")
        except Exception as ex:
            print(f"Error viewing packages: {ex}")

    def insert_data(self):
        try:
            # Get inputs with validation
            day_tour_id = self.get_integer_input("Enter Day Tour ID: ")
            customer_email = self.get_email_input("Enter Customer Email: ")
            package_type = input("Enter Package Type: ")
            package_price = self.get_float_input("Enter Package Price: ")
            max_km_limit = self.get_integer_input("Enter Max KM Limit: ")
            max_hour_limit = self.get_integer_input("Enter Max Hour Limit: ")
            vehicle_no = input("Enter Vehicle No: ")
            vehicle_traffies = self.get_integer_input("Enter Vehicle Traffics: ")
            vehicle_value = self.get_float_input("Enter Vehicle Value: ")
            driver_email = self.get_optional_email_input("Enter Driver Email (optional, press Enter to skip): ")
            driver_cost = self.get_float_input("Enter Driver Cost: ")
            start_km_reading = self.get_integer_input("Enter Start KM Reading: ")
            start_time = input("Enter Start Time (HH:MM): ")
            end_time = input("Enter End Time (HH:MM): ")
            end_km_reading = self.get_integer_input("Enter End KM Reading: ")
            
            total_time = self.calculate_total_time(start_time, end_time)
            total_km = end_km_reading - start_km_reading

            # Calculate charges
            waiting_charge = 0  # Placeholder for waiting charge calculation
            extra_km_charge = 0  # Placeholder for extra km charge calculation
            return_base_hire_charge = 0  # Placeholder for return base hire charge calculation
            day_tour_total = package_price + (vehicle_traffies * 10) + vehicle_value + driver_cost + waiting_charge + extra_km_charge + return_base_hire_charge

            # Insert data into the database
            insert_query = "INSERT INTO DayTourCalculations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor = self.con.cursor()
            cursor.execute(insert_query, (day_tour_id, customer_email, package_type, package_price, max_km_limit, max_hour_limit, vehicle_no, vehicle_traffies, vehicle_value, driver_email, driver_cost, start_km_reading, start_time, end_time, end_km_reading, total_time, total_km, waiting_charge, extra_km_charge, return_base_hire_charge, day_tour_total))
            self.con.commit()

            print("Data stored successfully...!")
        except Exception as ex:
            print(f"Error storing data: {ex}")

    def update_data(self):
        try:
            search_id = self.get_integer_input("Enter Day Tour ID to update: ")
            # Retrieve existing data
            search_query = "SELECT * FROM DayTourCalculations WHERE DayTourID = ?"
            cursor = self.con.cursor()
            cursor.execute(search_query, (search_id,))
            existing_data = cursor.fetchone()
            if not existing_data:
                print("Day Tour ID not found")
                return search_id
            
            # Collect updated data
            customer_email = input(f"Enter Customer Email ({existing_data[1]}): ") or existing_data[1]
            package_type = input(f"Enter Package Type ({existing_data[2]}): ") or existing_data[2]
            package_price = self.get_float_input(f"Enter Package Price ({existing_data[3]}): ") or existing_data[3]
            package_max_km_limit = self.get_integer_input(f"Enter Package Max KM Limit ({existing_data[4]}): ") or existing_data[4]
            package_max_hour_limit = self.get_integer_input(f"Enter Package Max Hour Limit ({existing_data[5]}): ") or existing_data[5]
            vehicle_no = input(f"Enter Vehicle No ({existing_data[6]}): ") or existing_data[6]
            vehicle_traffies = self.get_integer_input(f"Enter Vehicle Traffics ({existing_data[7]}): ") or existing_data[7]
            vehicle_value = self.get_float_input(f"Enter Vehicle Value ({existing_data[8]}): ") or existing_data[8]
            driver_email = self.get_optional_email_input(f"Enter Driver Email ({existing_data[9]}): ") or existing_data[9]
            driver_cost = self.get_float_input(f"Enter Driver Cost ({existing_data[10]}): ") or existing_data[10]
            start_km_reading = self.get_integer_input(f"Enter Start KM Reading ({existing_data[11]}): ") or existing_data[11]
            start_time = input(f"Enter Start Time (HH:MM) ({existing_data[12]}): ") or existing_data[12]
            end_time = input(f"Enter End Time (HH:MM) ({existing_data[13]}): ") or existing_data[13]
            end_km_reading = self.get_integer_input(f"Enter End KM Reading ({existing_data[14]}): ") or existing_data[14]

            total_time = self.calculate_total_time(start_time, end_time)
            total_km = end_km_reading - start_km_reading

            # Calculate charges
            waiting_charge = 0  # Placeholder for waiting charge calculation
            extra_km_charge = 0  # Placeholder for extra km charge calculation
            return_base_hire_charge = 0  # Placeholder for return base hire charge calculation
            day_tour_total = package_price + (vehicle_traffies * 10) + vehicle_value + driver_cost + waiting_charge + extra_km_charge + return_base_hire_charge

            # Update query
            update_query = "UPDATE DayTourCalculations SET CustomerEmail=?, PackageType=?, PackagePrice=?, PackageMaxKMLimit=?, PackageMaxHourLimit=?, VehicleNo=?, VehicleTraffies=?, VehicleValue=?, DriverEmail=?, DriverCost=?, StartKMReading=?, StartTime=?, EndTime=?, EndKMReading=?, TotalTime=?, TotalKM=?, WaitingCharge=?, ExtraKMcharge=?, ReturnBaseHireCharge=?, DayTourTotal=? WHERE DayTourID=?"
            cursor.execute(update_query, (customer_email, package_type, package_price, package_max_km_limit, package_max_hour_limit, vehicle_no, vehicle_traffies, vehicle_value, driver_email, driver_cost, start_km_reading, start_time, end_time, end_km_reading, total_time, total_km, waiting_charge, extra_km_charge, return_base_hire_charge, day_tour_total, search_id))
            self.con.commit()

            print("Data updated successfully...!")
        except Exception as ex:
            print(f"Error updating data: {ex}")

    def delete_data(self):
        try:
            search_id = self.get_integer_input("Enter Day Tour ID to delete: ")
            delete_query = "DELETE FROM DayTourCalculations WHERE DayTourID = ?"
            cursor = self.con.cursor()
            cursor.execute(delete_query, (search_id,))
            self.con.commit()

            print("Data deleted successfully...!")
        except Exception as ex:
            print(f"Error deleting data: {ex}")

    def calculate_total_time(self, start_time_str, end_time_str):
        start_time = datetime.strptime(start_time_str, "%H:%M")
        end_time = datetime.strptime(end_time_str, "%H:%M")
        duration = end_time - start_time
        return duration.total_seconds() / 3600  # Convert to hours

    def print_data(self, table_name, data):
        print(f"\n{table_name}:\n")
        print(data)

    def close_connection(self):
        self.con.close()
        print("Database connection closed successfully!")

    def get_integer_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input! Please enter an integer.")

    def get_float_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Invalid input! Please enter a number.")

    def get_email_input(self, prompt):
        while True:
            email = input(prompt)
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Invalid email address! Please enter a valid email.")

    def get_optional_email_input(self, prompt):
        email = input(prompt)
        if email.strip() == "":
            return None
        elif re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Invalid email address! Please enter a valid email.")

