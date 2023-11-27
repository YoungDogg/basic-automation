# Automated Actions Suite

## Description
This project is an automation tool designed to record and execute mouse and keyboard actions. It offers a user-friendly GUI to manage the recording and playback of these actions.

## Directory Structure
📦 Automated_Actions_Suite
├─ .gitignore
├─ README.md
├─ basic-macro.py
├─ directory_tree.txt
├─ docs
│ └─ memo.md
├─ license
│ └─ LICENSE
├─ logs
│ └─ activity_log.txt
├─ macro_execution.py
├─ macro_recorder.py
├─ main.py
├─ output.txt
├─ output
│ └─ actions_record.txt
├─ requirements.txt
├─ src
│ ├─ executor
│ │ ├─ pycache
│ │ │ └─ activity_executor.cpython-311.pyc
│ │ └─ activity_executor.py
│ ├─ gui
│ │ ├─ pycache
│ │ │ └─ gui_controls.cpython-311.pyc
│ │ └─ gui_controls.py
│ └─ recorder
│ ├─ pycache
│ │ └─ activity_recorder.cpython-311.pyc
│ └─ activity_recorder.py
├─ tests
│ └─ test_macros.py
├─ tree-formatting.py
└─ utilities
├─ directory_structure.py
└─ requirements_manager.py

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

## Versioning
Git is used for version control.

## Authors/Contributors
- YoungDogg

## License
Licensed under the terms in the `LICENSE` file in the `license` directory.

## Additional Notes
This project is in active development. Future updates may include more sophisticated macro recording features and enhancements to the user interface.
