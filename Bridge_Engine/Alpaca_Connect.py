import config
import alpaca_trade_api as tradeapi
from alpaca_trade_api.stream import Stream


base_url = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(
    config.APCA_API_KEY_ID,
    config.ALPACA_SECRET_KEY,
    base_url=base_url
)
account_info = api.get_account()
print(account_info)


async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(key_id=config.APCA_API_KEY_ID,
                secret_key=config.ALPACA_SECRET_KEY,
                base_url=base_url,
                data_feed='iex')

# subscribing to event
stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback, 'IBM')
stream.run()

