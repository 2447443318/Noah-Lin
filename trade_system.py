from order import Order
from market import Market

import random
from time import sleep

print("Welcom to Stock Market\n")
is_code = False
while not is_code:
    name = input("Please input trading code(three intigers) so we can show the transaction:")
    if len(name) > 3 or len(name) == 0:
        print('Trading code should be three intigers!')
        continue
    for letter in name:
        if letter not in '0123456789':
            print('Code should not contain letters!')
            is_code = False
            break
        is_code = True

ask_price = sorted(random.sample(range(30,50),7),reverse= True)
ask_number = sorted(random.sample(range(100,200),7))

bid_price = sorted(random.sample(range(1,25),7),reverse= True)
bid_number = sorted(random.sample(range(100,200),7))

market = Market(name, ask_price, ask_number, bid_price, bid_number)

print("Loading......")
sleep(0.5)
print("......\n\n")
sleep(0.5)

market.show()
print()
is_quit = False
i = 1

while not is_quit:
    a = input(f"[{i}]please input your order(sell/buy price number): ").split()
    i += 1
    if a == ['quit']:
        is_quit = True
    elif len(a) !=3 or a[0] not in ['buy','sell'] or int(a[1]) <= 0 or int(a[2]) <= 0:
        print('Invalid order!')
        continue   
    buy, price, number = a
    if buy == "buy":
        is_buy = True
    elif buy == "sell":
        is_buy = False  
    order = Order(int(number), int(price), is_buy)
    market.order_waiting(order)

print('\nThank you for using our trading system!')
