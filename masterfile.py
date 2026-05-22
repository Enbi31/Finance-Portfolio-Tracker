from abc import ABC , abstractmethod
from datetime import datetime


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

class Portfolio:
    def __init__(self ,owner_name):
        self.owner_name=owner_name
        self._asset =[]
        
    def add_asset(self,asset):
        self._asset.append(asset)    

    def get_net_worth(self):
        x =0
        for asset in self._asset:
            x += asset.get_value()
        return x

    def __str__(self):
        return f"the total networth of {self.owner_name} is {self.get_net_worth():,.2f}"

class Transaction:
    def __init__(self, asset_name, action, quantity, price):
        self.asset_name = asset_name
        self.action = action
        self.quantity = quantity
        self.price = price
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp.date()}] {self.action} {self.quantity} {self.asset_name} @ ₹{self.price}"

class TransactionHistory:
    def __init__(self):
        self._records = []          

    def log(self, transaction):
        self._records.append(transaction)

    def __len__(self):
        return len(self._records)

    def __iter__(self):
        return iter(self._records)

    def __str__(self):
        result = ""
        for txn in self._records:
            result += str(txn)+"\n"
        return result
