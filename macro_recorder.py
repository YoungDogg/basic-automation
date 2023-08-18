import pyautogui
import keyboard
import time
import threading
import tkinter as tk

# Function to record mouse and keyboard activity
def record_activity():
    global recording
    recording = True
    with open('output.txt', 'w') as file:
        while recording:
            x, y = pyautogui.position()
            file.write(f"Mouse Position: {x}, {y}\n")
            if keyboard.is_pressed('esc'):  # Stop recording on 'esc' key press
                recording = False
                break
            time.sleep(0.01)

# Function to start recording
def start_recording():
    thread = threading.Thread(target=record_activity)
    thread.start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# Function to stop recording
def stop_recording():
    global recording
    recording = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Macro Recorder")
start_button = tk.Button(root, text="Start Recording", command=start_recording)
stop_button = tk.Button(root, text="Stop Recording", command=stop_recording, state=tk.DISABLED)
start_button.pack()
stop_button.pack()
root.mainloop()
