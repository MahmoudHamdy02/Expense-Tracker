import tkinter
import tkinter.messagebox
import customtkinter as ctk

class Login(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self._border_color = "green"
        self._border_width = 5

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
    
    def signup(self):
        print("sign up")
