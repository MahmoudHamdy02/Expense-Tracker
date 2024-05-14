import tkinter
import tkinter.messagebox
import customtkinter as ctk
from GUI.personDashboard import PersonDashboard

class Login(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        frame = ctk.CTkFrame(self)
        frame.place(relx=0.5,rely=0.5,anchor="c")

        email_input = ctk.CTkEntry(frame, placeholder_text="email@test.com")
        email_input.pack(pady=5, expand=True, fill="none")

        password_input = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        password_input.pack(pady=5)

        logInButton = ctk.CTkButton(frame, text="Log In", command=self.login)
        logInButton.pack(pady=5)

        signupFrame = ctk.CTkFrame(frame)
        signupFrame.pack()

        personSignUpButton = ctk.CTkButton(signupFrame, text="Sign Up as a Person", command=self.signup)
        personSignUpButton.pack(side="left", padx=10, pady=10)

        companySignUpButton = ctk.CTkButton(signupFrame, text="Sign Up as a Company", command=self.signup)
        companySignUpButton.pack(side="left", padx=10)
    
    def login(self):
        print("login")
        self.destroy()
        self.master.dashboard = PersonDashboard(self.master, None)
        self.master.dashboard.grid(row=0, column=1, rowspan=4, sticky="nsew")

    
    def signup(self):
        print("sign up")
