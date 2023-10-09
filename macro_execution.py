import pyautogui
import keyboard
import time

# Function to execute mouse and keyboard actions
def execute_actions():
    with open('output.txt', 'r') as file:
        for line in file:
            if 'Mouse Position:' in line:
                _, position = line.split(":")
                x, y = map(int, position.strip().split(","))
                pyautogui.moveTo(x, y)
            elif 'Keyboard Event:' in line:  # Assuming you add keyboard events to output.txt
                _, key = line.split(":")
                keyboard.press_and_release(key.strip())
            time.sleep(0.01)  # Same sleep time as in the recording

if __name__ == "__main__":
    execute_actions()
