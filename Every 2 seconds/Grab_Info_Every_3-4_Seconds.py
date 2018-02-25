import urllib2
import html2text
import time
from time import sleep

file = open("Timestamps/2_seconds"+".txt", 'w')
file2 = open("Timestamps/2_seconds_times"+".txt", 'w')
file3 = open("Timestamps/2_seconds_times_LABELED"+".txt", 'w')

for x in range(0, 10):
	sleep(1)
	url=''
	timestr = time.strftime("%H:%M:%S\n")
	timestr2 = time.strftime("%m/%d/%Y - Hour: %H Min: %M Sec: %S\n")
	page = urllib2.urlopen("https://www.bitstamp.net/api/")
	html_content = page.read()
	rendered_content = html2text.html2text(html_content)
	file.write(str(rendered_content[569:577])+"\n")
	file2.write(timestr)
	file3.write(timestr2)
	#print rendered_content[569:577]

#file.write(rendered_content)

file.close()
file2.close()

	
"""
	timestr = time.strftime("_timestamp_%m_%d_%Y-%H_%M_%S")
	html_content = page.read()
	rendered_content = html2text.html2text(html_content)
	file = open("Timestamps/BTCPrice"+timestr+".txt.", 'w')
	file2 = open("TempBTCPrice.txt.", 'w')
	file.write(rendered_content)
	file2.write(rendered_content)
	file.close()
	file2.close()
"""