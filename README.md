## This script does NOT have the functionality of transferring any coins out of your account.


### Also, it CANNOT drain your account or loop trades endlessly.


#### Go to Binance API Management -> Create API Key -> Paste the Keys into the "keys.txt" file

Run "python main.py" from directory in command line

Note: Please do not sell balance more than once before buying back portfolio, otherwise conflicts may occur.

Note 2: This script does not use ALL the btc in your account when buying back, it only uses the BTC that was gained via the selloff. The side effect of this is for very small portfolios, the number of coins bought back may be slightly less (all else equal) due to fees and minimum increment sizes.

Don't have Python?

https://www.python.org/downloads/

Don't forget it to add it to your Operating System's "PATH" variable (google it).
