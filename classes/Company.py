import User

class Company(User):
    """
    This is a class that represents a Company.
    \n
    Extends the User class.
 
    Attributes:
        companyName (string): Name of the company
    """
    def __init__(self, companyName):
        super().__init__()
        self.companyName = companyName

    def viewCompanyBills(self):
        """
        Prints a list of bills for the company
        """
        pass

    def setSalary(self):
        """
        Sets the salary for the company's employees
        """
        pass