import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.transactionFrame import TransactionFrame

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class CompanyDashboard(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.transactionFrame = None

        self.money = 3100
        self.noOfTransactions = 299

        self.summaryFrame = ctk.CTkFrame(self, height=100)
        self.summaryFrame.grid(row=0, column=0, sticky="nsew", padx = (10,10))
        self.summaryFrame.grid_columnconfigure((0,1,2,3),weight=1)
        self.summaryFrame.grid_rowconfigure((0,1), weight=1)

        self.sidebar_button_1 = ctk.CTkButton(master.sidebar_frame, text="Set Income",command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=(100,0))
        self.sidebar_button_2 = ctk.CTkButton(master.sidebar_frame,text="Make A Transaction", command=self.makeTransaction)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(master.sidebar_frame,text="Set Budget", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20)

        self.incomeLabel = ctk.CTkLabel(self.summaryFrame, text="Income", font=ctk.CTkFont(size=20, weight="bold"))
        self.incomeLabel.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")
        self.income = ctk.CTkLabel(self.summaryFrame, text="$193,540", font=ctk.CTkFont(size=20))
        self.income.grid(row=1, column=0, sticky="ew")

        self.expenseLabel = ctk.CTkLabel(self.summaryFrame, text="Expense", font=ctk.CTkFont(size=20, weight="bold"))
        self.expenseLabel.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")
        self.expense = ctk.CTkLabel(self.summaryFrame, text="$44,980", font=ctk.CTkFont(size=20))
        self.expense.grid(row=1, column=1, sticky="ew")

        self.balanceLabel = ctk.CTkLabel(self.summaryFrame, text="Balance", font=ctk.CTkFont(size=20, weight="bold"))
        self.balanceLabel.grid(row=0, column=2, padx=10, pady=(10, 10), sticky="ew")
        self.balance = ctk.CTkLabel(self.summaryFrame, text="$384,930", font=ctk.CTkFont(size=20))
        self.balance.grid(row=1, column=2, sticky="ew")

        self.transactionLabel = ctk.CTkLabel(self.summaryFrame, text="Transactions", font=ctk.CTkFont(size=20, weight="bold"))
        self.transactionLabel.grid(row=0, column=3, padx=10, pady=(10, 10), sticky="ew")
        self.transaction = ctk.CTkLabel(self.summaryFrame, text="1093", font=ctk.CTkFont(size=20))
        self.transaction.grid(row=1, column=3, sticky="ew")

        fig = plt.Figure(figsize=(10, 4), dpi=100)
        ax = fig.add_subplot(111)
        values = [15.76, 12.79, 10.93, 10.40, 8.87, 8.49, 7.59, 6.52, 5.92, 12.73]
        labels = ["Office Rent", "Marketing", "Utilities", "Bills", "R&D", "Logistics", "Insurance", "Health Care", "Salaries", "Others"]
        wedges, texts = ax.pie(values, labels=labels, wedgeprops=dict(width=0.3))
        ax.axis('equal')
        ax.legend(wedges, [f'{l} ({v}%)' for l, v in zip(labels, values)],
          title="Categories",
          loc="center left",
          bbox_to_anchor=(-0.1, 0, 0.5, 1))
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew", padx = (10,10))

        recent_expenses = [
            {"date": "05/01/2024", "category": "Office Supplies", "payment": "Debit Card", "description": "Printer toner cartridges", "amount": "$300", "type": "minus"},
            {"date": "05/05/2024", "category": "Software Subscription", "payment": "Credit Card", "description": "Annual Adobe Creative Cloud subscription", "amount": "$600", "type": "minus"},
            {"date": "05/10/2024", "category": "Travel", "payment": "Credit Card", "description": "Flight tickets for business conference", "amount": "$1500", "type": "minus"},
            {"date": "05/15/2024", "category": "Marketing", "payment": "Debit Card", "description": "Social media advertising campaign", "amount": "$1000", "type": "minus"},
            {"date": "05/20/2024", "category": "Equipment", "payment": "Cash", "description": "New laptops for employees", "amount": "$5000", "type": "minus"}
        ]
        # Define the column headers
        headers = ["Date", "Category", "Payment", "Description", "Amount"]

        # Create a new frame for the expenses
        expenses_frame = ctk.CTkFrame(self)
        expenses_frame.grid(row=2, column=0, sticky="nsw", padx=(10,10))
        expenses_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        expensesLabel = ctk.CTkLabel(expenses_frame, text="Recent Expenses: ", font=ctk.CTkFont(size=20, weight="bold"))
        expensesLabel.grid(row=0, column=0, padx=10, pady=(10, 10))
        # Add the column headers to the expenses frame
        for i, header in enumerate(headers):
            header_label = ctk.CTkLabel(expenses_frame, text=header, font=ctk.CTkFont(size=15, weight="bold"))
            header_label.grid(row=1, column=i, padx=10, pady=10)

        # Add the recent expenses to the expenses frame
        for i, expense in enumerate(recent_expenses, start=2):
            date_label = ctk.CTkLabel(expenses_frame, text=expense['date'])
            date_label.grid(row=i, column=0, padx=10)

            category_label = ctk.CTkLabel(expenses_frame, text=expense['category'])
            category_label.grid(row=i, column=1, padx=10)

            payment_label = ctk.CTkLabel(expenses_frame, text=expense['payment'])
            payment_label.grid(row=i, column=2, padx=10)

            description_label = ctk.CTkLabel(expenses_frame, text=expense['description'])
            description_label.grid(row=i, column=3, padx=10)

            # Set the color of the amount label based on the 'type' field
            amount_color = "green" if expense['type'] == "plus" else "red"
            amount_label = ctk.CTkLabel(expenses_frame, text=expense['amount'], text_color=amount_color)
            amount_label.grid(row=i, column=4, padx=10)


    def sidebar_button_event(self):
        print("sidebar_button click")

    def makeTransaction(self):
        if self.transactionFrame is None or not self.transactionFrame.winfo_exists():
            self.transactionFrame = TransactionFrame(self)
            self.transactionFrame.attributes("-topmost","true")
        else:
            self.transactionFrame.focus()

    def doneTransaction(self, amount):
        self.money -=amount
        self.noOfTransactions += 1
        self.balance.configure(text=f"{self.money}")
        self.transaction.configure(text=f"{self.noOfTransactions}")



