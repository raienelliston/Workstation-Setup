from modules.application_opener import open_application
from modules.browser_opener import open_browser
from modules.config_editor import ConfigEditor
import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class Main_Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        button = customtkinter.CTkButton(master=self, text="Helo Word")
        button.pack(pady=10, padx=10)

        # All the dirrent load states
        for state in ConfigEditor.get_states():
            None # Add the large tiles to repersent states

        # All overlay static buttons
        edit_button = customtkinter.CTkButton(master=self, text="Edit")
        edit_button.pack(pady=10, padx=10)
        edit_button.tkraise()

        edit_universals = customtkinter.CTkButton(master=self, text="Edit Universals")
        edit_universals.pack(pady=10, padx=10)
        edit_universals.tkraise()

        settings_button = customtkinter.CTkButton(master=self, text="Settings")
        settings_button.pack(pady=10, padx=10)
        settings_button.tkraise()

def main():
    window = Main_Window()
    window.mainloop()

main()