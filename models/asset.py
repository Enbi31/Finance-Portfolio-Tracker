from abc import ABC , abstractmethod

class Asset(ABC):
    def __init__(self, share_name, symbol):
        self.share_name =  share_name
        self.symbol = symbol
    @abstractmethod    
    def get_value(self):
        pass
                
    def __str__(self):
        
        return f"the value of {self.share_name} is {self.get_value()}"    

class Stock(Asset):
    def __init__(self,share_name,symbol,quantity,buy_price):
        super().__init__(share_name,symbol)
        self.quantity=quantity
        self.buy_price=buy_price
    def get_value(self):
        return self.quantity*self.buy_price    

class Crypto(Asset):
    def __init__(self,coin_name,symbol,quantity,buy_price):
        super().__init__(coin_name,symbol)
        self.quantity=quantity
        self.buy_price=buy_price
    def get_value(self):
        return self.quantity*self.buy_price    

class Savings_Acc(Asset):
    def __init__(self, bank_name, symbol, principal, roi):
        super().__init__(bank_name, symbol)
        self._principal = principal
        self.roi = roi

    @property
    def principal(self):
        return self._principal        # read-only from outside

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        else:
            self._principal += amount  # _principal inside class

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        elif amount > self._principal:
            print("Cannot withdraw more than balance")
        else:
            self._principal -= amount  # actually subtract it

    def get_value(self):
        return self._principal * (1 + self.roi)