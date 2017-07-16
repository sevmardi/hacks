import requests
from BeautifulSoup import BeautifulSoup
import urllib2
import re

#https://stackoverflow.com/questions/15517483/how-to-extract-urls-from-an-html-page-in-python
#https://stackoverflow.com/questions/3075550/how-can-i-get-href-links-from-html-using-python

#Objective: Scan a thread of a given site (HN) and save all
#save all the url into a text file.

class ExtractUrlFromThread():

    def __construct__(self):
        pass


    def extract(self, page):
        """
        :param page: html of web page
        :return: urls in that page
        """
        
        start_link = page.find("href")
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1: end_quote]

        return url, end_quote

    def save_into_file(self, data):
        """Save the urls into a file"""
        pass

    
    
if __name__ == "__main__":
    
    main = ExtractUrlFromThread()
    url = "https://news.ycombinator.com/item?id=14437921"
    response = requests.get(url)
    page = str(BeautifulSoup(response.content))
    
    while True:
        url, n = main.extract(page)
        page = page[n:]
        if url:
            print(url)
        else:
            break
