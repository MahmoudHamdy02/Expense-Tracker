class User:
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def login(self, username, password):
        """
        Verifies correct username and password and logs the user in

        Args:
            username: Input username
            password: Input password
        """
        if username == self.username and password == self.password:
            return True
        return False

    def setBudget(self, category, amount):
        """
        Sets a budget limit of a specific category

        Args:
            category: Category to set limit of
            amount: Budget limit amount
        """
        pass

