import tkinter
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class PersonDashboard(ctk.CTkFrame):
    def __init__(self, master, Person):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.summaryFrame = ctk.CTkFrame(self, height=100)
        self.summaryFrame.grid(row=0, column=0, sticky="nsew", padx = (10,10))
        self.summaryFrame.grid_columnconfigure((0,1,2,3),weight=1)
        self.summaryFrame.grid_rowconfigure((0,1), weight=1)

        self.Person = Person

        self.incomeLabel = ctk.CTkLabel(self.summaryFrame, text="Income", font=ctk.CTkFont(size=20, weight="bold"))
        self.incomeLabel.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")
        self.income = ctk.CTkLabel(self.summaryFrame, text="$43,300", font=ctk.CTkFont(size=20))
        self.income.grid(row=1, column=0, sticky="ew")

        self.expenseLabel = ctk.CTkLabel(self.summaryFrame, text="Expense", font=ctk.CTkFont(size=20, weight="bold"))
        self.expenseLabel.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")
        self.expense = ctk.CTkLabel(self.summaryFrame, text="$12,300", font=ctk.CTkFont(size=20))
        self.expense.grid(row=1, column=1, sticky="ew")

        self.balanceLabel = ctk.CTkLabel(self.summaryFrame, text="Balance", font=ctk.CTkFont(size=20, weight="bold"))
        self.balanceLabel.grid(row=0, column=2, padx=10, pady=(10, 10), sticky="ew")
        self.balance = ctk.CTkLabel(self.summaryFrame, text="$31,000", font=ctk.CTkFont(size=20))
        self.balance.grid(row=1, column=2, sticky="ew")

        self.transactionLabel = ctk.CTkLabel(self.summaryFrame, text="Transactions", font=ctk.CTkFont(size=20, weight="bold"))
        self.transactionLabel.grid(row=0, column=3, padx=10, pady=(10, 10), sticky="ew")
        self.transaction = ctk.CTkLabel(self.summaryFrame, text="20", font=ctk.CTkFont(size=20))
        self.transaction.grid(row=1, column=3, sticky="ew")



