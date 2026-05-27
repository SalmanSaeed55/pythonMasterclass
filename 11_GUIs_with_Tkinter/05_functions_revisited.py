def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


python_food()

centre_text("Spam and eggs")
centre_text("Spam, eggs and spam")
centre_text("Spam and eggs and spam")
centre_text(453)

