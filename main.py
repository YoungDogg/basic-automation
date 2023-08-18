import time
import pyautogui

# Set the number of iterations and position
iterations = 3
position = (500,500)    # Replace with the desired coordinates

# Wait for 2 seconds before starting
time.sleep(2)

# Perform the click actions
for i in range(iterations):
    pyautogui.click(position)
    time.sleep(1)

print("Automation completed!")
