from classes.Budget import Budget
from classes.Category import Category

class User:
    """
    Represents a user of the Expense Tracker system.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
        budget (list): A list of budget limits set by the user.
    """

    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email
        self.budget = []

    def login(self, username: str, password: str):
        """
        Verifies correct username and password and logs the user in.

        Args:
            username (str): The input username.
            password (str): The input password.

        Returns:
            bool: True if the username and password are correct, False otherwise.
        """
        if username == self.username and password == self.password:
            return True
        return False

    def setBudget(self, category: Category, amount: int):
        """
        Sets a budget limit of a specific category.

        Args:
            category (Category): The category to set the budget limit for.
            amount (int): The budget limit amount.

        Returns:
            None
        """
        self.budget.append(Budget(amount, category))

