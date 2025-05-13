import csv
import os
initial_data = [
    ["Brand", "Model", "Price"],
    ["Toyota", "Corolla", "20000"],
    ["Honda", "Civic", "22000"],
    ["Ford", "Focus", "21000"]
]

with open("car_brands.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(initial_data)

print("Initial car data written to 'car_brands.csv'.")

new_cars = [
    ["Mazda", "3", "23000"],
    ["Hyundai", "Elantra", "19500"],
    ["Volkswagen", "Golf", "25000"]
]

with open("car_brands.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_cars)

print("New cars added to 'car_brands.csv'.")

filename = input("Enter the filename to read car data from: ")

try:
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        print("\nCar Data:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
