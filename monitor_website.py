import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
	url = "http://Google.com/"
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, "lxml")

	if str(soup).find("Google") == -1:
		time.sleep(60)
		continue
		
	else:

