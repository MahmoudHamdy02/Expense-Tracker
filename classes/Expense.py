class Expense:
    """
    This class represents an Expense

    Attributes:
        ExpenseID(int): The ID of the Expense
        name(string): The name of the Expense
        amount(float): The amount of the Expense
        category(string): The category the Expense belongs to
        date(date): The date the Expense

    """
    def __init__(self, amount, date, category, expenseID,name):
      self.amount = amount
      self.date = date
      self.category = category
      self.expenseID = expenseID