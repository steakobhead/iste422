import json
import csv
from datetime import datetime

# Load data.json
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Filter out records with no ccn
filteredData = [record for record in data if 'creditcard' in record and record['creditcard']]


# Get date in format YYYYMMDD
currentDate = datetime.now().strftime('%Y%m%d')

# Create the csv file
filename = f"{currentDate}.csv"
with open(filename, 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Credit Card']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the csv file
    writer.writeheader()

    for record in filteredData:
        writer.writerow({'Name': record['name'], 'Credit Card': record['creditcard']})

print(f"CSV file '{filename}' has been generated successfully.")
