entries = [1,2, 3, 4, 5]

print(f"all: {all(entries)}")
print(f"any: {any(entries)}")

print("Iterable with a 'false' value")
entries_with_zero = [1 ,2, 0, 4 ,5]

print(f"all: {all(entries_with_zero)}")
print(f"any: {any(entries_with_zero)}")