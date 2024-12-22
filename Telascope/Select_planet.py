import StellariumRC
import tkinter as tk
from tkinter import simpledialog

# Set up StellariumRC
s = StellariumRC.Stellarium()

# Function to ask user for a planet name and focus on it
def select_planet():
    # Ask the user to enter the name of the planet
    planet_name = simpledialog.askstring("Select Planet", "Enter the planet name (e.g., 'Mars'):")
    if planet_name:
        # Focus on the selected planet
        s.main.setFocus(target=planet_name, mode='zoom')
        print(f"Focusing on {planet_name}")

# Set up a basic Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt user to select a planet
select_planet()
