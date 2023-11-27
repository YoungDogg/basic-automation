import tkinter as tk
from src.recorder import activity_recorder
from src.executor import activity_executor

# Class: GUIApp
# Purpose: To provide a graphical interface for recording and executing automated actions.
# Parameters: root (tk.Tk) - The main window of the application.
# Methods:
# - __init__: Initializes the GUI application.
# - start_recording: Starts the recording of actions.
# - stop_recording: Stops the recording of actions.
# - execute_actions: Executes the recorded actions.

class GUIApp:
    # Constructor: Initializes the GUI application.
    # Parameters: root (tk.Tk) - The main window of the application.
    # Returns: None
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Actions Suite")
        
        # GUI Elements
        self.start_recording_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.stop_recording_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.execute_actions_button = tk.Button(self.root, text="Execute Actions", command=self.execute_actions)
        
        # Layout
        self.start_recording_button.pack()
        self.stop_recording_button.pack()
        self.execute_actions_button.pack()

    # Method: start_recording
    # Purpose: To start the recording of actions.
    # Parameters: None
    # Returns: None
    def start_recording(self):
        activity_recorder.start_recording()
        self.start_recording_button.config(state=tk.DISABLED)
        self.stop_recording_button.config(state=tk.NORMAL)
        self.execute_actions_button.config(state=tk.DISABLED)

    # Method: stop_recording
    # Purpose: To stop the recording of actions.
    # Parameters: None
    # Returns: None
    def stop_recording(self):
        activity_recorder.stop_recording()
        self.start_recording_button.config(state=tk.NORMAL)
        self.stop_recording_button.config(state=tk.DISABLED)
        self.execute_actions_button.config(state=tk.NORMAL)

    # Method: execute_actions
    # Purpose: To execute the recorded actions.
    # Parameters: None
    # Returns: None
    def execute_actions(self):
        activity_executor.execute_actions()

# Function: init_gui
# Purpose: Initializes and starts the GUI application.
# Parameters: None
# Returns: None
def init_gui():
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
