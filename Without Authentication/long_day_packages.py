import sqlite3
import re
import sys

class LongDayPackagesApp:
    def __init__(self):
        self.db_connection = sqlite3.connect("vms_db.db")
        
    def insert_package(self, package_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''INSERT INTO LongDayTourPackages (LongDayPackageID, PackageType, PackageBasedVehicleType,
                                                               PackageMaxKMLimit, PackagePrice)
                              VALUES (?, ?, ?, ?, ?)''', package_data)
            self.db_connection.commit()
            print("Package data inserted successfully!")
        except Exception as e:
            print(f"Failed to insert package data: {str(e)}")

    def update_package(self, package_data):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''UPDATE LongDayTourPackages SET PackageType=?, PackageBasedVehicleType=?,
                                                      PackageMaxKMLimit=?, PackagePrice=? 
                              WHERE LongDayPackageID=?''', package_data[1:] + [package_data[0]])
            self.db_connection.commit()
            print("Package data updated successfully!")
        except Exception as e:
            print(f"Failed to update package data: {str(e)}")

    def delete_package(self, package_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''DELETE FROM LongDayTourPackages WHERE LongDayPackageID=?''', (package_id,))
            self.db_connection.commit()
            print("Package data deleted successfully!")
        except Exception as e:
            print(f"Failed to delete package data: {str(e)}")

    def search_package(self, package_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM LongDayTourPackages WHERE LongDayPackageID=?''', (package_id,))
            package_data = cursor.fetchone()
            if package_data:
                print("Package data found:")
                print(package_data)
            else:
                print("Package not found!")
        except Exception as e:
            print(f"Failed to search for package: {str(e)}")

    def filter_package(self, criteria):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(f'''SELECT * FROM LongDayTourPackages WHERE {criteria}''')
            filtered_data = cursor.fetchall()
            if filtered_data:
                print("Filtered Packages:")
                for package in filtered_data:
                    print(package)
            else:
                print("No packages match the filter criteria!")
        except Exception as e:
            print(f"Failed to filter packages: {str(e)}")

    def view_packages(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''SELECT * FROM LongDayTourPackages''')
            all_packages = cursor.fetchall()
            if all_packages:
                print("All Packages:")
                for package in all_packages:
                    print(package)
            else:
                print("No packages found in the database!")
        except Exception as e:
            print(f"Failed to fetch packages: {str(e)}")

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
                print("1. Insert a new package")
                print("2. Update package details")
                print("3. Delete a package")
                print("4. Search for a package")
                print("5. Filter packages")
                print("6. View all packages")
                print("7. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    package_data = self.get_package_data_from_input()
                    self.insert_package(package_data)
                elif choice == '2':
                    package_id = input("Enter Package ID to update: ")
                    package_data = self.get_package_data_from_input()
                    self.update_package(package_data)
                elif choice == '3':
                    package_id = input("Enter Package ID to delete: ")
                    self.delete_package(package_id)
                elif choice == '4':
                    package_id = input("Enter Package ID to search: ")
                    self.search_package(package_id)
                elif choice == '5':
                    criteria = input("Enter filter criteria: ")
                    self.filter_package(criteria)
                elif choice == '6':
                    self.view_packages()
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

    def get_package_data_from_input(self):
        package_id = self.get_valid_package_id()
        package_type = self.get_valid_package_type()
        package_based_vehicle_type = self.get_valid_package_based_vehicle_type()
        package_max_km_limit = self.get_valid_max_km_limit()
        package_price = self.get_valid_package_price()
        return (package_id, package_type, package_based_vehicle_type, package_max_km_limit, package_price)

    def get_valid_package_id(self):
        while True:
            try:
                package_id = input("Enter Package ID: ")
                if re.match(r'^[A-Za-z0-9_-]*$', package_id):
                    return package_id
                else:
                    print("Invalid package ID format! Please enter a valid ID.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_package_type(self):
        while True:
            try:
                package_type = input("Enter Package Type: ")
                if re.match(r'^[A-Za-z\s]+$', package_type):
                    return package_type
                else:
                    print("Invalid package type! Please enter a valid type.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_package_based_vehicle_type(self):
        while True:
            try:
                package_based_vehicle_type = input("Enter Package Based Vehicle Type: ")
                if re.match(r'^[A-Za-z\s]+$', package_based_vehicle_type):
                    return package_based_vehicle_type
                else:
                    print("Invalid package based vehicle type! Please enter a valid type.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_max_km_limit(self):
        while True:
            try:
                max_km_limit = input("Enter Max KM Limit: ")
                if re.match(r'^\d+$', max_km_limit):
                    return int(max_km_limit)
                else:
                    print("Invalid max KM limit! Please enter a valid integer.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_valid_package_price(self):
        while True:
            try:
                package_price = input("Enter Package Price: ")
                if re.match(r'^\d+(\.\d+)?$', package_price):
                    return float(package_price)
                else:
                    print("Invalid package price! Please enter a valid number.")
            except KeyboardInterrupt:
                print("Process interrupted by the user.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

