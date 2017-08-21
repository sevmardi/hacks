import re

class SiteMapCrawler():
	"""docstring for SiteMapCrawler"""
	def __init__(self, arg):
		super(SiteMapCrawler, self).__init__()
		self.arg = arg

	def download(self, url, user_agent='wswp', num_retries=2, charset='utf-8'):
		print('Downloading..', url)
		request = urllib.request.Request(url)
		request.add_header('User-agent', user_agent)
		try:
			resp = urllib.request.urlopen(request)
			cs = resp.headers.get_content_charset()
			if not cs:
				cs = charset
			html = resp.read().decode(cs)
		except (URLError, HTTPError, ContentTooShortError) as e:
			print('Download error:', e.reason)
			html = None
			if num_retries > 0:
				if hasattr(e, 'code') and 500 <= e.code < 600:
					# recursively retry 5xx HTTP errors
					return download(url, num_retries-1)
		return html

	def crawl_sitemap(self, url):
		#download the sitemap file
		sitemap = self.download(url)
		#extract the sitemap links 
		links = re.findall('<loc>(.*?)</loc>', sitemap)
		# Download each link 
		for link in links:
			html = self.download(link)
			# scrap html here
			#... 

	def crawl_site(self, max_errors=5):
		for page in itertools.count(1):
			pg_url = '{}{}'.format(url, page)
			html = self.download(pg_url)
			if html is None:
				num_errors +=1
				if num_errors == max_errors:
					# max errors reached, exit loop 
					break
				else:
					num_errors = 0
			#	Success - can scrape the result



if __name__ == '__main__':
	SiteMapCrawler()