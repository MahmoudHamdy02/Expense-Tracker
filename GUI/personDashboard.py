import tkinter
import tkinter.messagebox
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.transactionFrame import TransactionFrame

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class PersonDashboard(ctk.CTkScrollableFrame):
    def __init__(self, master, Person):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.summaryFrame = ctk.CTkFrame(self, height=100)
        self.summaryFrame.grid(row=0, column=0, sticky="nsew", padx = (10,10))
        self.summaryFrame.grid_columnconfigure((0,1,2,3),weight=1)
        self.summaryFrame.grid_rowconfigure((0,1), weight=1)

        self.Person = Person

        self.sidebar_button_1 = ctk.CTkButton(master.sidebar_frame, text="Set Income",command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=(100,0))
        self.sidebar_button_2 = ctk.CTkButton(master.sidebar_frame,text="Make A Transaction", command=self.makeTransaction)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(master.sidebar_frame,text="Set Budget", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20)

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

        fig = plt.Figure(figsize=(10, 4), dpi=100)
        ax = fig.add_subplot(111)
        values = [15.76, 12.79, 10.93, 10.40, 8.87, 8.49, 7.59, 6.52, 5.92, 12.73]
        labels = ["Mortgage/Rent", "Food", "Utilities", "Bills", "Shopping", "Transport", "Insurance", "Health Care", "Clothing", "Others"]
        wedges, texts = ax.pie(values, labels=labels, wedgeprops=dict(width=0.3))
        ax.axis('equal')
        ax.legend(wedges, [f'{l} ({v}%)' for l, v in zip(labels, values)],
          title="Categories",
          loc="center left",
          bbox_to_anchor=(-0.1, 0, 0.5, 1))
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew", padx = (10,10))

    def sidebar_button_event(self):
        print("sidebar_button click")

    def makeTransaction(self):
        self.transactionFrame = TransactionFrame(self)



