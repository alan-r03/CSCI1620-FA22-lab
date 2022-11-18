class Account:

    def __init__(self, name):
        self.account_name = name
        self.account_balance = 0

    def is_float(self, amount):
        """
        Function to check if a string
        can be converted to a float
        :param amount: string value
        :return: boolean True if
        amount can be converted to
        a float, else False
        """
        try:
            float(amount.strip())
            return True
        except:
            return False

    def deposit(self, amount):
        """
        Function to add amount
        to an account's balance
        :param amount: string value
        :return: boolean True if
        amount is added to account
        balance, else False
        """
        if is_float(amount):
            amount = float(amount.strip())
            if 0 < amount:
                self.account_balance += amount
                return True
        return False

    def withdraw(self, amount):
        """
        Function to subtract amount
        from an account's balance
        :param amount: string value
        :return: boolean True if
        amount is subtracted from
        account balance, else False
        """
        if is_float(amount):
            amount = float(amount.strip())
            if 0 < amount <= self.account_balance:
                self.account_balance -= amount
                return True
        return False

    def get_balance(self):
        """
        Function to retrieve account's
        balance
        :return: Float account balance
        """
        return self.account_balance

    def get_name(self):
        """
        Function to retrieve account's
        name
        :return: String account name
        """
        return self.account_name