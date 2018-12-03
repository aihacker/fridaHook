import os
import requests
from lxml import etree

for page_num in range(102):
    url = "http://www.qiumeimei.com/page/%d" % (page_num+1)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return_txt = response.content.decode()  # 很多情况下的如果直接response.text会出现乱码的问题，所以使用response.content
    # 返回二进制格式数据，然后通过decode()转换为utf-8，这样就解决了通过response.text直接返回显示乱码的问题.
    result = etree.HTML(return_txt)  # change web sourcecode to xml object, this obj can be located by xpath expression
    image_url_list = result.xpath("//div[@class='home_main_wrap']/div/div[2]/p/img/@data-lazy-src")
    base_path = r'D:\tmp\1'  # windows dir symbol use "\" ,use single quot symbol
    if not os.path.exists(r'D:\tmp\1'):
        os.makedirs(r'D:\tmp\1')    # mkdir() different from makedirs() is "tmp" the second dir if not exist will error
    for image_url in image_url_list:    # makedirs 递归创建多级目录，if multi dirs should use makedirs
        image_name = image_url.split('/')[-1]
        image_path = base_path + os.sep + image_name
        if os.path.exists(image_path):
            print("exist image: ", image_name)
            continue
        try:
            with open(image_path, 'ab') as fp:
                response = requests.get(image_url, headers=headers)
                if response.status_code != 200:
                    print(page_num, image_name)
                fp.write(response.content)
                print(page_num+1, "--", image_name)
        except Exception as e:
            print(e)
            pass

# the common use of request lib
# http://www.mamicode.com/info-detail-1827232.html
# response = requests.get("https://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# # print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))
