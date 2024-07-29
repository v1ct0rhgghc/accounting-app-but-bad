class Person:
    def __init__(self, name):
        self.name = name
        self.payments = []
        self.expenses = []

    def add_payment(self, amount, description):
        self.payments.append({"amount": amount, "description": description})
        print(f"Payment of {amount} for '{description}' added for {self.name}.")

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})
        print(f"Expense of {amount} for '{description}' added for {self.name}.")

    def view_transactions(self):
        print(f"Transactions for {self.name}:")
        print("Payments:")
        for i, payment in enumerate(self.payments, 1):
            print(f"{i}. {payment['description']}: {payment['amount']}")
        print("Expenses:")
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. {expense['description']}: {expense['amount']}")

class Accounting:
    def __init__(self):
        self.people = {}
        self.general_expenses = []

    def add_person(self, name):
        if name in self.people:
            print(f"Person '{name}' already exists.")
        else:
            self.people[name] = Person(name)
            print(f"Person '{name}' added.")

    def add_payment(self, name, amount, description):
        if name in self.people:
            self.people[name].add_payment(amount, description)
        else:
            print(f"Person '{name}' not found.")

    def add_expense(self, name, amount, description):
        if name in self.people:
            self.people[name].add_expense(amount, description)
        else:
            print(f"Person '{name}' not found.")

    def add_general_expense(self, amount, description):
        self.general_expenses.append({"amount": amount, "description": description})
        print(f"General expense of {amount} for '{description}' added.")

    def view_all_transactions(self):
        for person in self.people.values():
            person.view_transactions()
        print("General Expenses:")
        for i, expense in enumerate(self.general_expenses, 1):
            print(f"{i}. {expense['description']}: {expense['amount']}")

# Example usage
def main():
    accounting = Accounting()
    while True:
        print("\n1. Add Person\n2. Add Payment\n3. Add Expense\n4. Add General Expense\n5. View All Transactions\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the person's name: ")
            accounting.add_person(name)
        elif choice == '2':
            name = input("Enter the person's name: ")
            amount = float(input("Enter the payment amount: "))
            description = input("Enter the payment description: ")
            accounting.add_payment(name, amount, description)
        elif choice == '3':
            name = input("Enter the person's name: ")
            amount = float(input("Enter the expense amount: "))
            description = input("Enter the expense description: ")
            accounting.add_expense(name, amount, description)
        elif choice == '4':
            amount = float(input("Enter the general expense amount: "))
            description = input("Enter the general expense description: ")
            accounting.add_general_expense(amount, description)
        elif choice == '5':
            accounting.view_all_transactions()
        elif choice == '6':
            print("Exiting the accounting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
