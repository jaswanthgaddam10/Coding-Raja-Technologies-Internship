import json
import os
from datetime import datetime
FILE = 'budget_data.json'
if not os.path.exists(FILE): json.dump([], open(FILE, 'w'))
def load_data(): return json.load(open(FILE))
def save_data(data): json.dump(data, open(FILE, 'w'))
def add_transaction(type, category, amount):
    data = load_data()
    data.append({'type': type, 'category': category, 'amount': amount, 'date': str(datetime.now())})
    save_data(data)
def calculate_budget():
    data = load_data()
    income = sum(item['amount'] for item in data if item['type'] == 'income')
    expenses = sum(item['amount'] for item in data if item['type'] == 'expense')
    return income - expenses
def analyze_expenses():
    data = load_data()
    categories = {}
    for item in data:
        if item['type'] == 'expense':
            if item['category'] in categories:
                categories[item['category']] += item['amount']
            else:
                categories[item['category']] = item['amount']
    return categories
def main():
    while True:
        print("1. Add Income\n2. Add Expense\n3. Calculate Budget\n4. Analyze Expenses\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            category = input("Income category: ")
            amount = float(input("Amount: "))
            add_transaction('income', category, amount)
            print("Income added.")
        elif choice == '2':
            category = input("Expense category: ")
            amount = float(input("Amount: "))
            add_transaction('expense', category, amount)
            print("Expense added.")
        elif choice == '3':
            print(f"Remaining budget: {calculate_budget()}")
        elif choice == '4':
            for category, amount in analyze_expenses().items():
                print(f"{category}: {amount}")
        elif choice == '5':
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
