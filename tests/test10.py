import binance

public = public_key_omitted
secret = secret_key_omitted

print("\nPreloading coins and values, this may take some time........")
exchange_info_dict = binance.get_btc_info()
response = binance.get_coins(public, secret)


# We want to filter through the coins that we have
# Then remove any 0 balances
# Add non-tradeable assets to new dict, remove from old dict





print(binance.trade_sell('ETH', 0.1, public, secret))