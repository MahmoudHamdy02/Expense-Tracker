
class Department:
    """
    This class represents a department within a company.

    Attributes:
        departmentID (int): The ID of the department.
        departmentName (str): The name of the department.
    """

    def __init__(self, departmentID, departmentName):
        """
        Initialize a new Department instance with the given attributes.

        Args:
            departmentID (int): The ID of the department.
            departmentName (str): The name of the department.
        """
        self.departmentID = departmentID
        self.departmentName = departmentName
        self.expenses = []  # Initialize an empty list to store expenses

    def addExpense(self, amount, date, category)-> None:
        """
        Add an expense to the department.

        Args:
            amount (float): The amount of the expense.
            date (str): The date of the expense in YYYY-MM-DD format.
            category (str): The category of the expense.
        """
        self.expenses.append({"amount": amount, "date": date, "category": category})

    def view_department_expenses(self) -> list:
        """
        View all expenses associated with the department.
        """
        return self.expenses


    def generate_report(self) -> str:
        """
        Generate a report for the department, containing expense details.
        """
        report = f"Department Report: {self.departmentName}\n"
        report += "Expenses:\n"
        for expense in self.expenses:
            report += f"  - {expense['category']}: {expense['amount']} on {expense['date']}\n"

        return report










