import sys
from customers import CustomersApp
from day_tour_calculation import DayTourCalculationApp
from day_tour_packages import PerDayPackagesApp
from drivers import DriversApp
from long_day_packages import LongDayPackagesApp
from long_tour_calculation import LongTourCalculationApp
from rent_tour_calculation import RentCalculationApp
from vehicles import VehiclesApp

def confirm_exit():
    while True:
        try:
            confirm_exit = input("Are you sure you want to exit? (yes/no): ")

            if confirm_exit.lower() == "yes":
                print("Exiting...")
                sys.exit(0)
            elif confirm_exit.lower() == "no":
                main()
            else:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError as e:
            print(f"{e}")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    while True:
        try:
            print("----- Welcome to Insophinia Vehicle Management System -----")
            print("\nWhat would you like to do?")
            print("1. Customer Management Portal")
            print("2. Driver Management Portal")
            print("3. Vehicle Management Portal")
            print("4. Per Day Tour Packages Management Portal")
            print("5. Long Day Tour Packages Management Portal")
            print("6. Rent Tour Calculation Portal")
            print("7. Day Tour Calculation Portal")
            print("8. Long Tour Calculation Portal")
            print("0. Exit from Application")
            
            section = int(input("Enter your choice: "))

            match section:
                case 1:
                    CustomersApp().interact()
                case 2:
                    DriversApp().interact()
                case 3:
                    VehiclesApp().interact()
                case 4:
                    PerDayPackagesApp().interact()
                case 5:
                    LongDayPackagesApp().interact()
                case 6:
                    RentCalculationApp().start()
                case 7:
                    DayTourCalculationApp().start()
                case 8:
                    LongTourCalculationApp().start()
                case 0:
                    confirm_exit()
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 8.")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)
