# Simulate trading agents / trading behavior
# -- Random traders placing random orders
# -- Momentum-based traders who buy/sell based on past price movement
# -- Market makers quoting both sides 
# -- Idea: create base Trader class and then diff subclasses 

from order import Order

class Trader:
  def __init__(self, trader_id):
    self.trader_id = trader_id
  
class RandomTrader(Trader):
  def __init__(self, trader_id):
    super().__init__(trader_id)
  
  def generate_order(self):
    return