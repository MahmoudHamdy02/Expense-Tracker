from datetime import date
from classes.Category import Category
from classes.Expense import Expense

class Department:
    """
    This class represents a department within a company.

    Attributes:
        departmentID (int): The ID of the department.
        departmentName (str): The name of the department.
        expenses (list): A list to store department expenses.
    """

    def __init__(self, departmentID: int, departmentName: str):
        """
        Initialize a new Department instance with the given attributes.

        Args:
            departmentID (int): The ID of the department.
            departmentName (str): The name of the department.
        """
        self.departmentID = departmentID
        self.departmentName = departmentName
        self.expenses = []  # Initialize an empty list to store expenses

    def addExpense(self, amount:float, date:date, category: Category)-> None:
        """
        Add an expense to the department.

        Args:
            amount (float): The amount of the expense.
            date (date): The date of the expense in YYYY-MM-DD format.
            category (Category): The category of the expense.
        """
        self.expenses.append(Expense(category=category, amount=amount, date=date, expenseID=len(self.expenses)))

    def view_department_expenses(self) -> list:
        """
        View all expenses associated with the department.

        Returns:
            list: A list of all expenses associated with the department.
        """
        return self.expenses


    def generate_report(self) -> str:
        """
        Generate a report for the department, containing expense details.

        Returns:
            str: A report containing expense details for the department.
        """
        report = f"Department Report: {self.departmentName}\n"
        report += "Expenses:\n"
        for expense in self.expenses:
            report += f"  - {expense['category']}: {expense['amount']} on {expense['date']}\n"

        return report










