import colorama
from colorama import Fore, Style

import time
#import os
import re

colorama.init()

timestr = time.strftime("_timestamp_%m_%d_%Y-%H_%M_%S")

key = open("BuyingPriceKey.txt", "r").readlines()
newprice = open("CurrentBTCPrice.txt").readline()

coin = key[4].rstrip()
usdatpurchase = key[5].rstrip()
totalinvestment = key[6].rstrip()

print "I bought at:		"+str(usdatpurchase)+" 	USD per BTC"
print "I purchased:		"+str(totalinvestment)+" 		worth of BTC"
print "for total of:		"+str(coin)+" 	BTC"

print "\n"

print "Price of BTC:		"+str(newprice)
print "Bitcoin has risen:	"+str(float(newprice)-float(usdatpurchase))
pricedifference = (float(newprice)-float(usdatpurchase))

currentusd = (float(newprice)*(float(coin)))
gains = (float(currentusd)-float(totalinvestment))

print "I have a total of:	"+str(currentusd)+"	in BTC"

text1 = "I have gained:		"
text2 = " 	Since my Original Purchase"

print text1 + Fore.GREEN + str(gains) + Style.RESET_ALL + text2

print "That is:		"+str((float(gains)/float(totalinvestment))*100)+"%"


#os.remove("TempBTCPrice.txt")

