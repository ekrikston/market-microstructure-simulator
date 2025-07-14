# Central coordinator of simulation:
# -- Instatiate order book and matching engine
# -- Accept orders from traders
# -- Send orders through the engine
# -- Collect trade history, market stats, etc
# -- Run the simulation loop (1 tick / sec)
# -- Possibly also handle market time, events, randomness