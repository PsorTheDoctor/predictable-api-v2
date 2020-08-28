import numpy as np
import arrow

from utils.coin_gecko import get_single_price

now = arrow.utcnow()

future_prices = []


def get_future_prices():
    return future_prices


def get_single_future_price(n_days_forward):
    return future_prices[n_days_forward - 1]


def get_last_dates(n_last_days):
    last_dates = []
    for day in range(n_last_days, 0, -1):
        past_date = now.shift(days=-day)
        last_dates.append(past_date.format('DD-MM-YYYY'))
    return last_dates


# Erroneous method
# For high numbers may get 429 too many requests error
# Sleep method could be useful
def get_last_prices(currency, n_last_days):
    last_dates = get_last_dates(n_last_days)
    last_prices = []
    for date in last_dates:
        past_price = get_single_price(currency, date)
        last_prices.append(past_price)
    return last_prices


def simple_moving_average(values):
    return np.mean(values)


def predict_prices(currency, n_last_days, n_future_days=3):
    prices = get_last_prices(currency, n_last_days)
    pred_prices = []

    pred_price = simple_moving_average(prices)
    pred_prices.append(pred_price)

    if n_future_days > 1:
        for idx in range(n_future_days - 1):
            pred_price = simple_moving_average(np.concatenate((prices[idx + 1:], pred_prices), axis=None))
            pred_prices.append(pred_price)

    global future_prices
    future_prices = pred_prices

    return pred_prices
