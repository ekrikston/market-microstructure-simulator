# Define what an Order is

class Order:
  def __init__(self, order_id, trader_id, direction, quantity, order_type, price = None, timestamp=None, cancel_id = None):
    
    self.order_id = order_id      # Unique Order ID 
    self.trader_id = trader_id    # ID of trader who submitted the order
    self.direction = direction    # Either "buy", "sell"
    self.quantity = quantity      # Quantity of order 
    self.order_type = order_type  # 'Market', 'Limit', 'Stop', or 'Cancel'
    self.price = price            # If Limit Order, price = limit price
                                  # If Stop Order, price = stop price 
    self.timestamp = timestamp    # Time at which the order is placed
    self.active = True            # active = True if the order is still waiting to be filled
    self.cancel_id = cancel_id    # If cancel order, cancel_id = id of the order to cancel
    self.stop_activated = False   # If stop order, stop_activated = True once stop price is met
  
  def is_match(self, resting_order):
    # Checks if current order is a match with the resting order
    # Assumes order type is limit or an activated stop order
    if self.direction == "buy":
      return self.price >= resting_order.price
    else:
      return self.price <= resting_order.price