from pathlib import Path
import csv

# Class to represent a bar tab for a specific table
class Bar_Tab():
    def __init__(self, table_number):
        # Initialize table number and tab details
        self.table_number = table_number
        self.drinks = []        # List to store drinks and their prices
        self.total = 0.0        # Total price of drinks
        self.tip = 0.0          # Tip amount
        self.grand_total = 0.0  # Total including tip

    # Method to interactively serve drinks to the user
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

            self.drinks.append((name, price))  # Add drink to the list

    # Method to calculate total, tip, and grand total
    def calculate_totals(self):
        self.total = sum(price for _, price in self.drinks)
        self.tip = self.total * 0.15  # Assuming a 15% tip
        self.grand_total = self.total + self.tip

    # Method to save the tab details to a CSV file
    def create_csv(self):
        if not self.drinks:
            print("No drinks to save.")
            return
        # Create the path for the CSV file in the same directory as this script
        path = Path(__file__).parent / f"table_{self.table_number}_tab.csv"
        

        # Open the CSV file for writing
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Drink Name", "Price"])
            for drink in self.drinks:
                writer.writerow(drink)
            writer.writerow([])
            writer.writerow(["Total", f"${self.total:.2f}"])
            writer.writerow(["Tip (15%)", f"${self.tip:.2f}"])
            writer.writerow(["Grand Total", f"${self.grand_total:.2f}"])
        print(f"Tab saved to {path}")

# Main function to run the bar tab app
def main():
    tab = Bar_Tab("4")  # Create a Bar_Tab instance for table 4
    print(f"Table Number: {tab.table_number}")
    tab.serve_user()          # Collect drink orders
    tab.calculate_totals()    # Calculate totals
    tab.create_csv()          # Save the tab to a CSV file
    return

# Entry point of the script
if __name__ == "__main__":
    main()