import pyautogui
import keyboard
import time
import threading
import tkinter as tk
import os

# Setting path for the output file
output_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output', 'actions_record.txt')

# Global variable to control recording
recording = False

# Function to record mouse and keyboard activity
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

# Function to start recording
def start_recording():
    thread = threading.Thread(target=record_activity)
    thread.start()

# Function to stop recording
def stop_recording():
    global recording
    recording = False
