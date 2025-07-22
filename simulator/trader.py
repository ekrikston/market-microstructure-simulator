# Simulate trading agents / trading behavior
# -- Random traders placing random orders
# -- Momentum-based traders who buy/sell based on past price movement
# -- Market makers quoting both sides 
# -- Idea: create base Trader class and then diff subclasses 

from simulator.order import Order

class Trade:
  def __init__(self, timestamp, trade_id, buy_order, sell_order, trade_price, trade_quantity):
    self.timestamp = timestamp
    self.trade_id = trade_id
    self.buy_order_id = buy_order.order_id
    self.sell_order_id = sell_order.order_id
    self.buyer_id = buy_order.trader_id
    self.seller_id = sell_order.trader_id
    self.trade_price = trade_price
    self.trade_quantity = trade_quantity 
    self.buy_order_type = buy_order.order_type
    self.sell_order_type = sell_order.order_type
    self.agressor = "Buy" if buy_order.timestamp > sell_order.timestamp else "Sell"
  
  def to_csv_row(self):
    return [
      self.timestamp,
      self.trade_id,
      self.trade_price,
      self.trade_quantity,
      self.buy_order_id,
      self.sell_order_id,
      self.buyer_id,
      self.seller_id,
      self.buy_order_type,
      self.sell_order_type,
      self.agressor
    ]
     
# A trader should keep track of the orders they've made
class Trader:
  def __init__(self, trader_id):
    self.trader_id = trader_id
  
class RandomTrader(Trader):
  def __init__(self, trader_id):
    super().__init__(trader_id)
  
  def generate_order(self):
    return