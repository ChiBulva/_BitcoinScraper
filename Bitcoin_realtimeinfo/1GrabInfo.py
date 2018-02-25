import urllib2
import html2text
import time
timestr = time.strftime("_timestamp_%m_%d_%Y-%H_%M_%S")

url=''
page = urllib2.urlopen("https://www.bitstamp.net/api/")
html_content = page.read()
rendered_content = html2text.html2text(html_content)
file = open("Timestamps/BTCPrice"+timestr+".txt.", 'w')
file2 = open("TempBTCPrice.txt.", 'w')
file.write(rendered_content)
file2.write(rendered_content)
file.close()
file2.close()