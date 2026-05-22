from models.asset import Stock, Crypto, Savings_Acc
from models.portfolio import Portfolio
from models.transaction import Transaction, TransactionHistory

def main():
    p = Portfolio("Naman")
    history = TransactionHistory()

    while True:
        print("\n--- Finance Tracker ---")
        print("1. Add Stock")
        print("2. Add Crypto")
        print("3. Add Savings Account")
        print("4. View Net Worth")
        print("5. View All Transactions")
        print("6. Save Portfolio")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            name = input("Stock name: ")
            symbol = input("Symbol: ")
            qty = int(input("Quantity: "))
            price = float(input("Buy price: "))
            stock = Stock(name, symbol, qty, price)
            p.add_asset(stock)
            history.log(Transaction(name, "BUY", qty, price))
            print(f"✅ Added {name} to portfolio")

        elif choice == "2":
            name = input("coin name: ")
            symbol = input("Symbol: ")
            qty = int(input("Quantity: "))
            price = float(input("Buy price: "))
            crypto = Crypto(name, symbol, qty, price)
            p.add_asset(crypto)
            history.log(Transaction(name, "BUY", qty, price))
            print(f"✅ Added {name} to portfolio")
            

        elif choice == "3":
            name = input("bank name: ")
            symbol = input("Symbol: ")
            principal = int(input("Principal: "))
            roi = float(input("ROI: "))
            bank = Savings_Acc(name, symbol, principal, roi)
            p.add_asset(bank)
            history.log(Transaction(name, "DEPOSIT", principal, roi))
            print(f"✅ Added {name} to portfolio")

        elif choice == "4":
            print(p)

        elif choice == "5":
            if len(history) == 0:
                print("No transactions yet")
            else:
                print(f"\nTotal transactions: {len(history)}")
                for txn in history:
                    print(txn)

        elif choice == "6":
            p.save()

        elif choice == "7":
            print("Goodbye!")
            break    
        else:
            print("Invalid option. Choose 1-6")

main() 