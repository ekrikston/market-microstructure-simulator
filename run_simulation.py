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
  book = OrderBook()
  exchange = Exchange(book)
  traders = [RandomTrader(i) for i in range(10)]
  for i in range(N):
    for trader in traders:
      order = trader.generate_order()
      if order: 
        exchange.submit_order(order)
      exchange.print_order_book()
      exchange.print_trades()


if __name__ == "__main__":
  main()