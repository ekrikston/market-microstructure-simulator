# Define what an order is (market or limit)
# Include the following:
# -- Unique ID
# -- Buy / sell side
# -- Quantity
# -- Price (if limit)
# -- Type (limit vs. market)
# -- Timestamp 

class Order:
  def __init__(self, order_id, direction, quant, type, time=None, stop=False, limit_price=None, stop_price=None):

    #Unique Order ID
    self.order_id = order_id

    #Either buy or sell
    self.direction = direction

    #Quantity of order
    self.quantity = quant

    #Desired price if limit order or stop-limit order 
    self.limit_price = limit_price

    #If the order is a stop order, the trigger price when the order is activated 
    self.stop_price = stop_price

    #Type of order: "market" or "limit"
    self.order_type = type

    #either True or False if the order is a stop order 
    self.stop = stop

    #Time at which the order is placed 
    self.timestamp = time
  
  def is_match(self, order2):
    # returns True if the current order is a match with order2, else False
    # self.direction must be opposite of order2.direction
    # -- if either order is type market --> match 
    # -- else:
    # ---- if the buy - sell price >= 0 --> match   
    if self.direction == order2.direction: 
      return False
    else:
      if self.order_type == "market" or order2.order_type == "market":
        return True
      elif self.direction == "buy":
        return self.limit_price >= order2.limit_price
      else:
        return self.limit_price <= order2.limit_price