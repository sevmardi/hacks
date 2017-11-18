import sys, os, webbrowser, pyperclip, requests
from bs4 import BeautifulSoup

def main():

	if len(sys.argv) > 1:
		#Get address from command line
		address = ''.join(sys.argv[1:])
	else:
		address = pyperclip.paste()
	
	webbrowser.open('https://www.google.nl/maps/place/' + address)

def requests_func():
	res = requests.get('https://www.woningnethollandrijnland.nl/Zoeken#model[Regulier aanbod]~plaatsenwijken[Hoofddorp]')
	try:
		res.raise_for_status()
		if res is not None:
			print(res)
		else: 
			print('There are nothing in this area')
	except Exception as e:
		print("There was a problem: %s" % (e))

def usign_bs4():
	res = requests.get('https://www.woningnethollandrijnland.nl/Zoeken#model[Regulier aanbod]~plaatsenwijken[Noordwijk]')
	res.raise_for_status()
	no_strach_soup = BeautifulSoup(res.text)
	print(no_strach_soup)


def feel_luck_search():
	print('Googling for ya .. ')
	res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
	res.raise_for_status()
	soup = BeautifulSoup(res.text)
	link_elems = soup.select('.r a')

	numOpen = min(5, len(link_elems))
	for i in range(numOpen):
		webbrowser.open('http://google.com' + linkElems[i].get('href'))



if __name__ == '__main__':
	feel_luck_search()