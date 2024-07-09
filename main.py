from modules.application_opener import open_application
from modules.browser_opener import open_browser
from modules.config_editor import ConfigEditor

import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Main_Window(customtkinter.CTk()):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("400x200")

    def create_widgets(self):
        None

        # label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
        # label_1.pack(pady=10, padx=10)

def main():
    window = Main_Window()
    window.mainloop()

main()