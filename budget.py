class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        show = self.name.center(30, '*') + '\n'
        for i in self.ledger:
            data = f'{i["description"][:23]:23}{i["amount"]:7.2f}'
            show += f'{data}\n'

        show += 'Total: ' + str(self.get_balance())
        return show

    def deposit(self, amount, description=''):
        deposito = {'amount': float(amount), 'description': description}
        self.ledger.append(deposito)

    def check_funds(self, amount):
        valor_total = 0
        for i in self.ledger:
            valor_total += i['amount']
        if amount <= valor_total:
            return True
        else:
            return False

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            retirada = {'amount': float(amount)*(-1), 'description': description}
            self.ledger.append(retirada)
            return True
        else:
            return False

    def transfer(self, amount, description):
        if self.check_funds(amount) == True:
            info = f'Transfer from {self.name}:Transfer to {description.name}'
            info = info.split(':')
            info_1 = info[0]
            info_2 = info[1]
            transf = {'amount': float(amount)*(-1), 'description': info_2}
            self.ledger.append(transf)
            receb = {'amount': float(amount), 'description': info_1}
            description.ledger.append(receb)
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        valor_total = 0
        for n in self.ledger:
            valor_total += n['amount']
        return valor_total


def create_spend_chart(categories):
    quant = len(categories)
    show_2 = 'Percentage spent by category\n'
    date = {}
    nm = 0
    value_int = 0

    for category in categories:
        if nm < len(category.name):
            nm = len(category.name)

        item = 0.00
        for v in category.ledger:
            if v['amount'] < 0:
                if len(category.name) > 1:
                    item += v['amount']
                    value_int += v['amount']*(-1)
                    date[category.name] = (float(item)*-1)


    for n in reversed(range(0, 101, 10)):
        show_2 += f'{(n):3}|'

        for d in date.values():
            if n < ((d/value_int)*100):
                show_2 += ' o '
            else:
                show_2 += '   '

        show_2 +=' \n'

    show_2 += '    -'
    for n in range(quant):
        show_2 +='---'

    for n in range(nm):
        show_2 += '\n    '
        for y in date.keys():
            if n < len(y):
                show_2 += ' ' + y[n] + ' '
            else:
                show_2+='   '
        show_2 += ' '

    return show_2