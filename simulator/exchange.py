# Central coordinator of simulation:
# -- Instatiate order book and matching engine
# -- Accept orders from traders
# -- Send orders through the engine
# -- Collect trade history, market stats, etc
# -- Run the simulation loop (1 tick / sec)
# -- Possibly also handle market time, events, randomness
from order import Order, MarketOrder, LimitOrder, StopOrder, CancelOrder

class Exchange:
  def __init__(self, order_book):
    self.order_book = order_book
    self.last_trade_price = None
    self.trade_log = []
    self.stops = []
    self.time = 0
  
  def check_stops(self):
    # check if any stop orders are activated
    # submit any newly activated orders 
    return

  def log_trade(self):
    # add trade to trade book
    # udpate last trade price 
    return

  def match_limit_order(self, order):
    # check for match in order book
    # if no match, add order to order_book 
    # if match, log the trade
    return

  def match_market_order(self, order):
    # logs trade and updates last trade price 
    # rejects or partially filles the market order if no liquidity available
    return 
  
  def submit_order(self, order):
    order.timestamp = self.time
    self.time += 1
    if isinstance(order, MarketOrder):
      self.match_market_order(order)
    elif isinstance(order, LimitOrder):
      self.match_limit_order
    elif isinstance(order, StopOrder):
      self.stops.append(order)
    elif isinstance(order, CancelOrder):
      self.order_book.cancel(order)
    else:
      print("Invalid order")

    self.check_stops()
  
  def print_order_book(self):
    print("Order Book: ")

  def print_trades(self):
    print("Trade Log: ")