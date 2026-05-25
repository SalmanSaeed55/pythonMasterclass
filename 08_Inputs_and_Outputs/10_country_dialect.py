import csv

input_filename = "./files/country_info.txt"

with open(input_filename, encoding="utf-8", newline="") as data:
    sample = ""
    for line in range(3):
        sample += data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    data.seek(0)
    country_reader = csv.reader(data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print("-" * 80)
attributes = [
    'delimiter',
    'doublequote',
    'escapechar',
    'lineterminator',
    'quotechar',
    'quoting',
    'skipinitialspace'
]

for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")