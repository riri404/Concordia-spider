# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotetutorialPipeline:
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        self.documents = []

    def close_spider(self, spider):
        # Clustering logic goes here, using self.documents
        pass

    def process_item(self, item, spider):
        self.documents.append(item['page_text'])
        return item
