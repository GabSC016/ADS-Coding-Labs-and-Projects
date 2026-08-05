# Project: Build a Budget App
# In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
    
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__ (self):
        final = ''

        title = f'{self.name.center(30,"*")}\n'
        final += title

        for transaction in self.ledger:

            description = f"{transaction['description']}"
            description = description[:23]

            amount = f"{transaction['amount']:.2f}"

            final += f'{description.ljust(23) + amount.rjust(7)}\n'

        total = f'Total: {self.get_balance():.2f}'
        final += total
        return final
        

def create_spend_chart(categories):
    # Total withdrawals
    total_withdrawals = []
    for category in categories:
        total_withdrawals_category = 0
        for withdrawal in category.ledger:
            if withdrawal['amount'] < 0:
                total_withdrawals_category += withdrawal['amount']
        total_withdrawals.append(total_withdrawals_category)

    total_spent_all_categories = abs(sum(total_withdrawals))

    # Gasto total (retiradas) por categoria + Porcentagem do gasto total por categoria (Arredondado para baixo para a dezena mais próxima)

    categories_data = []
    for category in categories:
        total_withdrawals_category = 0
        for withdrawal in category.ledger:
            if withdrawal['amount'] < 0:
                total_withdrawals_category += withdrawal['amount']
        
        total_withdrawals_category = abs(total_withdrawals_category)
        percent = total_withdrawals_category / total_spent_all_categories * 100
        percent = (percent // 10) * 10
        data = {'name': category.name, 'total_spent': total_withdrawals_category, 'percent': percent}
        categories_data.append(data)
    
    # BUILD CHART

    spend_chart = 'Percentage spent by category\n'

    for i in range(100,-10,-10):
        line = str(i).rjust(3) + '|'
        for category in categories_data:
            if category['percent'] >= i:
                line += ' o '
            else:
                line += '   '
        line += ' \n'
        spend_chart += line

    total_bars = len(categories) * 3
    spend_chart += '    ' + '-' * total_bars + '-\n'

    max_lenght = 0

    for category in categories:
        if len(category.name) > max_lenght:
            max_lenght = len(category.name)


    for i in range(0, max_lenght):
        line = '    '
        
        for category in categories_data:
            if len(category['name']) > i:
                letter = category['name'][i]
                line += f' {letter} '
            else:
                line += '   '

        if max_lenght-1 == i:
            line += ' '
            spend_chart += line
        
        else:
            line += ' \n'
            spend_chart += line

    return spend_chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)


auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(create_spend_chart([food, clothing, auto]))