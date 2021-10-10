import scrapy
from googlesearch import search

class BookItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = search(input("search word: "), num_results=int(input("num_results: "))) 
        print(urls)
        #urls = ['https://en.wikipedia.org/wiki/Paris']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):                                                   
        book = BookItem()                                                             
        raw_image_urls = response.css('.image img ::attr(src)').getall()
        raw_image_urls_2 = response.css("div.item.active > img::attr(src)").extract()
        clean_image_urls=[]
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        for img_url_2 in raw_image_urls_2:
            clean_image_urls.append(response.urljoin(img_url_2))
                
        yield {
            'image_urls': clean_image_urls
                }
    def url_join(self, urls, response):
        joined_urls = []
        for url in urls: 
            joined_urls.append(response.urljoin(url))
        return joined_urls
