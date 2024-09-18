# Importing Tkinter library
import tkinter as tk

# Create the main window (the root)
root = tk.Tk()

# Set window title
root.title("My First GUI")

# Set window size
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")

# Add the label to the window
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked!"))

# Add the button to the window
button.pack()

# Start the Tkinter event loop (this keeps the window open)
root.mainloop()
