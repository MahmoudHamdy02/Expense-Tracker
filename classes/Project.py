from datetime import date
from classes.Expense import Expense
from classes.Category import Category
class Project:

    """
    class to represent a project within a coompany

    Attributes:
        projectName (str): The name of the project.
        projectID (int): The unique identifier of the project.
        startDate (date): The start date of the project in YYYY-MM-DD format.
        endDate (date): The end date of the project in YYYY-MM-DD format.
        expenses (list): A list to store project expenses.
    """
    def __init__(self, projectName: str, projectID: int, startDate: date, endDate: date):
        self.projectName = projectName
        self.projectID = projectID
        self.startDate = startDate
        self.endDate = endDate
        self.expenses = []  # Initialize an empty list to store expenses

    def add_expense(self, amount: float, date: str, category: Category) -> None:
        """
        Add an expense to the project.

        Args:
            amount (float): The amount of the expense.
            date (date): The date of the expense in YYYY-MM-DD format.
            category (Category): The category of the expense.
        """
        self.expenses.append(Expense(category=category, amount=amount, date=date, expenseID=len(self.expenses)))

    def edit_expense(self, expense_id: int, new_amount: float, new_date: date) -> None:
        """
        Edit an existing expense in the project.

        Args:
            expense_id (int): The index of the expense to edit.
            new_amount (float): The new amount of the expense.
            new_date (date): The new date of the expense in YYYY-MM-DD format.
        """
        if expense_id < len(self.expenses):
            self.expenses[expense_id].editExpense(amount=new_amount, date=new_date)


    def view_project_expenses(self) -> list:
        """
        View all expenses associated with the project.
        """
        return self.expenses
