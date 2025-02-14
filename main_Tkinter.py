import tkinter as tk
import random


root = tk.Tk()
root.title("Catch my Heart!")

# Canvas dimensions
WIDTH, HEIGHT = 500, 500
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="pink")
canvas.pack()

# Initial position of the heart
x, y = WIDTH / 2, HEIGHT / 2
size = 30  # Size of the heart

def draw_heart():
    """Draws a heart at the current (x, y) position."""
    global x, y  # Ensure function has access to x and y
    canvas.delete("heart")  # Clear previous heart
    canvas.create_text(x, y, text="❤️", font=("Arial", size), tag="heart", fill='red')

def move_heart(event):
    """Moves the heart away when the mouse gets close."""
    global x, y  # Make x and y accessible inside the function
    threshold = 40  # Distance at which the heart moves

    # Calculate distance from the heart
    dx, dy = event.x - x, event.y - y
    distance = (dx**2 + dy**2) ** 0.5

    if distance < threshold:
        # Move to a new random position
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        draw_heart()  # Call the function without arguments

# Draw the first heart
draw_heart()

# Bind mouse movement to the function
canvas.bind("<Motion>", move_heart)

# Run the Tkinter event loop
root.mainloop()