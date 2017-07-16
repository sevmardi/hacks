import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError


class Scraper():
    
    def __construct__(self):
        pass

    def download(self, url, user_agent='zeroH', num_retries=2):
        """
        When the url is passed, this function will
        download the page and return html
        """ 
        print('Downloading: ', url)
        
        request = urllib.request.Request(url)
        request.add_header('User-agent', user_agent)
        
        try:
            html = urllib.request.urlopen(url).read()
        except (URLError, HTTPError, ContentTooShortError) as e:
            print('Download error: ', e.reason)
            html = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    #recrusivly retry 5xx http errors
                    return self.download(url, num_retries - 1)
                    
        print(html)

    def save_into_file(self, data):
        """
        :param data
        :return file
        Saving the urls into file
        """
        pass
    
    
if __name__ == '__main__':
    main = Scraper()
    main.download('https://meetup.com')
    
