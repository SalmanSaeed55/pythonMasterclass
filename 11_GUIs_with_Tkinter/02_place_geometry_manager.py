import tkinter as tk

mainWindow = tk.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+30+20")

label = tk.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tk.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tk.Canvas(leftFrame, relief="solid", borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tk.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky="n")

button1 = tk.Button(rightFrame, text="Button 1")
button2 = tk.Button(rightFrame, text="Button 2")
button3 = tk.Button(rightFrame, text="Button 3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)

button2.grid(sticky="ew")
mainWindow.mainloop()