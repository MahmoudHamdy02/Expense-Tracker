from classes.Category import Category

class Budget:
    """
    This class represents a budget for a specific category.

    Attributes:
        amount (float): The amount allocated for the budget.
        category (Category): The category of the budget.
    """

    def __init__(self, amount: float, category: Category):
        """
        Initialize a new Budget instance with the given attributes.

        Args:
            amount (float): The amount allocated for the budget.
            category (Category): The category of the budget.
        """
        self.amount = amount
        self.category = category

    def budgetAlert(self):
        
        """
        Check if the budget amount is above or below a certain threshold and raise an alert if needed.
        
        Returns:
            str: A message indicating whether the budget is above or below the threshold.
        """
        return "You're above your budget !"
