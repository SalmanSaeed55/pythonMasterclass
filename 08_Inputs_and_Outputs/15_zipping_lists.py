import csv

albums = [
    ("Welcome to my nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightening", "Metallica", 1984)
]
filename = "./files/albums.csv"

keys = ["album", "artist", "year"]

with open(filename, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()

    for row in albums:
        zip_object = zip(keys, row)
        # print(zip_object)
        #
        # for thing in zip_object:
        #     print(f"\t{thing}")
        albums_dict = dict(zip_object)
        print(albums_dict)
        writer.writerow(albums_dict)



