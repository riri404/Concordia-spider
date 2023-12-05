import json
from urllib.parse import urljoin, urlparse

import nltk
import scrapy
from afinn import Afinn
from bs4 import BeautifulSoup
from scrapy.exceptions import CloseSpider
from langdetect import detect
import re


class ConcordiaSpider(scrapy.Spider):
    name = "concordia"
    allowed_domains = ['concordia.ca']
    start_urls = ['https://www.concordia.ca']
    data_map = {}  # Hashmap to store tokens
    afinn = Afinn()  # Initialize Afinn

    def __init__(self, max_files=20, *args, **kwargs):
        super(ConcordiaSpider, self).__init__(*args, **kwargs)
        self.max_files = int(max_files)
        self.files_downloaded = 0

    def clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)
        return text

    def tokenize_text(self, text):
        return nltk.word_tokenize(text)

    def parse(self, response):
        if self.files_downloaded > self.max_files:
            raise CloseSpider(reason=f'Reached the maximum limit of {self.max_files} files.')

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        cleaned_text = self.clean_text(text)

        try:
            if detect(cleaned_text) == 'en':
                self.files_downloaded += 1

                # Sentiment analysis
                sentiment_score = self.afinn.score(cleaned_text)
                tokens = self.tokenize_text(cleaned_text)
                self.data_map[response.url] = {'tokens': tokens, 'sentiment': sentiment_score}

                text_without_numbers = re.sub(r'\d+', '', cleaned_text)
                yield {'page_text': text_without_numbers}

                internal_links = response.css('a::attr(href)').getall()
                for link in internal_links:
                    absolute_link = urljoin(response.url, link)
                    parsed_link = urlparse(absolute_link)
                    if parsed_link.scheme != 'mailto' and self.allowed_domains[0] in parsed_link.netloc:
                        yield scrapy.Request(absolute_link, callback=self.parse)
        except:
            pass

    # def closed(self, reason):
    #     # Save the tokens map to a JSON file when spider is closed
    #     with open('tokens_map.json', 'w') as file:
    #         json.dump(self.tokens_map, file, ensure_ascii=False, indent=4)


