# Initialize exchange and trader agents
# Run simulation for N steps 
# Output results to console or files
# Possibly: include CLI flags for parameters

from simulator.order import Order
from simulator.order_book import OrderBook
from simulator.exchange import Exchange
from simulator.trader import Trader, RandomTrader

#N = 100

def main():
  exchange = Exchange()
  order1 = Order(1, "A", "sell", "Limit", quantity = 25, price = 75)
  order2 = Order(2, "B", "buy", "Limit", quantity = 50, price = 80)
  order3 = Order(3, "C", "sell", "Limit", quantity = 25, price = 85)
  order4 = Order(4, "E", "buy", "Stop", quantity=25, price = 80)
  order5 = Order(5, "D", "sell", "Limit", quantity = 25, price = 85)
  order6 = Order(6, "A", "buy", "Limit", quantity = 25, price = 90)
  orders = [order1, order2, order3, order4, order5, order6]

  for ord in orders:
    exchange.submit_order(ord)
    exchange.print_order_book()
  
  exchange.print_trades()
  #traders = [RandomTrader(i) for i in range(10)]
  #for i in range(N):
    #for trader in traders:
      #order = trader.generate_order()
      #if order: 
        #exchange.submit_order(order)
      #exchange.print_order_book()
      #exchange.print_trades()


if __name__ == "__main__":
  main()