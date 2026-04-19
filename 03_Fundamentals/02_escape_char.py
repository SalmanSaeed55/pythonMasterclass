split_string = "This string has been\nspread over\nmany lines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

# If double/single quotes are used for the string and also within the string, those repeated within the string must be escaped out of it
print("the pet shop owner said \"No, no, 'e\'s uh,...he\'s resting\".")
print("the pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# Using triple quotes means you don't need to escape any characters for quotation
print("""the pet shop owner said "No, no, 'e's uh,...he's resting".""")

# this also means that new lines are automatically added
another_Split_String = """This string has been
split over
several
lines"""
print(another_Split_String)