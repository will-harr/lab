class Account:
    def __init__(self, name: str) -> None:
        '''
        :param name: name of the account
        :param account_balance: amount of money in the account
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        method deposits money into an account object
        
        :param amount: the numerical amount to deposit into the account object
        :return: True if deposit successful, false otherwise
        '''
        if amount > 0:
            self.__account_balance += amount
            return True

        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        method withdraws money from an account object
        
        :param amount: numerical amount to withdraw from the account object
        :return: True if withdraw successful, false otherwise
        '''
        if (amount > 0) and (amount <= self.__account_balance):
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        :return: the account balance
        '''
        return self.__account_balance

    def get_name(self) -> float:
        '''
        :return: the account name
        '''
        return self.__account_name
