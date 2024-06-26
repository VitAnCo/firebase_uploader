from view.main_view import MainView
from view.add_file_view import AddFileView
from model.firebase_handler import FirebaseHandler
from tkinter import messagebox
import threading


class MainController:
    def __init__(self) -> None:
        self.view = MainView() 
        self.model = FirebaseHandler()
        self.bind()
        self.filename = "None"

    def bind(self):
        self.view.addfile_button.bind("<ButtonRelease-1>", lambda e:self.add_file())
        self.view.upload_button.bind("<ButtonRelease-1>", lambda e:threading.Thread(target=self.upload_file).start())


    def add_file(self):
        self.file_view = AddFileView()
        self.filename=self.file_view.get_file_name()
        if self.filename == "":
            self.filename = "None"
            
        self.view.file_link.set(self.filename)
        pass

    def upload_file(self):
        self.view.upload_button['state'] = "disable"
        if (self.filename != "None"):
            self.view.progress_bar.config(mode="indeterminate")
            self.view.progress_bar.start(10)
            self.model.file_to_firebase(self.filename, self.view.nodeid.get())
            self.view.progress_bar.stop()
            self.view.upload_button['state'] = "normal"
            self.view.progress_bar.config(mode="determinate")
            messagebox.showinfo("Success", f"Upload {self.filename} success !")
        else:
            messagebox.showerror("Error", "Please choose file to upload !")
        

   
