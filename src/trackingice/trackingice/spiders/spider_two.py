import scrapy
from trackingice.items import TrackingiceItem

class TrackingIce(scrapy.Spider):
    name = "Tracker"
    start_urls = ["https://en.wikipedia.org/wiki/List_of_immigration_raids_and_arrests_in_the_second_Trump_presidency"]

    def parse(self, response):
        item = TrackingiceItem()
        # item['month'] = response.xpath('//*[@id="January"]').extract()
        # item['section'] = response.xpath('//*[@id="mw-content-text"]/div[2]/p[4]').extract()
        item['year'] = response.xpath("//h2[@id='2025']/text()").get()
        item['month'] = response.xpath("//h3[@id='January']/text()").get()
        item['section'] = response.xpath('//*[@id="mw-content-text"]/div[2]/p[4]').extract()

        return item