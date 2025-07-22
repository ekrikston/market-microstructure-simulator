# Define what an order is (market or limit)
# Include the following:
# -- Unique ID
# -- Buy / sell side
# -- Quantity
# -- Price (if limit)
# -- Type (limit vs. market)
# -- Timestamp 

class Order:
  def __init__(self, order_id, trader_id, direction, quantity, order_type, price = None, timestamp=None):
    
    self.order_id = order_id    # Unique Order ID 
    self.trader_id = trader_id  # ID of trader who submitted the order
    self.direction = direction  # Either "buy", "sell"
    self.quantity = quantity    # Quantity of order 
    self.order_type = order_type  # 'Market', 'Limit', 'Stop', or 'Cancel'
    self.timestamp = timestamp  # Time at which the order is placed
    self.price = price          # If Limit Order, price = limit price
                                # If Stop Order, price = stop price 
    self.active = True
    

class MarketOrder(Order):
  def __init__(self, order_id, trader_id, direction, quantity, timestamp=None):
    super().__init__(order_id, trader_id, direction, quantity, "Market", price=None, timestamp=None)

class LimitOrder(Order):
  def __init__(self, order_id, trader_id, direction, quantity, limit_price, timestamp=None):
    super().__init__(order_id, trader_id, direction, quantity, "Limit", limit_price, timestamp)

class StopOrder(Order):
  def __init__(self, order_id, trader_id, direction, quantity, stop_price, timestamp=None):
    super().__init__(order_id, trader_id, direction, quantity, "Stop", stop_price, timestamp)
    self.activated = False

class CancelOrder(Order):
  def __init__(self, order_id, trader_id, direction, cancel_id, timestamp=None):
    super().__init__(order_id, trader_id, direction, 0, "Cancel", price=None, timestamp=None)
    self.cancel_id = cancel_id