from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from slugify import slugify
from voodoobot.items import VoodooItem
from voodoo.models import Site, Category, SubCategory
from _cffi_backend import callback
from _mysql import NULL

class GuardianSpider(CrawlSpider):
    name = 'guardian'
    start_urls = ['http://www.theguardian.com/football']
    rules = [Rule(LinkExtractor(allow=[r'\d{4}/\w{3,}/\d{2}/[a-z0-9]+(-[a-z0-9]+)*']), follow=True, callback="parse_newspost")]
    
    def parse_newspost(self, response):
        hxs = HtmlXPathSelector(response)
        item = VoodooItem()
        # Extract the article title
        item['title'] = hxs.xpath('//title/text()').extract()
        slug = str(item['title'][0])
        item['slug'] = slugify(slug)
        item['body'] = hxs.xpath('//div[@class="flexible-content-body"]//p/text()').extract()
        item['site'] = Site.objects.get(id=4)
        item['sport_name'] = SubCategory.objects.get(sport_name='Football')
        item['url'] = response.url
        item['image'] = hxs.xpath('//*[@class="gu-image"]/@src').extract()
        
        return item