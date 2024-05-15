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

    def addExpense(self, amount, date, category):

        """
        Add an expense to the project.

        Args:
            amount (float): The amount of the expense.
            date (str): The date of the expense in YYYY-MM-DD format.
            category (str): The category of the expense.
        """
        pass

    def editExpense(self, expenseID, newAmount, newDate):

        """
        Edit an existing expense in the project.

        Args:
            expenseID (int): The index of the expense to edit.
            newAmount (float): The new amount of the expense.
            newDate (str): The new date of the expense in YYYY-MM-DD format.
        """
        pass

    def viewProjectExpenses(self):
        """
        View all expenses associated with the project.
        """
        pass

