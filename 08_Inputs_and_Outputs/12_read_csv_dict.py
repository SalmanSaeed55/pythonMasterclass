import csv

cereals_filename = "./files/cereal_grains.csv"

with open(cereals_filename, encoding="utf-8", newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)