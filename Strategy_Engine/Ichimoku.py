# It takes the given number of the last candles and return
# the kijun_sen (26) or tenkan_sen (9) depends on the given number
def sen_calculator(candles, interval):
    high_prices = []
    low_prices = []
    for candle in candles[-interval:]:
        high_prices.append(candle['h'])
        low_prices.append(candle['l'])
    return (max(high_prices) + min(low_prices)) / 2
