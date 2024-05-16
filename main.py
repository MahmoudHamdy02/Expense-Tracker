import os
from GUI.login import Login
import tkinter.messagebox
import customtkinter
from PIL import Image


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Expense Tracker App")
        self.geometry(f"{1100}x{580}")
        self.iconbitmap(os.path.join("GUI", "images", "accounting.ico"))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((2, 6), weight=1)
        self.logoImage = customtkinter.CTkImage(light_image=Image.open(os.path.join("GUI", "images", "accounting.png")), size=(80,80))
        self.logoImageLabel = customtkinter.CTkLabel(self.sidebar_frame, image=self.logoImage, text="")
        self.logoImageLabel.grid(row=0, column=0, padx=20, pady=(20, 0))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Expense Tracker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        self.loginFrame = Login(self)
        self.loginFrame.grid(row=0, column=1, rowspan=4, sticky="nsew")



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == '__main__':
    main = MainWindow()
    main.mainloop()
