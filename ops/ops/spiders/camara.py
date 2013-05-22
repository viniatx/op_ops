from scrapy.spider import BaseSpider

class CamaraSpider(BaseSpider):
    name = "camara"
    allowed_domains = ["camara.leg.br"]
    start_urls = ('http://www2.camara.leg.br/',)

    def parse(self, response):
        pass
