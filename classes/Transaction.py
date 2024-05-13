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
    



    def __init__(self, amount, timestamp, type, transactionID, category):
        self.amount = amount
        self.timestamp = timestamp
        self.type = type
        self.transactionID = transactionID
        self.category = category

    def viewTransactions(self):
        """
        view all transactions made by the user
        """
        pass

    def send(self, amount, description, category):
        """
        make a transaction

         Args:
            amount (float): The amount of money to send.
            description (str): Description or note for the transaction.
            category (str): The category of the transaction.
        
        """
        pass

    def recieve(self, amount, description):
        """
        recieve a transaction

        Args:
            amount (float): The amount of money received.
            description (str): Description or note for the transaction.
        """
        pass

