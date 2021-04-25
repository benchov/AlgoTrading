last_26 = []


def candle_container(price):
    last_26.append(price)
    if len(last_26) > 6:
        last_26.pop(0)
    return last_26

while True:
    given_price = input('?price ')
    print(candle_container(given_price))