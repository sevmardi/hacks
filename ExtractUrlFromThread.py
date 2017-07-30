import urllib.request
import time
from bs4 import BeautifulSoup
import urllib.parse

URL = "https://news.ycombinator.com/item?id=14437921"

#
# https://stackoverflow.com/questions/3075550/how-can-i-get-href-links-from-html-using-python

# Objective: Scan a thread of a given site (HN) and save all
# save all the url into a text file.

class ExtractUrlFromThread():
    
    def __construct__(self):
        #self.test()
        pass

    def main(self):
        url = str(input('URL to extract:   '))
        conn = urllib2.urlopen(url)
        html = conn.read()
        # self.extract(urlInput)

    def extract(self, page):
        """
        :param page: html of web page
        :return: urls in that page
        """
        print("Extracting..");
        #loading = time.sleep(5)

        start_link = page.find("www")
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1: end_quote]

        return url, end_quote

    def save_into_file(self, data):
        """Save the urls into a file"""
        try:
            fileObj = open('urls_in_thread', 'w')
            fileObj.write(data)
            fileObj.close()

        except Exception as e:
            print(e)


if __name__ == "__main__":

    main  = ExtractUrlFromThread()
    main.main()    