# Central coordinator of simulation:
# -- Instatiate order book, list of stop orders, and matching engine
# -- Accept orders submitted by traders
# -- Implement matching logic 
# -- Collect trade history, market stats, etc??
# -- Run the simulation loop (1 tick / sec)??
# -- Possibly also handle market time, events, randomness??

from simulator.order import Order
from simulator.order_book import OrderBook
from simulator.trader import Trader, Trade
import csv

class Exchange:
  def __init__(self):
    self.order_book = OrderBook()
    self.last_trade_price = None
    self.stops = OrderBook()
    self.time = 0
    self.total_trades = 0
    self.trade_log_path = "trade_log.csv"
    with open(self.trade_log_path, "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow([
        "Timestamp", "Trade ID", "Trade Price", "Trade Quantity", 
        "Buy Order ID", "Sell Order ID", "Buyer ID", "Seller ID", 
        "Buy Order Type", "Sell Order Type", "Aggressor"
      ])
  
  def check_stops(self):
    # scan stop order book if any stops are triggered by last_trade_price
    # submit any newly activated orders 

    # First check bids
    while self.stops.bids:
      stop_order = self.stops.safe_peek("buy")
      if self.last_trade_price is None or self.last_trade_price < stop_order.price:
        break
      self.stops.safe_pop("buy")
      stop_order.order_type = "Market"
      stop_order.stop_activated = True
      self.submit_order(stop_order)
    
    #Next check asks
    while self.stops.asks:
      stop_order = self.stops.safe_peek("sell")
      if self.last_trade_price is None or self.last_trade_price > stop_order.price:
        break
      self.stops.safe_pop("sell")
      stop_order.order_type = "Market"
      stop_order.stop_activated = True
      self.submit_order(stop_order)

  def log_trade(self, trade):
    # Add trade as a row in the trade log
    with open(self.trade_log_path, "a", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(trade.to_csv_row())
  
  def make_trade(self, incoming_order, resting_order, incoming_direction):
    # Make a trade, log the trade, and return new quantities of each order

    resting_price = resting_order.price
    match_quantity = min(incoming_order.quantity, resting_order.quantity)   
    trade = Trade(
      timestamp = self.time,
      trade_id = self.total_trades,
      buy_order = incoming_order if incoming_direction == "buy" else resting_order,
      sell_order = incoming_order if incoming_direction == "sell" else resting_order,
      trade_price = resting_price,
      trade_quantity = match_quantity
    )
    self.log_trade(trade)
    self.total_trades += 1
    self.last_trade_price = resting_price
    self.check_stops
    return incoming_order.quantity - match_quantity, resting_order.quantity - match_quantity

  def match_limit_order(self, incoming_order):

    # Matching incoming limit orders or adding to order book

    incoming_direction = incoming_order.direction
    pop_direction = "sell" if incoming_direction == "buy" else "buy"
    resting_order = self.order_book.safe_peek(pop_direction)
    if resting_order is None:
      self.order_book.insert(incoming_order)
      return

    while resting_order and incoming_order.is_match(resting_order): 
      #Pop resting order from heap
      self.order_book.safe_pop(pop_direction)

      # Make the trade, get total amount traded, and update orders
      incoming_order.quantity, resting_order.quantity = self.make_trade(incoming_order, resting_order, incoming_direction)

      # Put resting order back in the book if remainder
      if resting_order.quantity > 0:
        self.order_book.insert(resting_order)

      # If all of incoming order has been traded, return from function
      if incoming_order.quantity == 0:
        return

      # Get new resting order 
      resting_order = self.order_book.safe_peek(pop_direction)

    # If resting and incoming order not a match, add remainder of incoming order to book
    self.order_book.insert(incoming_order)

  def match_market_order(self, incoming_order):

    # Matching incoming market orders 
    incoming_direction = incoming_order.direction
    pop_direction = "sell" if incoming_direction == "buy" else "buy"

    while incoming_order.quantity > 0:

      resting_order = self.order_book.safe_pop(pop_direction)
      if resting_order is None:
        print("No liquidity remaining")
        return
      
      incoming_order.quantity, resting_order.quantity = self.make_trade(incoming_order, resting_order, incoming_direction)

      if resting_order.quantity > 0:
        self.order_book.insert(resting_order)

  def submit_order(self, order):
    order.timestamp = self.time
    self.time += 1
    incoming_order_type = order.order_type
    if incoming_order_type == "Market":
      self.match_market_order(order)
      self.check_stops()
    elif incoming_order_type == "Limit":
      self.match_limit_order(order)
      self.check_stops()
    elif incoming_order_type == "Stop":
      self.stops.insert_stop(order)
    elif incoming_order_type == "Cancel":
      self.order_book.cancel(order.direction, order.cancel_id)
    else:
      print("Invalid order type")
  
  def print_order_book(self, n=5):
    print("\n--- Order Book --- ")
    print("\nBIDS (Buy Orders): ")
    print("Price\tQty\tTrader\tType\tTime")

    top_bids = sorted(self.order_book.bids)[:n]
    for _, _, _, order in top_bids:
      print(f"{order.price:.2f}\t{order.quantity}\t{order.trader_id}\t{order.order_type}\t{order.timestamp}")

    print("\nASKS (Sell Orders): ")
    print("Price\tQty\tTrader\tType\tTime")

    top_asks = sorted(self.order_book.asks)[:n]
    for _, _, _, order in top_asks:
      print(f"{order.price:.2f}\t{order.quantity}\t{order.trader_id}\t{order.order_type}\t{order.timestamp}")


  def print_trades(self, n=5):
    print(f"\n--- Preview First {n} Trades ---")
    
    with open(self.trade_log_path, mode="r") as f:
      reader = csv.reader(f)
      header = next(reader)
      print("\t".join(header))
      for i, row in enumerate(reader):
        print("\t".join(row))
        if i + 1 >= n:
          break
  
  def save_trades(self, filename=None):
    if filename==None:
      timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
      filename = f"trade_log_{timestamp}.csv"
    
    shutil.copy(self.trade_log_path, filename)
    print(f"Trade log saved as {filename}")
