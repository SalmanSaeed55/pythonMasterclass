import random
import tkinter as tk

mainWindow = tk.Tk()


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    if tk.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # for each, retrieve image for the cards
    for suit in suits:
        for card in range(1, 11):
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tk.PhotoImage(file=name)
            card_images.append((card, image))

        # Now face cards
        for card in face_cards:
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tk.PhotoImage(file=name)
            card_images.append((card, image))

# Set up screen and frames for the dealer and player
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")

result_text = tk.StringVar()
result = tk.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tk.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tk.IntVar()
tk.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tk.Label(card_frame, text="Dealer Score Label", background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold card images
dealer_card_frame = tk.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tk.IntVar()
tk.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tk.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold card images
player_card_frame = tk.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tk.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tk.Button(button_frame)
dealer_button.grid(row=0, column=0)

player_button = tk.Button(button_frame)
player_button.grid(row=0, column=1)

# load cards
cards = []
load_images(cards)
print(cards)

# create new deck and shuffle
deck = list(cards)
random.shuffle(deck)

#create lists to store both sets of hands
dealer_hand = []
player_hand = []

mainWindow.mainloop()