import methods.binance as binance
import io

def print_menu():
    print("\n****************************")
    print("* Menu:                    *")
    print("*                          *")
    print("* 1. Retrieve Balance      *")
    print("* 2. Sell All Coins        *")
    print("* 3. Buyback All Coins     *")
    print("*                          *")
    print("* 0. Exit                  *")
    print("****************************\n\n")
    return int(input("Please enter a number: "))


def get_balance(apikey_public, apikey_secret):
    print("\nRetrieving all coins that are greater than 0........\n\n")
    response = binance.get_coins(apikey_public, apikey_secret)
    total_btc = 0
    btc_price = 0
    placeholder_btc_units = 0
    for i in response:
      if(i['free'] != '0'):
        try:
          if(i['coin'] == 'BTC'):
            placeholder_btc_units = float(i['free'])
            continue
          print('Token: ' + i['coin'])
          print('Units: ' + str(f"{float(i['free']):.8f}") + ' ' + i['coin'])
          if(i['trading']):
            pmt = binance.coin_price(i['coin'] + 'BTC')['price']
            print('Price: ' + pmt + ' BTC')
            output = f"{(binance.truncate(float(pmt) * float(i['free']), 8)):.8f}"
            print('*********************\n' + 'Value: ' + str(output) + ' BTC' + '\n*********************')
            total_btc += (float(pmt) * float(i['free']))
          else:
            print('N/A')
          print('\n')
        except:
          print("Not Applicable.\n\n")
          continue
  
    btc_price = binance.coin_price('BTCUSDT')['price']

    print('Token: BTC - The King')
    print('Units: ' + str(f"{placeholder_btc_units:.8f}") + 'BTC')
    print('Price: ' + btc_price + ' USDT')
    print('*********************\n' + 'Value: ' + str(binance.truncate(float(btc_price) * placeholder_btc_units, 8)) + ' USDT' + '\n*********************')
    total_btc += placeholder_btc_units
    print("\n")

    print('Total portfolio value: ' + str(binance.truncate(total_btc, 8)) + ' BTC')
    total_usdt = binance.truncate(total_btc * float(btc_price), 8)
    print('Total portfolio value: $' + str(total_usdt) + 'USDT\n')
    print('-- Calculated using $' + btc_price + ' per Bitcoin\n')




def sell_balance(apikey_public, apikey_secret):
  print("\nYou have selected 2: Sell All Coins")
  print("\nSelling all applicable coins that are greater than 0 into BTC")
  print("This does not include fiat currencies etc.\n")
  response = binance.get_coins(apikey_public, apikey_secret)
  binance_info_dict = binance.get_binance_info()['symbols']

  def search(symbol):
    for i in binance_info_dict:
      if(i['symbol'] == symbol):
        return i

  btc_price = binance.coin_price('BTCUSDT')['price']
  btc_total = 0
  btc_gained = 0
  fee_cum = 0
  pct_dict = {}

  for i in response:
    if(i['free'] != '0' and i['trading']):
      print("\n********************************************************\n")
      print("Coin: " + i['coin'])
      print("Balance: " + i['free'])
      print("\nAttempting to sell " + i['coin'] + " do not close this app........\n")

      coin_object = search(i['coin'] + 'BTC')

      if(coin_object == None):
        print("Coin cannot be traded in BTC                               ...N/A")
      else:
        tmp = i['free']
        divisor = coin_object['filters'][2]['stepSize']
        zero_target = round(float(i['free']) % float(divisor), 8)
        if zero_target != 0:
          tmp = round(float(i['free']) - zero_target, 8)
        trade_result = binance.trade_sell(i['coin'], tmp, apikey_public, apikey_secret)
        if(trade_result == 0):
          print("Trade failed. Skipping                                     ...FAIL\n")
          print("Please refer to the above error code for details.")
          print("You may have less than the minimum quantity.")
        elif(trade_result['status'] == 'FILLED'):
          pct_dict[i['coin']] = trade_result['cummulativeQuoteQty']
          btc_gained = float(trade_result['cummulativeQuoteQty'])
          print("Success! Sold for " + str(f'{binance.truncate(btc_gained, 8):.8f}') + " BTC                            ...SUCCESS\n")
          print("($" + str(f'{binance.truncate(btc_gained * float(btc_price), 8):.8f}') + ")")
          btc_total += btc_gained
          for j in trade_result['fills']:
            fee_cum += float(j['commission'])
          fee_cum = 0
  print("\n********************************************************\n")
  print("Received " + str(btc_total) + "BTC")
  print("($" + str(btc_total * float(btc_price)) + ")")
  print("\n********************************************************\n")

  new_dict = {}
  for i in pct_dict:
    new_dict[i] = float(pct_dict[i]) / btc_total
  new_dict['btc_total'] = btc_total
  return(new_dict)



def buy_balance(pct_dict, apikey_public, apikey_secret):
  print("\nYou have selected 3: Buy All Coins")
  print("\nBuying back all coins as applicable via Binance trading conditions\n")

  response = binance.get_coins(apikey_public, apikey_secret)
  binance_info_dict = binance.get_binance_info()['symbols']

  def search(symbol):
    for i in binance_info_dict:
      if(i['symbol'] == symbol):
        return i

  btc_total = float(pct_dict['btc_total'])
  del pct_dict['btc_total']

  for i in pct_dict:
    tmp = f"{float(pct_dict[i] * btc_total):.8f}"
    coin_object = search(i + 'BTC')
    divisor = coin_object['filters'][0]['tickSize']
    zero_target = float(f"{binance.truncate(float(pct_dict[i] * btc_total) % float(divisor), 8):.8f}")

    if zero_target != 0:
      tmp = f"{float(pct_dict[i] * btc_total) - zero_target:.8f}"
      #print("\nQuoteOrderQty: " + str(tmp))
    print("Buying " + str(tmp) + "BTC worth of " + i + "\n")
    trade_result = binance.trade_buy(i, tmp, apikey_public, apikey_secret)
    if(trade_result == 0):
      print("Trade failed. Skipping\n")
      print("Please refer to the above error code for details.")
      print("You may have less than the minimum quantity.\n")
    elif(trade_result['status'] == 'FILLED'):
      asset_gained = float(trade_result['executedQty'])
      print("Bought " + str(asset_gained) + i + "\n")
  return