from medals_data import medals_table

print(medals_table.sort(key=lambda d: d["country"], reverse=True))
