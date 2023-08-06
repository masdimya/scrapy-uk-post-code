import scrapy
from rightmove_property.items import PostCodeItem


class UkpostcodeSpider(scrapy.Spider):
    name = "ukpostcode"
    allowed_domains = ["ukpostcode.org"]
    post_code_item = PostCodeItem()
    

    def start_requests(self):
        yield scrapy.Request(url = "https://ukpostcode.org/", callback = self.states_list)

    def states_list(self,response):
        states = response.css('.states-list h4')
        for i in range(4):
            url  = states[i].css('a::attr(href)').get()
            yield scrapy.Request(url, callback = self.district_list)
    
    def district_list(self, response):
        districts = response.css('.states-list h4')
        for district in districts:
            url  = district.css('a::attr(href)').get()
            yield scrapy.Request(url, callback = self.post_code_list)


    def post_code_list(self, response):
        rows = response.xpath('//table/tr[position() > 1]')
        for row in rows:
            self.post_code_item['states'] = row.xpath('td[3]/text()').get()
            self.post_code_item['states_abbrv'] = row.xpath('td[4]/text()').get()
            self.post_code_item['city'] = row.xpath('td[1]/a/text()').get()

            self.post_code_item['district'] = row.xpath('td[2]/a/text()').get()
            self.post_code_item['postcode'] = row.xpath('td[5]/a/text()').get()

            
            yield self.post_code_item
        
