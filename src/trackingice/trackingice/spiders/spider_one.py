import scrapy

class TrackingIce(scrapy.Spider):
    name = "Wiki"
    start_urls = ["https://en.wikipedia.org/wiki/List_of_immigration_raids_and_arrests_in_the_second_Trump_presidency"]

    def parse(self, response):
        page = response.url
        filename = f"../../../../data/raw/icetracker.html"
        with open(filename, "wb") as f:
            f.write(response.body)
