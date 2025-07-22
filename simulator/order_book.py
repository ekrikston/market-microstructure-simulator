# Manage the live list of orders. 

import heapq

class OrderBook:
  def __init__(self):
    # List of bids (orders looking to buy) -- sorted by price-time priority
    self.bids = []

    # List of bids (orders looking to sell) -- sorted by price-time priority 
    self.asks = []
  
  def insert(self, order):
    # Inserts a new limit order to the book
    if order.direction == "buy":
      heapq.heappush(self.bids, (-order.price, order.timestamp, order.order_id, order))
    else:
      heapq.heappush(self.asks, (order.price, order.timestamp, order.order_id, order))
  
  def cancel(self, direction, cancel_id):
    # Removes specified order from the book
    heap = self.bids if direction == "buy" else self.asks
    for _, _, order_id, order in heap:
      if order_id == cancel_id:
        order.active = False
  
  def safe_pop(self, direction):
    # Returns best active offer and removes from heap
    heap = self.asks if direction == "sell" else self.bids
    while heap:
      best = heapq.heappop(heap)[3]
      if best.active:
        return best
    return None

  def safe_peek(self, direction):
    # Returns best active offer without altering heap
    heap = self.asks if direction == "sell" else self.bids
    while heap:
      best = heap[0][3]
      if best.active:
        return best
      else:
        heapq.heappop(heap)[3]
    return None