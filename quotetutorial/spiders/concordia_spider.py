from urllib.parse import urljoin, urlparse
import scrapy
from bs4 import BeautifulSoup
from scrapy.exceptions import CloseSpider


class ConcordiaSpider(scrapy.Spider):
    name = "concordia"
    allowed_domains = ['concordia.ca']
    start_urls = [
        'https://www.concordia.ca'
    ]

    def __init__(self, max_files=10, *args, **kwargs):
        super(ConcordiaSpider, self).__init__(*args, **kwargs)
        self.max_files = int(max_files)
        self.files_downloaded = 0

    def parse(self, response):
        # Increment the counter at the start to count the initial URL as well
        self.files_downloaded += 1
        # Check if the maximum limit has been reached
        if self.files_downloaded > self.max_files:
            raise CloseSpider(reason=f'Reached the maximum limit of {self.max_files} files.')

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting text using BeautifulSoup
        # We extract all the text in the body of the page
        text = soup.get_text(strip=True)
        yield {'page_text': text}

        '''#CSS selector to extract title text
        title = response.css('title::text').get()
        yield {'titletext': title}'''

        # Extract and follow links within the same domain
        internal_links = response.css('a::attr(href)').getall()
        for link in internal_links:
            # Handle relative URLs and filter out external links and mailto links
            absolute_link = urljoin(response.url, link)
            parsed_link = urlparse(absolute_link)
            # Check if the link is a mailto link or not an allowed domain
            if parsed_link.scheme == 'mailto' or not self.allowed_domains[0] in parsed_link.netloc:
                continue
            yield scrapy.Request(absolute_link, callback=self.parse)

        '''for link in internal_links:
            # Handle relative URLs and filter out external links
            absolute_link = urljoin(response.url, link)
            if self.allowed_domains[0] in absolute_link:
                yield scrapy.Request(absolute_link, callback=self.parse)'''

        '''for link in internal_links:
            if link.startswith('https://www.concordia.ca'):
                # Follow the internal link and continue crawling
                yield scrapy.Request(link, callback=self.parse)'''

