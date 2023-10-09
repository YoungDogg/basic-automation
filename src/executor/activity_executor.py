import pyautogui
import keyboard
import time
import os

# Setting path for the output file
output_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output', 'actions_record.txt')

# Function to execute mouse and keyboard actions
def execute_actions():
    with open(output_file_path, 'r') as file:
        for line in file:
            if 'Mouse Position:' in line:
                _, position = line.split(":")
                x, y = map(int, position.strip().split(","))
                pyautogui.moveTo(x, y)
            elif 'Keyboard Event:' in line:
                _, key = line.split(":")
                keyboard.press_and_release(key.strip())
            time.sleep(0.01)
