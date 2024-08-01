import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name):
        self.name = name
        self.payments = []
        self.expenses = []

    def add_payment(self, amount, description):
        self.payments.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def view_transactions(self):
        transactions = f"Transactions for {self.name}:\nPayments:\n"
        for i, payment in enumerate(self.payments, 1):
            transactions += f"{i}. {payment['description']}: {payment['amount']}\n"
        transactions += "Expenses:\n"
        for i, expense in enumerate(self.expenses, 1):
            transactions += f"{i}. {expense['description']}: {expense['amount']}\n"
        return transactions

class Accounting:
    def __init__(self):
        self.people = {}
        self.general_expenses = []

    def add_person(self, name):
        if name in self.people:
            return False
        else:
            self.people[name] = Person(name)
            return True

    def add_payment(self, name, amount, description):
        if name in self.people:
            self.people[name].add_payment(amount, description)
            return True
        else:
            return False

    def add_expense(self, name, amount, description):
        if name in self.people:
            self.people[name].add_expense(amount, description)
            return True
        else:
            return False

    def add_general_expense(self, amount, description):
        self.general_expenses.append({"amount": amount, "description": description})

    def view_all_transactions(self):
        all_transactions = ""
        for person in self.people.values():
            all_transactions += person.view_transactions() + "\n"
        all_transactions += "General Expenses:\n"
        for i, expense in enumerate(self.general_expenses, 1):
            all_transactions += f"{i}. {expense['description']}: {expense['amount']}\n"
        return all_transactions

class AccountingApp:
    def __init__(self, root):
        self.accounting = Accounting()
        self.root = root
        self.root.title("Accounting App")

        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.amount_label = tk.Label(root, text="Amount")
        self.amount_label.grid(row=1, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)

        self.desc_label = tk.Label(root, text="Description")
        self.desc_label.grid(row=2, column=0)
        self.desc_entry = tk.Entry(root)
        self.desc_entry.grid(row=2, column=1)

        self.add_person_button = tk.Button(root, text="Add Person", command=self.add_person)
        self.add_person_button.grid(row=3, column=0)

        self.add_payment_button = tk.Button(root, text="Add Payment", command=self.add_payment)
        self.add_payment_button.grid(row=3, column=1)

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=3, column=2)

        self.add_general_expense_button = tk.Button(root, text="Add General Expense", command=self.add_general_expense)
        self.add_general_expense_button.grid(row=4, column=0)

        self.view_transactions_button = tk.Button(root, text="View All Transactions", command=self.view_transactions)
        self.view_transactions_button.grid(row=4, column=1)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=5, column=0, columnspan=3)

    def add_person(self):
        name = self.name_entry.get()
        if self.accounting.add_person(name):
            messagebox.showinfo("Success", f"Person '{name}' added.")
        else:
            messagebox.showwarning("Warning", f"Person '{name}' already exists.")
        self.clear_entries()

    def add_payment(self):
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        description = self.desc_entry.get()
        if amount.isdigit():
            if self.accounting.add_payment(name, float(amount), description):
                messagebox.showinfo("Success", f"Payment of {amount} for '{description}' added for {name}.")
            else:
                messagebox.showwarning("Warning", f"Person '{name}' not found.")
        else:
            messagebox.showerror("Error", "Invalid amount.")
        self.clear_entries()

    def add_expense(self):
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        description = self.desc_entry.get()
        if amount.isdigit():
            if self.accounting.add_expense(name, float(amount), description):
                messagebox.showinfo("Success", f"Expense of {amount} for '{description}' added for {name}.")
            else:
                messagebox.showwarning("Warning", f"Person '{name}' not found.")
        else:
            messagebox.showerror("Error", "Invalid amount.")
        self.clear_entries()

    def add_general_expense(self):
        amount = self.amount_entry.get()
        description = self.desc_entry.get()
        if amount.isdigit():
            self.accounting.add_general_expense(float(amount), description)
            messagebox.showinfo("Success", f"General expense of {amount} for '{description}' added.")
        else:
            messagebox.showerror("Error", "Invalid amount.")
        self.clear_entries()

    def view_transactions(self):
        transactions = self.accounting.view_all_transactions()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, transactions)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountingApp(root)
    root.mainloop()
