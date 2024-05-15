from classes.User import User
from classes.Expense import Expense

class Person(User):
    """
    This is a class that represents a Person.
    
    Extends the User class.

    Attributes:
        firstName (string): First name of the person
        secondName (string): Second name of the person
        income (string): Monthly income of the person
        savings (string): Savings amount of the person
    """
    def __init__(self, first_name: str, second_name: str, income: float, savings: float):
        super().__init__("person", "password", "email")  # Initialize User attributes
        self.first_name = first_name
        self.second_name = second_name
        self.income = income
        self.savings = savings
        self.expenses = []  # Store expenses in a list

    def addExpenses(self, amount, date, category) -> None:
        """
        Adds an expense for the person

        Args:
            amount: Expense amount
            date: Expense date
            category: Expense category
        """
        self.expenses.append(Expense(category=category, amount=amount, date=date, expenseID=len(self.expenses)))

    def viewExpenses(self):
        """
        Views all expenses for the person
        """
        return self.expenses

    def editExpense(self, expenseID, newAmount, newDate) -> None:
        """
        Edits details of an expense for the person

        Args:
            expenseID: Expense ID to be edited
            newAmount: New expense amount
            newDate: New expense date
        """
        if expenseID < len(self.expenses):
            self.expenses[expenseID].editExpense(amount=newAmount, date=newDate)


    def deleteExpense(self, expenseID: int) -> None:
            """
            Deletes an expense for the person

            Args:
                expenseID (int): The ID of the expense to be deleted

            Returns:
                None
            """
            self.expenses = [expense for expense in self.expenses if expense["expense_id"] != expenseID]
        

    def viewSavings(self)-> float:
        """
        Views current savings amount of the person
        """
        return self.savings
        










