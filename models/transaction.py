from datetime import datetime

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
