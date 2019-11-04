# -*- coding: utf-8 -*-
import scrapy


class Test01Spider(scrapy.Spider):
    
    name = 'test01'         # 爬虫名
    allowed_domains = ['www.baidu.com']     # 域名
    start_urls = ['https://www.baidu.com/'] # 爬取地址
    # 上面三行内容也可以改写成函数形式
    # def start_requests(self):
    #     urls = ['https://www.baidu.com/']
        
    #     for url in urls:
    #         yield scrapy.Request(url = url, callback=self.parse)
                

    # 对爬取地址返回内容进行解析
    def parse(self, response):
        # pass
        filename = 'baidu.html'
        with open(filename, 'w', encoding = 'utf-8') as f:
            f.write(response.body.decode())
        print('success')
        self.log('Save file {}'.format(filename))
