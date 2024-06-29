customers_table = """CREATE TABLE Customers 
(
CustomerID TEXT PRIMARY KEY,
CustomerName TEXT,
CustomerGender TEXT,
CustomerEmail TEXT,
CustomerTelNo INTEGER,
CustomerCategory TEXT
)
"""

drivers_table = """
CREATE TABLE Drivers 
(
DriverID TEXT PRIMARY KEY,
DriverName TEXT,
DriverGender TEXT,
DriverEmail TEXT,
DriverNo INTEGER
)
"""

vehicles_table = """
CREATE TABLE Vehicles 
(
VehicleID TEXT PRIMARY KEY,
VehicleNo TEXT,
VehicleType TEXT,
VehicleCondition TEXT,
VehicleTelNo INTEGER,
VehicleCategory TEXT,
VehicleSeatCount INTEGER,
VehicleModel TEXT,
VehicleTraffies TEXT,
VehicleValue REAL
)
"""

per_day_packages = """
CREATE TABLE PerDayTourPackages 
(
PackageID TEXT PRIMARY KEY,
PackageType TEXT,
PackageBasedVehicleType TEXT,
MaxKMLimit INTEGER,
MaxHourLimit INTEGER,
PackagePrice REAL
)
"""

long_day_packages = """
CREATE TABLE LongDayTourPackages 
(
LongDayPackageID TEXT PRIMARY KEY,
PackageType TEXT,
PackageBasedVehicleType TEXT,
PackageMaxKMLimit INTEGER,
PackagePrice INTEGER
)
"""

rent_calculations = """
CREATE TABLE RentCalculations 
(
RentID INTEGER PRIMARY KEY AUTOINCREMENT,
CustomerEmail TEXT NOT NULL,
RentDate TEXT NOT NULL,
VehicleNo TEXT NOT NULL,
VehicleTraffies REAL,
VehicleValue REAL,
DriverCondition TEXT,
DriverEmail TEXT,
DriverCost REAL,
ReturnDate TEXT,
TotalDays INTEGER,
RentTotal REAL,
FOREIGN KEY (CustomerEmail) REFERENCES Customers(CustomerEmail),
FOREIGN KEY (VehicleNo) REFERENCES Vehicles(VehicleNo),
FOREIGN KEY (DriverEmail) REFERENCES Drivers(DriverEmail)
)
"""

day_tour_calculations = """
CREATE TABLE DayTourCalculations (
DayTourID INTEGER PRIMARY KEY,
CustomerEmail TEXT,
PackageType TEXT,
PackagePrice REAL,
PackageMaxKMLimit INTEGER,
PackageMaxHourLimit INTEGER,
VehicleNo TEXT,
VehicleTraffies INTEGER,
VehicleValue REAL,
DriverEmail TEXT,
DriverCost REAL,
StartKMReading INTEGER,
StartTime TEXT,
EndTime TEXT,
EndKMReading INTEGER,
TotalTime INTEGER,
TotalKM INTEGER,
WaitingCharge REAL,
ExtraKMCharge REAL,
ReturnBaseHireCharge REAL,
DayTourTotal REAL
)
"""

long_tour_calculations = """
CREATE TABLE LongTourCalculations 
(
LongTourID INTEGER PRIMARY KEY AUTOINCREMENT,
CustomerEmail TEXT NOT NULL,
PackageType TEXT,
PackagePrice REAL,
PackageMaxKMLimit INTEGER,
VehicleNo TEXT NOT NULL,
VehicleTraffics REAL,
VehicleValue REAL,
DriverEmail TEXT,
DriverCost REAL,
StartKMReading INTEGER,
StartDate TEXT NOT NULL,
EndDate TEXT NOT NULL,
EndKMReading INTEGER,
TotalDays INTEGER,
TotalKM INTEGER,
OverNightStayCharge REAL,
VehicleNightParkCharge REAL,
ExtraKMCharge REAL,
ReturnBaseHireCharge REAL,
LongTourTotal REAL,
FOREIGN KEY (CustomerEmail) REFERENCES Customers(CustomerEmail),
FOREIGN KEY (VehicleNo) REFERENCES Vehicles(VehicleNo),
FOREIGN KEY (DriverEmail) REFERENCES Drivers(DriverEmail)
)
"""

table_list = ['Customers', 'Drivers', 'Vehicles', 'PerDayTourPackages', 'LongDayTourPackages', 'RentCalculations', 'DayTourCalculations', 'LongTourCalculations']
queries = [customers_table, drivers_table, vehicles_table, per_day_packages, long_day_packages, rent_calculations, day_tour_calculations, long_tour_calculations]