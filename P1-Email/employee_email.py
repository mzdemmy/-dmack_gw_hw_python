# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field 
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile, ('first_name', 'last_name','ssn'))

    header = next(reader)  #skip header row

    for row in reader:
    # construct email using first_name and last_name and add to row   
        row["email"] = (row['first_name'] + "." + row['last_name'] + "@example.com")        
        new_employee_data.append(row) 

        
# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    fields = ["first_name", "last_name","ssn","email"]
    csv_writer = csv.DictWriter(csvfile, fields)
    csv_writer.writeheader()
    csv_writer.writerows(new_employee_data)

    print("Woo Hoo! Your file update is ready to review.")


