#Author: Marko Gvero
#Module 3 Lab - Case Study: Lists, Functions, and Classes
#filename: Module3-Lab-MarkoGvero.py
#This app prompts users for a car and will then ask for information about that car
#it will then print the car's information in a readable format

print("")
vehicle_type = input("enter the vehicle type. (car, truck, plane, boat, broomstick) ")
vehicle_year = input("enter the vehicle year. ")
vehicle_make = input("enter the vehicle make. ")
vehicle_model = input("enter the vehicle model. ")
vehicle_doors = input("enter the number of doors. ")
vehicle_roof = input("enter type of roof ex Hard-top ")

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, vehicle_year, vehicle_make, vehicle_model, vehicle_doors, vehicle_roof):
        super().__init__(vehicle_type)
        self.vehicle_year = vehicle_year
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
        self.vehicle_doors = vehicle_doors
        self.vehicle_roof = vehicle_roof

my_car = Automobile(vehicle_type, vehicle_year, vehicle_make, vehicle_model, vehicle_doors, vehicle_roof)

print(f"""
        Vehicle Type: {my_car.vehicle_type}
        Vehicle Year: {my_car.vehicle_year}
        Vehicle Make: {my_car.vehicle_make}
        Vehicle Model: {my_car.vehicle_model}
        Number of Doors: {my_car.vehicle_doors}
        Type of Roof: {my_car.vehicle_roof}""")

'''
Test Cases
test 1
enter the vehicle type. (car, truck, plane, boat, broomstick) Car
enter the vehicle year. 1991
enter the vehicle make. Honda
enter the vehicle model. Cr-X
enter the number of doors. 2
enter type of roof ex Hard-top Hard-Top

        Vehicle Type: Car
        Vehicle Year: 1991
        Vehicle Make: Honda
        Vehicle Model: Cr-X
        Number of Doors: 2
        Type of Roof: Hard-Top

Process finished with exit code 0

test 2
enter the vehicle type. (car, truck, plane, boat, broomstick) plane
enter the vehicle year. 1972
enter the vehicle make. Cessna
enter the vehicle model. 150l
enter the number of doors. 2
enter type of roof ex Hard-top Fixed Wing

        Vehicle Type: plane
        Vehicle Year: 1972
        Vehicle Make: Cessna
        Vehicle Model: 150l
        Number of Doors: 2
        Type of Roof: Fixed Wing

Process finished with exit code 0
'''