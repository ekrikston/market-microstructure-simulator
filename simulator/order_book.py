# Manage the live list of orders. 
# The core structure holding all active orders waiting to be matched:
#  -- Maintain two sortted sides -- buy (bids) and sell (asks)
#  -- Insert new limit orders
#  -- Remove or update orders (e.g. cancellations)
#  -- Return best bid/ask
#  -- Possibly support price-time priority or FIFO 