class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories_entered = 0

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})
        self.categories_entered += 1

    def get_total_expenses(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        return total_expenses

# Create an instance of ExpenseTracker
tracker = ExpenseTracker()

# Allow users to input expenses interactively for up to 6 categories
while tracker.categories_entered < 6:
    amount = float(input("Enter expense amount for category {}: ".format(tracker.categories_entered + 1)))
    category = input("Enter expense category: ")
    tracker.add_expense(amount, category)

# Display total monthly expenses
total_expenses = tracker.get_total_expenses()
print("\nTotal Monthly Expenses {:.2f}".format(total_expenses))