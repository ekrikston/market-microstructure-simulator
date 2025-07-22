# Initialize exchange and trader agents
# Run simulation for N steps 
# Output results to console or files
# Possibly: include CLI flags for parameters

from simulator.order import Order, MarketOrder, LimitOrder, StopOrder, CancelOrder
from simulator.order_book import OrderBook
from simulator.exchange import Exchange
from simulator.trader import Trader, RandomTrader

N = 100

def main():
  exchange = Exchange()
  order1 = LimitOrder(1, "A", "sell", 25, 75)
  order2 = LimitOrder(2, "B", "sell", 50, 60)
  order3 = LimitOrder(3, "A", "sell", 25, 70)
  order4 = MarketOrder(4, "C", "buy", 100)
  orders = [order1, order2, order3, order4]

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