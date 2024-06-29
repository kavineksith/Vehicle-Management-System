import sqlite3
import re
import sys

class VehiclesApp:
    def __init__(self):
        self.db_connection = sqlite3.connect("vms_db.db")
        
    def insert_vehicle(self, vehicle_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''INSERT INTO Vehicles (VehicleID, VehicleNo, VehicleType, VehicleCondition, VehicleTelNo, 
                                                      VehicleCategory, VehicleSeatCount, VehicleModel, VehicleTraffies, VehicleValue)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', vehicle_data)
            self.db_connection.commit()
            print("Vehicle data inserted successfully!")
        except Exception as e:
            print(f"Failed to insert vehicle data: {str(e)}")

    def update_vehicle(self, vehicle_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''UPDATE Vehicles SET VehicleNo=?, VehicleType=?, VehicleCondition=?, VehicleTelNo=?, 
                                                      VehicleCategory=?, VehicleSeatCount=?, VehicleModel=?, VehicleTraffies=?, VehicleValue=? 
                              WHERE VehicleID=?''', vehicle_data[1:] + [vehicle_data[0]])
            self.db_connection.commit()
            print("Vehicle data updated successfully!")
        except Exception as e:
            print(f"Failed to update vehicle data: {str(e)}")

    def delete_vehicle(self, vehicle_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''DELETE FROM Vehicles WHERE VehicleID=?''', (vehicle_id,))
            self.db_connection.commit()
            print("Vehicle data deleted successfully!")
        except Exception as e:
            print(f"Failed to delete vehicle data: {str(e)}")

    def search_vehicle(self, vehicle_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM Vehicles WHERE VehicleID=?''', (vehicle_id,))
            vehicle_data = cursor.fetchone()
            if vehicle_data:
                print("Vehicle data found:")
                print(vehicle_data)
            else:
                print("Vehicle not found!")
        except Exception as e:
            print(f"Failed to search for vehicle: {str(e)}")

    def filter_vehicle(self, criteria):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(f'''SELECT * FROM Vehicles WHERE {criteria}''')
            filtered_data = cursor.fetchall()
            if filtered_data:
                print("Filtered Vehicles:")
                for vehicle in filtered_data:
                    print(vehicle)
            else:
                print("No vehicles match the filter criteria!")
        except Exception as e:
            print(f"Failed to filter vehicles: {str(e)}")

    def view_vehicles(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM Vehicles''')
            all_vehicles = cursor.fetchall()
            if all_vehicles:
                print("All Vehicles:")
                for vehicle in all_vehicles:
                    print(vehicle)
            else:
                print("No vehicles found in the database!")
        except Exception as e:
            print(f"Failed to fetch vehicles: {str(e)}")

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
                print("1. Insert a new vehicle")
                print("2. Update vehicle details")
                print("3. Delete a vehicle")
                print("4. Search for a vehicle")
                print("5. Filter vehicles")
                print("6. View all vehicles")
                print("7. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    vehicle_data = self.get_vehicle_data_from_input()
                    self.insert_vehicle(vehicle_data)
                elif choice == '2':
                    vehicle_id = input("Enter Vehicle ID to update: ")
                    vehicle_data = self.get_vehicle_data_from_input()
                    self.update_vehicle(vehicle_data)
                elif choice == '3':
                    vehicle_id = input("Enter Vehicle ID to delete: ")
                    self.delete_vehicle(vehicle_id)
                elif choice == '4':
                    vehicle_id = input("Enter Vehicle ID to search: ")
                    self.search_vehicle(vehicle_id)
                elif choice == '5':
                    criteria = input("Enter filter criteria: ")
                    self.filter_vehicle(criteria)
                elif choice == '6':
                    self.view_vehicles()
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

    def get_vehicle_data_from_input(self):
        vehicle_id = self.get_valid_id()
        vehicle_no = self.get_valid_no()
        vehicle_type = self.get_valid_type()
        vehicle_condition = self.get_valid_condition()
        vehicle_telno = self.get_valid_telno()
        vehicle_category = self.get_valid_category()
        vehicle_seat_count = self.get_valid_seat_count()
        vehicle_model = self.get_valid_model()
        vehicle_traffies = self.get_valid_traffies()
        vehicle_value = self.get_valid_value()
        return (vehicle_id, vehicle_no, vehicle_type, vehicle_condition, vehicle_telno, vehicle_category, 
                vehicle_seat_count, vehicle_model, vehicle_traffies, vehicle_value)

    def get_valid_id(self):
        while True:
            try:
                vehicle_id = input("Enter Vehicle ID: ")
                if re.match(r'^[A-Za-z0-9_-]*$', vehicle_id):
                    return vehicle_id
                else:
                    print("Invalid ID format! Please enter a valid ID.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_no(self):
        while True:
            try:
                vehicle_no = input("Enter Vehicle No: ")
                if re.match(r'^[A-Za-z0-9_-]*$', vehicle_no):
                    return vehicle_no
                else:
                    print("Invalid number format! Please enter a valid number.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_condition(self):
        while True:
            try:
                condition = input("Enter Vehicle Condition (new/used): ").lower()
                if condition in ('new', 'used'):
                    return condition
                else:
                    print("Invalid input! Please enter 'new' or 'used'.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_type(self):
        while True:
            try:
                type = input("Enter Vehicle Type (car/truck/motorcycle): ").lower()
                if type in ('car', 'truck', 'motorcycle'):
                    return type
                else:
                    print("Invalid input! Please enter 'car', 'truck', or 'motorcycle'.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_telno(self):
        while True:
            try:
                telno = input("Enter Vehicle Tel No: ")
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
                category = input("Enter Vehicle Category (luxury/economy): ").lower()
                if category in ('luxury', 'economy'):
                    return category
                else:
                    print("Invalid input! Please enter 'luxury' or 'economy'.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_seat_count(self):
        while True:
            try:
                seat_count = input("Enter Vehicle Seat Count: ")
                if re.match(r'^\d+$', seat_count):  # Match one or more digits
                    return int(seat_count)
                else:
                    print("Invalid seat count! Please enter a positive integer.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_model(self):
        while True:
            try:
                model = input("Enter Vehicle Model: ")
                if re.match(r'^[A-Za-z0-9\s]+$', model):  # Match alphanumeric characters and spaces
                    return model
                else:
                    print("Invalid model! Please enter a valid model.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_traffies(self):
        while True:
            try:
                traffies = input("Enter Vehicle Traffies: ")
                if re.match(r'^[A-Za-z0-9\s]+$', traffies):  # Match alphanumeric characters and spaces
                    return traffies
                else:
                    print("Invalid traffies! Please enter valid traffies.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_value(self):
        while True:
            try:
                value = input("Enter Vehicle Value: ")
                if re.match(r'^\d+(\.\d+)?$', value):  # Match positive numbers (integer or decimal)
                    return float(value)
                else:
                    print("Invalid value! Please enter a valid positive number.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

