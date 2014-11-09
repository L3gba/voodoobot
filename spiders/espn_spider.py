from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from slugify import slugify
from voodoobot.items import VoodooItem
from voodoo.models import Site, Category, SubCategory
from _cffi_backend import callback
from _mysql import NULL

class EspnSpider(CrawlSpider):
    name = 'espn'
    start_urls = ['http://espnfc.us']
    rules = [Rule(LinkExtractor(allow=[r'[A-z0-9]+(-[A-z0-9]+)*/story/\d+/[A-z0-9]+(-[A-z0-9]+)*']), follow=True, callback="parse_newspost")]
    
    def parse_newspost(self, response):
        hxs = HtmlXPathSelector(response)
        item = VoodooItem()
        # Extract the article title
        item['title'] = hxs.xpath('//title/text()').extract()
        slug = item['title']
        item['slug'] = slugify(slug)
        item['body'] = hxs.xpath('//*[@class="above-fold"]//p/text()').extract()
        item['site'] = Site.objects.get(id=3)
        item['sport_name'] = SubCategory.objects.get(sport_name='Football')
        item['url'] = 'http://www.espngc.us'
        item['image'] = hxs.xpath('//*[@class="picture"]/img[@src]').extract()
        
        return item