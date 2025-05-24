from order import Order
class Market:
    def __init__(self, trading_code, ask_price, ask_number, bid_price, bid_number):
        self.code = trading_code
        self.ask_price = ask_price
        self.ask_number = ask_number
        self.bid_price = bid_price
        self.bid_number = bid_number

    def show(self):
        print("Price|   |Number")
        for i in range(len(self.ask_price)):
            print(f"{self.ask_price[i]}|    |{self.ask_number[i]}")
        print("——————————\nAsk in waiting\n")

        print("bid in waiting\n——————————")
        for i in range(len(self.bid_price)):
            print(f"{self.bid_price[i]}|    |{self.bid_number[i]}")
        print()

    def order_dealing(self, order:Order):
        print(order)
        
        if order.is_buy == True:
            if self.ask_price == [] or order.price < self.ask_price[-1]:
            # buy_order can't make dealed immidiately have to wait
                for i in range(len(self.bid_price)):
                    if self.bid_price[i] == order.price:
                        self.bid_number[i] += order.num
                        return self.show()
                    if self.bid_price[i] < order.price:
                        self.bid_price = self.bid_price[:i] + [order.price] + self.bid_price[i:]
                        self.bid_number = self.bid_number[:i] + [order.num] + self.bid_number[i:]                        
                        return self.show()
                    if i == len(self.bid_price)-1:
                        self.bid_price = self.bid_price + [order.price] 
                        self.bid_number = self.bid_number + [order.num]                        
                        return self.show()
            return self.deal_matching(order)
            
    
        elif order.is_buy == False:
            if self.bid_price == [] or order.price > self.bid_price[0]:
            # sell_order can't make deal immidiately have to wait
                for i in range(len(self.ask_price)):
                    if self.ask_price[i] == order.price:
                        self.ask_number[i] += order.num
                        return self.show()
                    if self.ask_price[i] < order.price:
                        self.ask_price = self.ask_price[:i] + [order.price] + self.ask_price[i:]
                        self.ask_number = self.ask_number[:i] + [order.num] + self.ask_number[i:]                        
                        return self.show()
                    if i == len(self.ask_price) - 1:
                        self.ask_price = self.ask_price + [order.price]
                        self.ask_number = self.ask_number + [order.num]                     
                        return self.show()
        
            return self.deal_matching(order)
                

    def deal_matching(self, order:Order):
        if order.is_buy == True:
            pop_index = len(self.ask_price)
            for i in range(len(self.ask_price) - 1, -1, -1):
                if order.price >= self.ask_price[i]:
                    if self.ask_number[i] >= order.num:
                        self.ask_number[i] -= order.num
                        print(f'buy {order.num} stocks at price {self.ask_price[i]}')
                        
                        if self.ask_number[i] == 0:
                            pop_index = i
                        self.ask_price = self.ask_price[:pop_index]
                        self.ask_number = self.ask_number[:pop_index]
                     
                    else:
                        order.num -= self.ask_number[i]
                        pop_index = i
                        print(f'buy {self.ask_number[i]} stocks at price {self.ask_price[i]}')

                elif order.price < self.ask_price[i]:
                    self.ask_price = self.ask_price[:pop_index]
                    self.ask_number = self.ask_number[:pop_index]
                    if order.num != 0:
                        self.bid_number =  [order.num] + self.bid_number 
                        self.bid_price = [order.price] + self.bid_price
                    if i == 0:
                        self.ask_number = []
                        self.ask_price = []
                    print()
                    return self.show()  
                if i == 0:
                    self.ask_number = []
                    self.ask_price = []
                    if order.num != 0:
                        self.bid_number =  [order.num] + self.bid_number 
                        self.bid_price = [order.price] + self.bid_price
                    print()
                    return self.show()    
        else:
            i = 0
            while i < len(self.bid_price):
                if order.price <= self.bid_price[i]:
                    if self.bid_number[i] >= order.num:
                        print(f'sell {order.num} stocks at price {self.bid_price[i]}')
                        self.bid_number[i] -= order.num
                        if self.bid_number[i] == 0:
                            del self.bid_price[i]
                            del self.bid_number[i]
                        else:
                            i += 1
                        order.num = 0
                        break
                    else:
                        print(f'sell {self.bid_number[i]} stocks at price {self.bid_price[i]}')
                        order.num -= self.bid_number[i]
                        del self.bid_price[i]
                        del self.bid_number[i]
                else:
                    i += 1

            if order.num > 0:
                self.ask_price.append(order.price)
                self.ask_number.append(order.num)
            
            return self.show()
