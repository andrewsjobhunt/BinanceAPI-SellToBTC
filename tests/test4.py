import binance

try:
    tmp = binance.check_apikey()
    apikey_public = tmp[0]
    apikey_secret = tmp[1]
    del tmp
    print("\n...OK!\n")
except:
    print("\nFAILED\n")