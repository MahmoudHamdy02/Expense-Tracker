from classes.Expense import Expense

class Category:
    """
    This is a class that represents a category where you can add your expenses 

    Attributes:
        name(string): The name of the category
        description(string): The description of the category
        expenses(list): A list to store category expenses
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.expenses = []  # Initialize an empty list to store expenses

    def calculate_total_expenses(self) -> float:
        """
        This function calculates the total expense for each category

        Returns:
            float: The total expense for the category
        """
        return sum(expense.getAmount() for expense in self.expenses)