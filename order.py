class Order:
    def __init__(self, num:int, price:int, is_buy):
        self.num = num
        self.price = price
        self.is_buy = is_buy

    def __str__(self):
        if self.is_buy:
            return f'Order:buy {self.num} stocks at price: ${self.price}\n'
        return f'Order:sell {self.num} stocks at price: ${self.price}\n' 

if __name__ == '__main__':
    print('please run trade_system.py to start!!!')
