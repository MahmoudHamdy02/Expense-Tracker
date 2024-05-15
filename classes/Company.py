import User

class Company(User):
    """
    This is a class that represents a Company.
    Extends the User class.
 
    Attributes:
        companyName (string): Name of the company
        bills (list): List of bills for the company
    """

    def __init__(self, companyName: str):
        super().__init__()
        self.companyName = companyName
        bills = []

    def viewCompanyBills(self):
        """
        Prints a list of bills for the company
        """
        for bill in self.bills:
            print(bill)

    def setSalary(self, employeeID:int, amount: float):
        """
        Sets the salary for the company's employees

        Parameters:
            employeeID (int): The ID of the employee
            amount (float): The salary amount to be set
        """
        employee = self.employees[employeeID]
        employee.setSalary(amount)