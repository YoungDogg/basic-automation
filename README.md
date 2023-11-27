# Basic Automation

## Description
This project is an automation tool designed to record and execute mouse and keyboard actions. It offers a user-friendly GUI to manage the recording and playback of these actions.

## Directory Structure
https://woochanleee.github.io/project-tree-generator/ paste this repo

## Modules and Scripts

### executor/activity_executor.py
- **Purpose**: Executes recorded mouse and keyboard actions.
- **Major Functions**:
  - `execute_actions`: Reads and executes actions from a file.

### gui/gui_controls.py
- **Purpose**: Provides GUI controls for the application.
- **Major Functions**:
  - GUI-related functions to manage user interactions.

### recorder/activity_recorder.py
- **Purpose**: Records mouse and keyboard actions.
- **Major Functions**:
  - Functions related to the recording of user activities.

### main.py
- **Purpose**: Main entry point for the GUI application.
- **Major Functions**:
  - Initializes and runs the application.

## Dependencies
Listed in `requirements.txt`.

## Setup and Execution
1. Install dependencies: `pip install -r requirements.txt`.
2. Run the application: `python main.py`.


## Installation

1. Clone the repository:

   git clone https://github.com/YoungDogg/basic-automation.git
   

2. Install the required dependencies:
pip install pyautogui

## Versioning
Git is used for version control.

## Authors/Contributors
- YoungDogg

## License
Licensed under the terms in the `LICENSE` file in the `license` directory.

## Additional Notes
This project is in active development. Future updates may include more sophisticated macro recording features and enhancements to the user interface.
