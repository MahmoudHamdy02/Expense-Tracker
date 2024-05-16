import tkinter as tk
import customtkinter as ctk
from GUI.personDashboard import PersonDashboard
from GUI.companyDashboard import CompanyDashboard
from classes.Person import Person
from CTkMessagebox import CTkMessagebox

# List to store user credentials
user_database = []

class Login(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.signup_window = None
        frame = ctk.CTkFrame(self)
        frame.place(relx=0.5, rely=0.5, anchor="c")

        self.email_input = ctk.CTkEntry(frame, placeholder_text="email@test.com")
        self.email_input.pack(pady=5, expand=True, fill="none")

        self.password_input = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        self.password_input.pack(pady=5)

        logInButton = ctk.CTkButton(frame, text="Log In", command=self.login)
        logInButton.pack(pady=5)

        signupFrame = ctk.CTkFrame(frame)
        signupFrame.pack()

        personSignUpButton = ctk.CTkButton(signupFrame, text="Sign Up as a Person", command=self.signup_person)
        personSignUpButton.pack(side="left", padx=10, pady=10)

        companySignUpButton = ctk.CTkButton(signupFrame, text="Sign Up as a Company", command=self.signup_company)
        companySignUpButton.pack(side="left", padx=10)
    
    def login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        
        if not email or not password:
            CTkMessagebox(self, icon="warning", message="Please enter both email and password", title="Error")
            return
        
        # Check if the credentials are in the user_database
        if (email, password) not in user_database:
            CTkMessagebox(self, icon="warning", message="Please enter correct email and password or signup", title="Error")
            return
        self.destroy()
        
        if self.user_type == "Company":
            self.master.dashboard = CompanyDashboard(self.master)
        else:
            person = Person("John", "Doe", 1000.0, 200.0)
            self.master.dashboard = PersonDashboard(self.master, person)
        self.master.dashboard.grid(row=0, column=1, rowspan=4, sticky="nsew")
        

    def signup_person(self):
        self.signup("Person")
    
    def signup_company(self):
        self.signup("Company")
    
    def signup(self, user_type):
        self.user_type = user_type
        if self.signup_window is None or not self.signup_window.winfo_exists():
            self.signup_window = ctk.CTkToplevel(self)
            self.signup_window.attributes("-topmost", "true")
            self.signup_window.title(f"Sign Up as {user_type}")
            self.signup_window.geometry("400x300")

            frame = ctk.CTkFrame(self.signup_window)
            frame.pack(pady=20, padx=20)

            email_label = ctk.CTkLabel(frame, text="Email:")
            email_label.pack()
            email_entry = ctk.CTkEntry(frame)
            email_entry.pack()

            password_label = ctk.CTkLabel(frame, text="Password:")
            password_label.pack()
            password_entry = ctk.CTkEntry(frame, show="*")
            password_entry.pack()
        else:
            self.transactionFrame.focus()

        def submit_signup():
            email = email_entry.get()
            password = password_entry.get()

            if not email or not password:
                CTkMessagebox(self, icon="warning", message="Please fill out all fields", title="Error")
                return
            
            # Add the new user credentials to the user_database
            user_database.append((email, password))
            CTkMessagebox(self, icon="info", message=f"{user_type} account created successfully!", title="Success")
            self.signup_window.destroy()     
            

        signup_button = ctk.CTkButton(frame, text="Sign Up", command=submit_signup)
        signup_button.pack(pady=10)

# Example usage (within a Tkinter application):
if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("800x600")
    login_frame = Login(root)
    login_frame.pack(expand=True, fill="both")
    root.mainloop()
