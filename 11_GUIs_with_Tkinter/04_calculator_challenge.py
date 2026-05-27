import tkinter as tk

keys = [[("C", 1), ("CE", 2)],
        [("7", 1), ("8", 1), ("9", 1), ("+", 1)],
        [("4", 1), ("5", 1), ("6", 1), ("-", 1)],
        [("1", 1), ("2", 1), ("3", 1), ("*", 1)],
        [("0", 1), ("=", 1), ("/", 1)]]
mainWindow_padding = 8

mainWindow = tk.Tk()
mainWindow.title("Calculator Challenge")
mainWindow.geometry("640x480+12+20")
mainWindow["padx"] = mainWindow_padding

result = tk.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky="nsew")

keyPad = tk.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky="nsew")

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tk.Button(
            keyPad, text=key[0]
        ).grid(row=row, column=col, columnspan=key[1], sticky=tk.E + tk.W)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindow_padding, keyPad.winfo_height() + mainWindow_padding)

mainWindow.mainloop()