import User

class Person(User):
    """
    This is a class that represents a Person.
    \n
    Extends the User class.
 
    Attributes:
        firstName (string): First name of the person
        secondName (string): Second name of the person
        income (string): Monthly income of the person
        savings (string): Savings amount of the person
    """
    def __init__(self, firstName, secondName, income, savings):
        super().__init__()
        self.firstName = firstName
        self.secondName = secondName
        self.income = income
        self.savings = savings

    def addExpenses(self, amount, date, category):
        """
        Adds an expense for the person

        Args:
            amount: Expense amount
            date: Expense date
            category: Expense category
        """
        pass
    
    def viewExpenses(self):
        """
        Views all expenses for the person
        """
        pass

    def editExpense(self, expenseID, newAmount, newDate):
        """
        Edits details of an expense for the person

        Args:
            expenseID: Expense ID to be edited
            newAmount: New expense amount
            newDate: New expense date
        """
        pass

    def deleteExpense(self, expenseID):
        """
        Deletes an expense for the person

        Args:
            expenseID: Expense ID to be deleted
        """
        pass

    def viewSavings(self):
        """
        Views current savings amount of the person
        """
        pass