#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:02:27 2023

@author: leozhang
"""

import tkinter as tk
from tkinter import ttk
import subprocess

# Function to handle button clicks
def on_button_click(script_number):
    if script_number == 1:
        result_label.config(text="Starting Callibration.")
        subprocess.run(["python", "script1.py"]) #replace with callibration script
    elif script_number == 2:
        result_label.config(text="Starting Program")
        subprocess.run(["python", "startprogram.py"]) #replace with start program script

# Create the main window
root = tk.Tk()
root.title("Remmy")

# Configure window size and padding
root.geometry("300x150")
root.resizable(False, False)
root.configure(padx=20, pady=20)

# Button 1
button1 = ttk.Button(root, text="Callibrate Headset", command=lambda: on_button_click(1))
button1.pack(pady=10, fill=tk.X)

# Button 2
button2 = ttk.Button(root, text="Run Program", command=lambda: on_button_click(2))
button2.pack(pady=10, fill=tk.X)

# Label to display script execution status
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Start the main loop
root.mainloop()
