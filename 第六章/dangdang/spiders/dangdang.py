import scrapy

from ..items import DangdangItem
class dangdangspider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.org"]
    start_urls = {
        "http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA%C0%E0&category_path=01.00.00.00.00.00#J_tab"
    }

    def parse(self,response):
        div_list = response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul')
        for sel in div_list :
            item = DangdangItem()
            item['title'] = sel.xpath ('./li/a/@title').extract()
            item['link'] = sel.xpath('./li/a/@href').extract()
            yield item
