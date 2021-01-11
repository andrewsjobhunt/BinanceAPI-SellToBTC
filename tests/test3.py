import binance


# def check_apikey
#   try:
#     txt = open('keys.txt', "r")
#   except:
#     return 0

#   # return txt.readlines()
#   return txt.readlines()

print("\nFAILED\n") if binance.check_apikey() == 1 else print("\n...OK!\n")