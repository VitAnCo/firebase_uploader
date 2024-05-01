import tkinter as tk
from tkinter import *


class MainView(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('600x300')
        self.title("FIRMWARE UPLOADER")
        self.minsize(600, 300)
        self.configure(background='aliceblue')

        self.main_frame = tk.Frame(self, bg = 'aliceblue')
        self.main_frame.pack(expand=1, fill=BOTH, side=TOP, anchor=N)

        self.file_link = StringVar(value="None")

        # Title
        self.frame_title = Label(self.main_frame, text="FIRMWARE UPLOADER" , fg = "crimson",padx=10, pady=10, font=('Mona Sans Bold', 25), bg = 'aliceblue')
        self.frame_title.pack(side=TOP,padx=10, pady=10)

        # Select file frame
        self.choose_file_frame = Frame(self.main_frame, bg = 'aliceblue')
        self.choose_file_frame.pack(side=TOP, expand=1, fill=X)

        # Upload file label
        self.test_file_label = Label(self.choose_file_frame, text="Upload file: ", fg = "blue", font=('Mona Sans Bold', 15), padx= 10, bg = 'aliceblue')
        self.test_file_label.pack(side=LEFT)

        # File path label
        self.test_file_dir = Entry(self.choose_file_frame, textvariable=self.file_link)
        self.test_file_dir.pack(side=LEFT, expand=1, fill=X)
        
        # Add file path button
        self.addfile_button = Button(self.choose_file_frame, text = "Select file", width=10, height=1)
        self.addfile_button.pack(side=RIGHT, padx=5)
        
        # Node ID frame
        self.nodeid_frame = Frame(self.main_frame, bg = 'aliceblue')
        self.nodeid_frame.pack(expand=1, fill=X, anchor=N)

        # Node ID label
        self.nodeid_label = Label(self.nodeid_frame, text="Node ID: ", fg = "blue", font=('Mona Sans Bold', 15), padx= 10, bg = 'aliceblue')
        self.nodeid_label.pack(side=LEFT)

        # Node ID entry
        self.nodeid = IntVar()
        self.nodeid_entry = Entry(self.nodeid_frame, width=20, textvariable=self.nodeid)
        self.nodeid_entry.pack(side=LEFT, padx=10)

        # Button frame
        self.button_frame = tk.Frame(self, bg = 'aliceblue')
        self.button_frame.pack()
        
        # Upload button
        self.upload_button = Button(self.button_frame, text = "Upload file", width=10, height=2)
        self.upload_button.pack(side=LEFT, padx=5, pady=5)

        
