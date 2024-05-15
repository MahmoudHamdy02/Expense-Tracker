import datetime
from classes.Category import Category
class Transaction:
    """
    This class represents a transaction made by the user.

    Attributes:
        amount (float): The amount to be transferred.
        timestamp (datetime): The timestamp of the transaction.
        type (str): The type of transaction.
        transactionID (int): The id of the transaction.
        category (Category): The category the transaction belongs to.
        description (str): Description or note for the transaction.
    """

    def __init__(
        self,
        amount: float,
        timestamp: datetime,
        type: str,
        transactionID: int,
        category: Category,
        description: str = ""
    ):
        self.amount = amount
        self.timestamp = timestamp
        self.type = type
        self.transactionID = transactionID
        self.category = category
        self.description = description

    def view_transactions(self) -> None:
        """
        View the details of the transaction.
        """
        print(f"Transaction ID: {self.transactionID}")
        print(f"Amount: {self.amount}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Type: {self.type}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")

    def send(self, amount: float, description: str, category: Category) -> None:
        """
        Make a transaction.

        Args:
            amount (float): The amount of money to send.
            description (str): Description or note for the transaction.
            category (Category): The category of the transaction.
        """
        self.amount = amount
        self.timestamp = datetime.now()
        self.type = "send"
        self.category = category
        self.description = description

    def receive(self, amount: float, description: str) -> None:
        """
        Receive a transaction.

        Args:
            amount (float): The amount of money received.
            description (str): Description or note for the transaction.
        """
        self.amount = amount
        self.timestamp = datetime.now()
        self.type = "receive"
        self.category = Category("income")
        self.description = description