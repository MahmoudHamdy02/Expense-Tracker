import tkinter
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class PersonDashboard(ctk.CTkFrame):
    def __init__(self, master, Person):
        super().__init__(master)

        self.Person = Person

        
