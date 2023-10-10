import unittest
from unittest.mock import patch, mock_open
from src.recorder import activity_recorder

class TestRecorder(unittest.TestCase):

    @patch('src.recorder.activity_recorder.pyautogui.position')
    @patch('src.recorder.activity_recorder.keyboard.is_pressed')    
    @patch('builtins.open', new_callable=mock_open)
    def test_record_activity(self, mock_file, mock_keyboard, mock_pyautogui):
        mock_pyautogui.return_value = (0, 0)  # Modify this line to return a tuple
        mock_keyboard.return_value = True  # This will simulate the 'esc' key being pressed 
        
        activity_recorder.recording = True 
        activity_recorder.record_activity() # how to match those funciton and arguments' return value?

        self.assertTrue(mock_file.called)
        self.assertTrue(mock_pyautogui.called)
        self.assertTrue(mock_keyboard.called)

if __name__ == "__main__":
    unittest.main()
