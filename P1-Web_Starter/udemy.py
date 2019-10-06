import os
import csv

# Set path for source file
#udemy_csv = os.path.join("..", "Resources", "web_starter.csv")
udemy_csv = os.path.join("web_starter.csv")

# store data in lists
title = []
price = []
subscribers = []
reviews = []
length = []
review_percent = []

# Open the CSV
with open(udemy_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read through  the web_starter csv file and create lists
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        

        # Determine percent of review left to 2 decimal places
        percent = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(percent)

        # Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))


#zip lists together
zipped_data = zip(title, price, subscribers, reviews, review_percent, length) 

# Set variable for output file
output_file = os.path.join("dart_web_final.csv")

# Open the output dart_web_final csv file
with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile, delimiter=',')
        
        # Write the header row and zipped rows
        writer.writerow(["Title","Price","Subscribers","Reviews","Percent of Reviews","Length"])
        writer.writerows(zipped_data)
        print("Woo Hoo!  Your new file is ready to review.")