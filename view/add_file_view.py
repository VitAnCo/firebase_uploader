from tkinter import filedialog

class AddFileView:
    def __init__(self) -> None:
        pass
    def get_file_name(self):
        return filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = ((".bin files", "*.bin*"),
                                                    ("Text files", "*.txt*"),
                                                    ("All files",  "*.*")))
        
        
        