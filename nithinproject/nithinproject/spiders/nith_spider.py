from scrapy import Spider
from scrapy.selector import Selector

from nithinproject.items import NithinprojectItem


class StackSpider(Spider):
    name = "nithinproject"
    allowed_domains = ["theguardian.com"]
    start_urls = [
        "https://www.theguardian.com/world",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="fc-item__header"]/h2')

        for question in questions:
            item = NithinprojectItem()
            item['title'] = question.xpath(
                'a[@class="fc-item__link"]/span[@class="u-faux-block-link__cta fc-item__headline"]/span[@class="js-headline-text"]/text()').extract()
            item['url'] = question.xpath(
                'a[@class="fc-item__link"]/@href').extract()
            yield item

