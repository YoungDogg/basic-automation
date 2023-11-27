import pyautogui
import keyboard
import time
import os

# Script Purpose: This script reads a file containing recorded mouse and keyboard actions and replicates them.

# Global Variables
output_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output', 'actions_record.txt')

# Function: execute_actions
# Purpose: To execute mouse and keyboard actions based on the recorded data in the output file.
# Parameters: None
# Returns: None
def execute_actions():
    with open(output_file_path, 'r') as file:
        for line in file:
            # Handling mouse movement events
            if 'Mouse Position:' in line:
                _, position = line.split(":")
                x, y = map(int, position.strip().split(","))
                pyautogui.moveTo(x, y)
            
            # Handling keyboard press events
            elif 'Keyboard Event:' in line:
                _, key = line.split(":")
                keyboard.press_and_release(key.strip())
            
            # Brief pause between actions
            time.sleep(0.01)