from modules.application_opener import open_application
from modules.config_editor import ConfigEditor
import tkinter as tk
from tkinter import ttk
import customtkinter as CTk

CTk.set_appearance_mode("System")
CTk.set_default_color_theme("blue")

settings = ConfigEditor("settings.cfg")

class Main_Window(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):

        s = ttk.Style()

        s.configure('State_Frames.TFrame', background='red')

        main_frame = ttk.Frame(master=self, style='State_Frames.TFrame', padding=10, relief="solid", borderwidth=1)
        main_frame.pack(fill="both", padx=10, pady=10)

        button = CTk.CTkButton(master=self, text="Helo Word")
        button.pack(pady=10, padx=10)

        # Testing frames
        
        test_label = CTk.CTkLabel(main_frame, text="Test Label")
        test_label.pack(pady=10, padx=10)

        test_button = CTk.CTkButton(main_frame, text="Test Button")
        test_button.pack(pady=10, padx=10)

        # All the dirrent load states
        for state in settings.get_config("states"):
            None # Add the large tiles to repersent states

        # All overlay static buttons
        edit_button = CTk.CTkButton(master=self, text="Edit")
        edit_button.pack(pady=10, padx=10, side="left")
        edit_button.tkraise()

        edit_universals = CTk.CTkButton(master=self, text="Edit Universals")
        edit_universals.pack(pady=10, padx=10, side="left")
        edit_universals.tkraise()

        settings_button = CTk.CTkButton(master=self, text="Settings")
        settings_button.pack(pady=10, padx=10, side="left")
        settings_button.tkraise()

def main():
    window = Main_Window()
    window.mainloop()

main()