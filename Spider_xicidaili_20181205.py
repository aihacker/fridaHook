import requests
from lxml import etree

ip_list = []
url = "http://www.xicidaili.com/nn/1"
baidu_url ="http://kaoshi.jhwx.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
proxies = {
    'http': 'http://103.102.239.97:53281',
    'https': 'https://103.102.239.97:53281'
}
try:
    response = requests.get(url, headers=headers, timeout=3)
    print(response.status_code)
    if response.status_code == 200:
        obj_xpath = etree.HTML(response.text)
        for item in obj_xpath.xpath('//table[@id="ip_list"]//tr')[1:]:
            ip = item.xpath('./td[2]/text()')[0] + ":" + item.xpath('./td[3]/text()')[0]
            print(ip)
            proxies2 = {
                'http': r"http://" + ip,
                'https': r"https://" + ip
            }
            try:
                response2 = requests.get(baidu_url, proxies=proxies2, timeout=5)
                if response2.status_code == 200:
                    print(ip)
                    ip_list.append(ip)
                else:
                    print(ip, response2.status_code)
            except Exception as e:
                print(e)
except Exception as e:
    print(e)
with open("ip.txt", mode="w", encoding="utf-8") as fp:
    fp.write(",".join(ip_list))
print(ip_list)