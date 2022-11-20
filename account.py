class Account:
    """
    A class representing details for an Account object
    """

    def __init__(self, name: str, balance=0.0) -> None:
        """
        Constructor to create initial
        state of an Account object
        :param name: string value
        :param balance: default
        account balance
        :return: None
        """
        self.__account_name: string = str(name)
        self.__account_balance: float = balance

    def is_float(self, amount: float) -> bool:
        """
        Function to check if a string
        can be converted to a float
        :param amount: string value
        :return: boolean True if
        amount can be converted to
        a float, else False
        """
        try:
            float(amount)
            return True
        except:
            return False

    def deposit(self, amount: float) -> bool:
        """
        Function to add amount
        to an account's balance
        :param amount: string value
        :return: boolean True if
        amount is added to account
        balance, else False
        """
        if self.is_float(f'{amount}'.strip()):
            amount = float(f'{amount}'.strip())
            if 0 < amount:
                self.__account_balance += round(amount, 2)
                return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to subtract amount
        from an account's balance
        :param amount: string value
        :return: boolean True if
        amount is subtracted from
        account balance, else False
        """
        if self.is_float(f'{amount}'.strip()):
            amount = float(f'{amount}'.strip())
            if 0 < amount <= self.__account_balance:
                self.__account_balance -= round(amount, 2)
                return True
        return False

    def get_balance(self) -> float:
        """
        Function to retrieve account's
        balance
        :return: Float account balance
        """
        return round(self.__account_balance, 2)

    def get_name(self) -> str:
        """
        Function to retrieve account's
        name
        :return: String account name
        """
        return self.__account_name
