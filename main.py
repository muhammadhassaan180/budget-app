# freeCodeCamp python-v9 — Certification Project
# Build a Budget App
# My code goes below.
class Category:
    def __init__(self, name):
        self.name= name
        self.ledger= []

    def __str__(self):
        title = self.name.center(30, '*')
        rows = ''
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7]
            rows += f"{description:<23}{amount:>7}\n"
        return f"{title}\n{rows}Total: {self.get_balance():.2f}"
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        
        return False

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

def create_spend_chart(categories):
    category_withdrawals = []
    total_spent = 0
    
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        category_withdrawals.append(spent)
        total_spent += spent

    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        percentages = [int((amount / total_spent) * 100 // 10) * 10 for amount in category_withdrawals]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)
    
    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += f"{name[i]}  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"

    return chart

print(food)

auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(15, 'repair')

print(create_spend_chart([food, clothing, auto]))