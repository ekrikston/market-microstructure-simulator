# Manage the live list of orders. 
# The core structure holding all active orders waiting to be matched:
#  -- Maintain two sorted sides -- buy (bids) and sell (asks)
#  -- Insert new limit orders
#  -- Remove or update orders (e.g. cancellations)
#  -- Return best bid/ask
#  -- Possibly support price-time priority or FIFO 
import heapq

class OrderBook:
  def __init__(self):
    # List of bids (orders looking to buy) -- sorted by price-time priority
    self.bids = []

    # List of bids (orders looking to sell) -- sorted by price-time priority 
    self.asks = []

    # List stop orders waiting to be activated
    self.stops = []
  
  def insert(self, order):
    # Inserts a new limit order to the book
    if order.direction == "buy":
      heapq.heappush(self.bids, (-order.limit_price, order.timestamp, order.order_id, order))
    else:
      heapq.heappush(self.asks, (order.limit_price, order.timestamp, order.order_id, order))
  
  def cancel(self, order):
    # Removes specified order from the book
    return order
  
  def get_best_ask(self):
    # Returns order with lowest selling price
    best_ask = heapq.heappop(self.asks)
    return best_ask[3]
  
  def get_best_bid(self):
    # Returns order with highest buying price 
    best_bid = heapq.heappop(self.bids)
    return best_bid[3]