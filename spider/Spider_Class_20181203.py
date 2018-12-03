import os
import requests
from lxml import etree


class Spider(object):
    def __init__(self):
        self.url = "http://www.mmjpg.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
            "Referer": "http://www.mmjpg.com/"
        }

    def start_request(self):
        for page in range(1, 10):
            if page == 1:
                response = requests.get(self.url, headers=self.headers)
            else:
                response = requests.get(self.url + "home/%d" % page, headers=self.headers)
                print("正在爬去-----第%d页--------------" % page)
            html = etree.HTML(response.content.decode())
            self.xpath_data(html)

    def xpath_data(self, html):
        src_list = html.xpath('//div[@class="pic"]/ul/li/a/img/@src')
        alt_list = html.xpath('//div[@class="pic"]/ul/li/a/img/@alt')
        if not os.path.exists(r"D:/tmp/2/"):
            os.makedirs(r"D:/tmp/2/")
        for src, alt in zip(src_list, alt_list):    # zip
            response = requests.get(src, headers=self.headers)
            file_name = "D:/tmp/2/" + alt + ".jpg"
            print("正在抓取" + file_name)
            # 3.save data
            try:
                with open(file_name, 'wb') as fp:
                    fp.write(response.content)
            except Exception as e:
                print(e)


spider = Spider()
spider.start_request()
