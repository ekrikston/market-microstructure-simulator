# Define what an order is (market or limit)
# Include the following:
# -- Unique ID
# -- Buy / sell side
# -- Quantity
# -- Price (if limit)
# -- Type (limit vs. market)
# -- Timestamp 

class Order:
  def __init__(self, order_id, direction, quantity, timestamp=None):
    
    self.order_id = order_id    # Unique Order ID 
    self.direction = direction  # Either "buy" or "sell"
    self.quantity = quantity    # Quantity of order 
    self.timestamp = timestamp  # Time at which the order is placed

class MarketOrder(Order):
  def __init__(self, order_id, direction, quantity, timestamp=None):
    super().__init__(order_id, direction, quantity, timestamp)

class LimitOrder(Order):
  def __init__(self, order_id, direction, quantity, limit_price, timestamp=None):
    super().__init__(order_id, direction, quantity, timestamp)
    self.limit_price = limit_price

class StopOrder(Order):
  def __init__(self, order_id, direction, quantity, stop_price, timestamp=None):
    super().__init__(order_id, direction, quantity, timestamp)
    self.stop_price = stop_price
    self.activated = False

class CancelOrder(Order):
  def __init__(self, order_id, cancel_id, timestamp=None):
    super().__init__(order_id, direction=None, quantity=0, timestamp=timestamp)
    self.cancel_id = cancel_id