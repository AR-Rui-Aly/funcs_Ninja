from pathlib import Path
import csv


class Bar_Tab():
    def __init__(self, table_number):
        self.table_number = table_number
        self.drinks = []
        self.total = 0.0
        self.tip = 0.0
        self.grand_total = 0.0

    def serve_user(self):
        while True:
            name = input("Enter drink name (or 'done' to finish): ")
            if name.lower() == 'done':
                break

            try:
                price = float(input("Enter drink price: "))
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue 

            self.drinks.append((name, price))




        
def main():
    tab = Bar_Tab("4")
    print(f"Table Number: {tab.table_number}")
    tab.serve_user()
    print(tab.drinks)
    return




if __name__ == "__main__":
    main()