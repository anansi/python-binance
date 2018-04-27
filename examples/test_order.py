import sys
sys.path.insert(0, '../')
sys.path.insert(0, '/root/sites/binance_python/')


from datetime import datetime
from binance.client import Client

MY_KEY = "PXRZZR2Jv54oDVmTZcE10lXty2Swgj6tIXz5OqEGns5drO3bqlyLFkucD31dlnvt"
MY_SECRET = "iBJEghWwUYL346Kny5uLCWC0j6UDmAtkbeeZjYHT1Zf9CiNmXWPcBLMTt75ekw1t"

client = Client(MY_KEY, MY_SECRET)
order = client.create_order(
    symbol='BTCUSDT',
    side=Client.SIDE_SELL,
    type=Client.ORDER_TYPE_MARKET,
    quantity=0.001)

print "order placed"
