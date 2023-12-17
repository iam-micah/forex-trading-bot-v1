import defs

instrument = 'EUR_USD'

url = f'{defs.OANDA_URL}/instruments/{instrument}/candles'

print(url)
