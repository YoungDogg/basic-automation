from tkinter import Tk, Toplevel, Button, filedialog
import os

def list_files(startpath, output_file='directory_tree.txt'):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(subindent, file))

def pick_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        list_files(folder_selected)

root = Tk()
root.withdraw()  # Hide the main window

top = Toplevel(root)
Button(top, text="Choose Directory", command=pick_directory).pack()
top.mainloop()
