from models.asset import Asset
import json
import os

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

    def save(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        os.makedirs(data_dir, exist_ok=True)
        filename = os.path.join(data_dir, "portfolio.json")
        
        data = {
            "owner": self.owner_name,
            "net_worth": self.get_net_worth(),
            "assets": [
                {
                    "type": type(asset).__name__,
                    "name": asset.share_name,
                    "value": asset.get_value()
                }
                for asset in self._asset
            ]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Portfolio saved.")