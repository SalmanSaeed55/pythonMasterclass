import csv

csv_filename = "./files/cereal_grains.csv"

with open(csv_filename, encoding="utf-8", newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)