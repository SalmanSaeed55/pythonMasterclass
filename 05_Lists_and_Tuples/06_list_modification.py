computer_parts = ["Keyboard", "Mouse", "Mouse Pad", "Monitor", "Computer"]
print(computer_parts)

computer_parts[1] = "3D printer"
print(computer_parts)

computer_parts[5:] = ["Projector"]
print(computer_parts)

computer_parts[5:] = ["Projector", "Speaker", "Headphones", "Lamp"]
print(computer_parts)

new_parts = ["Webcam", "Microphone", "Laptop", "Monitor Stand"]

computer_parts += new_parts
print(computer_parts)

computer_parts.remove("Webcam")
print(computer_parts)

new_computer_parts = new_parts.copy()
print(new_computer_parts)