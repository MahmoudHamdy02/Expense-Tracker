import datetime
from classes.Category import Category

class Transaction:
    """
    This class represents A transaction made by the user

    Attributes:
        transactionID(int): The id of the transaction
        amount(float): The amount to be transferred
        timestamp(datetime): The timestamp of the transaction
        type(string): The type of transaction
        category(string): The category the transaction belongs to
    """
    def __init__(
            self, 
            amount: int, 
            timestamp: datetime, 
            type: str, 
            transactionID: int, 
            category: Category
            ):
        self.amount = amount
        self.timestamp = timestamp
        self.type = type
        self.transactionID = transactionID
        self.category = category

    def view_transactions(self) -> None:
        """
        View the transactions made by the user
        """
        print(f"Transaction ID: {self.transactionID}")
        print(f"Amount: {self.amount}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Type: {self.type}")
        print(f"Category: {self.category}\n")
        print(f"Description: {self.description}\n")

    def send(self, amount: float, description: str, category: str) -> None:
        """
        Make a transaction

        Args:
            amount (float): The amount of money to send.
            description (str): Description or note for the transaction.
            category (str): The category of the transaction.
        """
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.type = "send"
        self.category = category
        self.description = description

    def receive(self, amount: float, description: str) -> None:
        """
        Receive a transaction

        Args:
            amount (float): The amount of money received.
            description (str): Description or note for the transaction.
        """
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.type = "receive"
        self.category = "income"
        self.description = description