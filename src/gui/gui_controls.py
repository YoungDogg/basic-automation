import tkinter as tk
from src.recorder import activity_recorder
from src.executor import activity_executor

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Actions Suite")
        
        self.start_recording_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.stop_recording_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.execute_actions_button = tk.Button(self.root, text="Execute Actions", command=self.execute_actions)
        
        self.start_recording_button.pack()
        self.stop_recording_button.pack()
        self.execute_actions_button.pack()
        
    def start_recording(self):
        activity_recorder.start_recording()
        self.start_recording_button.config(state=tk.DISABLED)
        self.stop_recording_button.config(state=tk.NORMAL)
        self.execute_actions_button.config(state=tk.DISABLED)

    def stop_recording(self):
        activity_recorder.stop_recording()
        self.start_recording_button.config(state=tk.NORMAL)
        self.stop_recording_button.config(state=tk.DISABLED)
        self.execute_actions_button.config(state=tk.NORMAL)

    def execute_actions(self):
        activity_executor.execute_actions()
        
def init_gui():
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
