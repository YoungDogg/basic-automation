import pyautogui
import keyboard
import time
import threading
import tkinter as tk
import os

# Script Purpose: This script records mouse and keyboard activities and saves them to a file.

# Global Variables
output_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output', 'actions_record.txt')
recording = False  # Variable to control recording

# Function: record_activity
# Purpose: To continuously record the mouse position and save it to a file.
# Parameters: None
# Returns: None
def record_activity():
    global recording
    recording = True
    with open(output_file_path, 'w') as file:
        while recording:
            x, y = pyautogui.position()
            file.write(f"Mouse Position: {x}, {y}\n")
            if keyboard.is_pressed('esc'):
                recording = False
                break
            time.sleep(0.01)

# Function: start_recording
# Purpose: To start the recording of mouse and keyboard activity in a separate thread.
# Parameters: None
# Returns: None
def start_recording():
    thread = threading.Thread(target=record_activity)
    thread.start()

# Function: stop_recording
# Purpose: To stop the recording of mouse and keyboard activity.
# Parameters: None
# Returns: None
def stop_recording():
    global recording
    recording = False
