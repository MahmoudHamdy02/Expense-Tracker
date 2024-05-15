from datetime import date
from classes.Category import Category

class Expense:
    """
    This class represents an Expense

    Attributes:
        ExpenseID(int): The ID of the Expense
        name(string): The name of the Expense
        amount(float): The amount of the Expense
        category(Category): The category the Expense belongs to
        date(date): The date the Expense

    """
def __init__(self, amount: float, date: date, category: Category, expenseID:int):
    self.amount = amount
    self.date = date
    self.category = category
    self.expenseID = expenseID

def editExpense(self, amount: float, date: date):
    """
    Edit the details of an expense.

    Args:
        amount (float): The amount of the expense.
        date (str): The date of the expense in YYYY-MM-DD format.
    """
    self.amount = amount
    self.date = date

def getAmount(self):
    """
    Get the amount of the expense.

    Returns:
        float: The amount of the expense.
    """
    return self.amount