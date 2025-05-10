import csv
from datetime import datetime

def log_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., food, rent): ")
    description = input("Enter description: ")

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("✅ Expense logged.")

def main():
    while True:
        print("\n== Expense Tracker ==")
        print("1. Log new expense")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            log_expense()
        elif choice == "2":
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
