import binance

# response = binance.check_status()

# print(response)

# if(binance.check_status()):
#     print("yay")

print("\nFAILED\n") if binance.check_status() == 1 else print("\nOK!\n") 