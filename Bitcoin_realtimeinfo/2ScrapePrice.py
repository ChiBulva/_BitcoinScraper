import time
#import os
import re

timestr = time.strftime("_timestamp_%m_%d_%Y-%H_%M_%S")

line = open("TempBTCPrice.txt", "r").readlines()[25]
line2 = re.findall(r'\b\d+\b',str(line))
line3 = line2[0]+"."+line2[1]


file = open ("CurrentBTCPrice.txt", "w")
file2 = open ("JustPrice/BTCPrice"+timestr+".txt", "w")
file2.write(line)
file.write(line3)
file.close();
file2.close();

#os.remove("TempBTCPrice.txt")

