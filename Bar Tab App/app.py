from pathlib import Path
import csv
from platform import processor
from symtable import Class

#Class

class BarTab():
    def __init__(self,table_number):
        self.table_number = table_number
        self.drinks = []
        self.total = 0.0
        self.tip = 0.0
        self.grand_total = 0.0


# serve the customer
    def serve_customer(self ):
        while True:
            drink = input("Enter your drink (or 'q' to quit): ")
            if drink.lower() == 'q':
                break
            elif drink == '':
                print("drink cannot be empty")
                continue

            try:
                price= int(input("what is the price of the drink? "))
            except ValueError:
                print("please enter your drink and a valid price again: ")
                continue

            self.drinks.append((drink,price))



# calculate the totals
    def calculate_totals(self):
        self.total = sum(price for _, price in self.drinks)
        self.tip = self.total * 0.20
        self.grand_total = self.total + self.tip


# create csv file path
    def create_csv(self):
        if not self.drinks:
            return
        path = Path(__file__).parent / f"table{self.table_number}.csv"
        with path.open("w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["drink","price"])

            for drink,price in self.drinks:
                writer.writerow([drink,price])
            writer.writerow(["Total ", f"{self.total:.2f}"])
            writer.writerow(["Tip ", f"{self.tip:.2f}"])
            writer.writerow(["Grand Total ", f"{self.grand_total:.2f}"])




# main func
def main():

    table_one = BarTab(1)
    table_one.serve_customer()
    table_one.calculate_totals()
    table_one.create_csv()
    return


# entry point of the script
if __name__ == "__main__":
    main()
