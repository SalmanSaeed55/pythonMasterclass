import tkinter as tk

mainWindow = tk.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+30+20")

label = tk.Label(mainWindow, text="Hello World")
label.pack(side="top")

leftFrame = tk.Frame(mainWindow)
leftFrame.pack(side="left", anchor="n", fill=tk.Y, expand=False)

canvas = tk.Canvas(leftFrame, relief="solid", borderwidth=1)
canvas.pack(side="left", anchor="n")

rightFrame = tk.Frame(mainWindow)
rightFrame.pack(side="right", anchor="n", expand=False)

button1 = tk.Button(rightFrame, text="Button 1")
button2 = tk.Button(rightFrame, text="Button 2")
button3 = tk.Button(rightFrame, text="Button 3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

mainWindow.mainloop()