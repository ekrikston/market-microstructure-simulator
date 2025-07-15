# Initialize exchange and trader agents
# Run simulation for N steps 
# Output results to console or files
# Possibly: include CLI flags for parameters

from simulator.order import Order
#from simulator.order_book import OrderBook

def main():

  order1 = Order(1, "buy", 100, "limit", limit_price=55) 
  order2 = Order(2, "sell", 100, "limit", limit_price = 50)
  #bids = [order1]
  #asks = [order2]
  match = order1.is_match(order2)
  print(match)
  #book = OrderBook(bids, asks, [])


if __name__ == "__main__":
  main()