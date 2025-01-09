import re
import sqlite3
import sys
from datetime import datetime

class LongTourCalculationApp:
    def __init__(self):
        self.con = sqlite3.connect("vms_db.db")
        
    def start(self):
        while True:
            try:
                print("\nWhat would you like to do?")
                print("1. Search Long Tour")
                print("2. Search Customer")
                print("3. Search Vehicle")
                print("4. Search Driver")
                print("5. View Customers")
                print("6. View Vehicles")
                print("7. View Drivers")
                print("8. View Long Tour Calculations")
                print("9. Insert Data")
                print("10. Update Data")
                print("11. Delete Data")
                print("12. Calculate Total")
                print("13. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.search_long_tour()
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
                    self.view_long_tour_calculations()
                elif choice == "9":
                    self.insert_data()
                elif choice == "10":
                    self.update_data()
                elif choice == "11":
                    self.delete_data()
                elif choice == "12":
                    self.calculate_total()
                elif choice == "13":
                    print("Exiting the application...")
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
                print("Vehicle Traffics:", result[6])
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

    def view_long_tour_calculations(self):
        try:
            command = "SELECT * FROM LongTourCalculations"
            cursor = self.con.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            self.print_data("Long Tour Calculations", data)
        except Exception as ex:
            print(f"Error viewing long tour calculations: {ex}")

    def insert_data(self):
        try:
            long_tour_id = input("Enter Long Tour ID: ")
            customer_email = self.get_valid_customer_email()
            package_type = input("Enter Package Type: ")
            package_price = self.get_valid_float("Package Price")
            max_km_limit = int(input("Enter Max KM Limit: "))
            vehicle_no = self.get_valid_vehicle_no()
            vehicle_traffics = self.get_valid_float("Vehicle Traffics")
            vehicle_value = self.get_valid_float("Vehicle Value")
            driver_email = self.get_valid_driver_email()
            driver_cost = self.get_valid_float("Driver Cost")
            start_km_reading = int(input("Enter Start KM Reading: "))
            start_date = self.get_valid_date("Start Date")
            end_date = self.get_valid_date("End Date")
            end_km_reading = int(input("Enter End KM Reading: "))

            total_days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
            total_km = end_km_reading - start_km_reading

            over_night_stay_charge = self.get_valid_float("Overnight Stay Charge")
            vehicle_night_park_charge = self.get_valid_float("Vehicle Night Park Charge")
            extra_km_charge = self.get_valid_float("Extra KM Charge")
            return_base_hire_charge = self.get_valid_float("Return Base Hire Charge")

            long_tour_total = package_price + (vehicle_traffics * 10) + vehicle_value + driver_cost + over_night_stay_charge + vehicle_night_park_charge + extra_km_charge + return_base_hire_charge

            insert_query = "INSERT INTO LongTourCalculations (LongTourID, CustomerEmail, PackageType, PackagePrice, PackageMaxKMLimit, VehicleNo, VehicleTraffics, VehicleValue, DriverEmail, DriverCost, StartKMReading, StartDate, EndDate, EndKMReading, TotalDays, TotalKM, OverNightStayCharge, VehicleNightParkCharge, ExtraKMCharge, ReturnBaseHireCharge, LongTourTotal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cmd_insert = self.con.cursor()
            cmd_insert.execute(insert_query, (long_tour_id, customer_email, package_type, package_price, max_km_limit, vehicle_no, vehicle_traffics, vehicle_value, driver_email, driver_cost, start_km_reading, start_date, end_date, end_km_reading, total_days, total_km, over_night_stay_charge, vehicle_night_park_charge, extra_km_charge, return_base_hire_charge, long_tour_total))
            self.con.commit()

            print("Data stored successfully...!")

        except Exception as ex:
            print(f"Error storing data: {ex}")

    def update_data(self):
        try:
            search_id = input("Enter Long Tour ID to update: ")

            customer_email = self.get_valid_customer_email()
            package_type = input("Enter Package Type: ")
            package_price = self.get_valid_float("Package Price")
            max_km_limit = int(input("Enter Max KM Limit: "))
            vehicle_no = self.get_valid_vehicle_no()
            vehicle_traffics = self.get_valid_float("Vehicle Traffics")
            vehicle_value = self.get_valid_float("Vehicle Value")
            driver_email = self.get_valid_driver_email()
            driver_cost = self.get_valid_float("Driver Cost")
            start_km_reading = int(input("Enter Start KM Reading: "))
            start_date = self.get_valid_date("Start Date")
            end_date = self.get_valid_date("End Date")
            end_km_reading = int(input("Enter End KM Reading: "))

            total_days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
            total_km = end_km_reading - start_km_reading

            over_night_stay_charge = self.get_valid_float("Overnight Stay Charge")
            vehicle_night_park_charge = self.get_valid_float("Vehicle Night Park Charge")
            extra_km_charge = self.get_valid_float("Extra KM Charge")
            return_base_hire_charge = self.get_valid_float("Return Base Hire Charge")

            long_tour_total = package_price + (vehicle_traffics * 10) + vehicle_value + driver_cost + over_night_stay_charge + vehicle_night_park_charge + extra_km_charge + return_base_hire_charge

            update_query = "UPDATE LongTourCalculations SET CustomerEmail=?, PackageType=?, PackagePrice=?, PackageMaxKMLimit=?, VehicleNo=?, VehicleTraffics=?, VehicleValue=?, DriverEmail=?, DriverCost=?, StartKMReading=?, StartDate=?, EndDate=?, EndKMReading=?, TotalDays=?, TotalKM=?, OverNightStayCharge=?, VehicleNightParkCharge=?, ExtraKMCharge=?, ReturnBaseHireCharge=?, LongTourTotal=? WHERE LongTourID=?"
            cmd_update = self.con.cursor()
            cmd_update.execute(update_query, (customer_email, package_type, package_price, max_km_limit, vehicle_no, vehicle_traffics, vehicle_value, driver_email, driver_cost, start_km_reading, start_date, end_date, end_km_reading, total_days, total_km, over_night_stay_charge, vehicle_night_park_charge, extra_km_charge, return_base_hire_charge, long_tour_total, search_id))
            self.con.commit()

            print("Data updated successfully...!")
        except Exception as ex:
            print(f"Error updating data: {ex}")

    def delete_data(self):
        try:
            search_id = input("Enter Long Tour ID to delete: ")

            delete_query = "DELETE FROM LongTourCalculations WHERE LongTourID=?"
            cmd_delete = self.con.cursor()
            cmd_delete.execute(delete_query, (search_id,))
            self.con.commit()

            print("Data deleted successfully...!")
        except Exception as ex:
            print(f"Error deleting data: {ex}")

    def calculate_total(self):
        try:
            package_price = self.get_valid_float("Package Price")
            vehicle_traffics = self.get_valid_float("Vehicle Traffics")
            vehicle_value = self.get_valid_float("Vehicle Value")
            driver_cost = self.get_valid_float("Driver Cost")
            start_km_reading = int(input("Enter Start KM Reading: "))
            start_date = self.get_valid_date("Start Date")
            end_date = self.get_valid_date("End Date")
            end_km_reading = int(input("Enter End KM Reading: "))

            total_days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
            total_km = end_km_reading - start_km_reading

            over_night_stay_charge = self.get_valid_float("Overnight Stay Charge")
            vehicle_night_park_charge = self.get_valid_float("Vehicle Night Park Charge")
            extra_km_charge = self.get_valid_float("Extra KM Charge")
            return_base_hire_charge = self.get_valid_float("Return Base Hire Charge")

            long_tour_total = package_price + (vehicle_traffics * 10) + vehicle_value + driver_cost + over_night_stay_charge + vehicle_night_park_charge + extra_km_charge + return_base_hire_charge

            print("Long Tour Total:", long_tour_total)
            print("Data processed successfully...!")
        except Exception as ex:
            print(f"Error processing data: {ex}")

    def search_long_tour(self):
        try:
            search_id = input("Enter Long Tour ID to search: ")
            search_query = "SELECT * FROM LongTourCalculations WHERE LongTourID = ?"
            cmd_search = self.con.cursor()
            cmd_search.execute(search_query, (search_id,))
            result = cmd_search.fetchone()
            if result:
                print("Long Tour ID:", result[0])
                print("Customer Email:", result[1])
                print("Package Type:", result[2])
                print("Package Price:", result[3])
                print("Package Max KM Limit:", result[4])
                print("Vehicle No:", result[5])
                print("Vehicle Traffics:", result[6])
                print("Vehicle Value:", result[7])
                print("Driver Email:", result[8])
                print("Driver Cost:", result[9])
                print("Start KM Reading:", result[10])
                print("Start Date:", result[11])
                print("End Date:", result[12])
                print("End KM Reading:", result[13])
                print("Total Days:", result[14])
                print("Total KM:", result[15])
                print("Overnight Stay Charge:", result[16])
                print("Vehicle Night Park Charge:", result[17])
                print("Extra KM Charge:", result[18])
                print("Return Base Hire Charge:", result[19])
                print("Long Tour Total:", result[20])
            else:
                print("Long Tour ID not found")
        except ValueError:
            print("Long Tour ID must be an integer")

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

