
class Project:

    """
    class to represent a project within a coompany

    Attributes:
        projectName (str): The name of the project.
        projectID (int): The unique identifier of the project.
        startDate (str): The start date of the project in YYYY-MM-DD format.
        endDate (str): The end date of the project in YYYY-MM-DD format.
        expenses (list): A list to store project expenses.
    """
    def __init__(self, projectName, projectID, startDate, endDate):
        self.projectName = projectName
        self.projectID = projectID
        self.startDate = startDate
        self.endDate = endDate
        self.expenses = []  # Initialize an empty list to store expenses

    def add_expense(self, amount: float, date: str, category: str) -> None:
        """
        Add an expense to the project.

        Args:
            amount (float): The amount of the expense.
            date (str): The date of the expense in YYYY-MM-DD format.
            category (str): The category of the expense.
        """
        self.expenses.append({"amount": amount, "date": date, "category": category})

    def edit_expense(self, expense_id: int, new_amount: float, new_date: str) -> None:
        """
        Edit an existing expense in the project.

        Args:
            expense_id (int): The index of the expense to edit.
            new_amount (float): The new amount of the expense.
            new_date (str): The new date of the expense in YYYY-MM-DD format.
        """
        if expense_id < len(self.expenses):
            self.expenses[expense_id]["amount"] = new_amount
            self.expenses[expense_id]["date"] = new_date


    def view_project_expenses(self) -> list:
        """
        View all expenses associated with the project.
        """
        return self.expenses
