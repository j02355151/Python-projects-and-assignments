import collections
import sys

stockLists = {}
stockLists['T-Mobile US'] = collections.deque()
stockLists['Verizon'] = collections.deque()

def buyStock(stock_list, name, quantity, price):
    stock = {'name': name, 'quantity': quantity, 'price': price}
    stock_list.appendleft(stock)
    print(f"You bought {quantity} shares of {name} stock at ${price:.2f} per share")

def sellLIFO(stock_list, num_to_sell):
    total_quantity = sum(stock['quantity'] for stock in stock_list)
    if not stock_list or num_to_sell > total_quantity:
        print("Insufficient stocks to sell.")
        return

    total_cost = 0
    remaining_to_sell = num_to_sell

    while remaining_to_sell > 0:
        top_stock = stock_list[0]
        if top_stock['quantity'] <= remaining_to_sell:
            total_cost += top_stock['price'] * top_stock['quantity']
            remaining_to_sell -= top_stock['quantity']
            stock_list.popleft()
        else:
            total_cost += top_stock['price'] * remaining_to_sell
            top_stock['quantity'] -= remaining_to_sell
            remaining_to_sell = 0

    avg_cost = total_cost / num_to_sell
    print(f"You sold {num_to_sell} shares at an average cost of ${avg_cost:.2f} per share using LIFO")

def sellFIFO(stock_list, num_to_sell):
    total_quantity = sum(stock['quantity'] for stock in stock_list)
    if not stock_list or num_to_sell > total_quantity:
        print("Insufficient stocks to sell.")
        return

    total_cost = 0

    while num_to_sell > 0:
        top_stock = stock_list[0]
        if top_stock['quantity'] <= num_to_sell:
            total_cost += top_stock['price'] * top_stock['quantity']
            num_to_sell -= top_stock['quantity']
            stock_list.popleft()
        else:
            total_cost += top_stock['price'] * num_to_sell
            top_stock['quantity'] -= num_to_sell
            num_to_sell = 0

    avg_cost = total_cost / (num_to_sell + sum(stock['quantity'] for stock in stock_list))
    print(f"You sold {num_to_sell} shares at an average cost of ${avg_cost:.2f} per share using FIFO")

while True:
    stock_name = input("Enter stock name (e.g. T-Mobile US, Verizon) or 'quit' to exit: ")
    if stock_name.lower() == 'quit':
        break

    if stock_name not in stockLists:
        print("Stock not recognized. Try again.")
        continue

    control_num = int(input("Input 1 to buy, 2 to sell: "))
    quantity = int(input("How many stocks: "))

    if control_num == 1:
        price = float(input("At what price: "))
        buyStock(stockLists[stock_name], stock_name, quantity, price)
    else:
        control_num = int(input("Press 1 for LIFO accounting, 2 for FIFO accounting: "))
        if control_num == 1:
            sellLIFO(stockLists[stock_name], quantity)
        else:
            sellFIFO(stockLists[stock_name], quantity)

