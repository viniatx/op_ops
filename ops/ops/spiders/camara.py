from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class CamaraSpider(BaseSpider):
    name = "camara"
    allowed_domains = ["camara.leg.br"]
    start_urls = ('http://www2.camara.leg.br/lista_deputados', )

    DEP_BASE_URL = 'http://www.camara.leg.br/Internet/Deputado/dep_Detalhe.asp?id=%s'

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        values = hxs.select("//option/@value").extract()
        values.remove('')
        for value in values:
            url = self.DEP_BASE_URL % value
            yield Request(url, callback=self.parse_dept)

    def parse_dept(self, response):
        pass
