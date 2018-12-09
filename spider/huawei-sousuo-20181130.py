#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'blue'
# date：20181130

import re
import os
import hashlib
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from requests.exceptions import RequestException

total_page_nums = 9

apk_num_inpage = 0
apk_num_total = 0
apk_num_download = 0
PRINT_MSG = ''
page_url_list = []
base_url = 'http://appstore.huawei.com'
root = r'D:\T\1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}

# 华为搜索
def get_page_list(total_page_nums):
    for page_num in range(1, total_page_nums + 1, 1):
        # page_url = 'http://appstore.huawei.com/search/租车/{}'.format(page_num)  # 1.租车类   总页数为5
        # page_url = 'http://appstore.huawei.com/search/约车/{}'.format(page_num)  # 1.约车类   总页数为6
        # page_url = 'http://appstore.huawei.com/search/租车%20约车/{}'.format(page_num)  # 1.约车类   总页数为6
        # page_url = 'http://appstore.huawei.com/search/社交/{}'.format(page_num)  # 1.社交类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/聊天/{}'.format(page_num)  # 1.聊天类   总页数为6
        # page_url = 'http://appstore.huawei.com/search/交友/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/游戏/{}'.format(page_num)  # 1.聊天类   总页数为6
        # page_url = 'http://appstore.huawei.com/search/网络游戏/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/精灵联盟OL/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/捕鱼游戏王/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/坦克前线/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/王者荣耀/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/开心消消乐/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/绝地求生%20刺激战场/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/迷你世界/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/贪吃蛇大作战/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/神庙逃亡/{}'.format(page_num)  # 1.交友类   总页数为7
        page_url = 'http://appstore.huawei.com/search/植物大战僵尸/{}'.format(page_num)  # 1.交友类   总页数为7
        # page_url = 'http://appstore.huawei.com/search/%E7%BD%91%E7%BB%9C%E6%B8%B8%E6%88%8F/{}'.format(page_num)  # 6.网络游戏类   总页数为5
        page_url_list.append(page_url)
    return page_url_list


def parse_html(page_url_list):
    global PRINT_MSG
    global apk_num_total
    global apk_num_download
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    page_num = 0
    for apk_list_page_url in page_url_list:
        page_num = int(apk_list_page_url.split('/')[-1])
        print(apk_list_page_url)
        print(" ----------========== 爬取第%s页开始 ==========----------" % str(page_num))
        # with open('D:\\T\\1\\wandoujia_BeatifulSoup.txt', 'a+', encoding='utf_8') as ft1:
        #     ft1.write(" ----------========== 爬取第%s页开始 ==========----------" % str(page_num) + '\n')
        try:
            response = requests.get(apk_list_page_url, headers=headers)
        except RequestException:
            print(RequestException.strerror)
        # 1.2设置编码格式
        if response.status_code != 200:
            continue
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "lxml")
        # print(soup.prettify())
        links = soup.select("body > div.lay-body > div.lay-main > div.lay-left.corner > div.unit.nofloat > div.unit-main > div.list-game-app.dotline-btn.nofloat > div.game-info-ico > a")
        apk_num_inpage = 0
        appnames = ""
        try:
            for link in links:
                is_exsit = False
                file_list = []
                apk_num_inpage += 1
                response = requests.get(base_url + link.attrs["href"], headers=headers)
                if response.status_code == 200:
                    response.encoding = 'utf-8'
                    soup = BeautifulSoup(response.text, "lxml")
                    # print(soup.prettify())
                    appnames = soup.select('#bodyonline > div > div.lay-main > div.lay-left.hdn-x > div > div > div.app-info.flt > ul:nth-of-type(1) > li:nth-of-type(2) > p:nth-of-type(1) > span.title')[0].text
                    # print(appnames)
                    developers = soup.select("#bodyonline > div > div.lay-main > div.lay-left.hdn-x > div > div > div.app-info.flt > ul:nth-of-type(2) > li:nth-of-type(3) > span")
                    # print(developers[0]['title'])
                    apk_download_count = soup.select(
                        "#bodyonline > div > div.lay-main > div.lay-left.hdn-x > div > div > div.app-info.flt > ul:nth-of-type(1) > li:nth-of-type(2) > p:nth-of-type(1) > span.grey.sub")[0].text.split('：')[1]
                    # print(apk_download_count)
                    apk_download_url = soup.select('#bodyonline > div > div.lay-main > div.lay-left.hdn-x > div > div > div.app-function.nofloat > a')
                    apk_download_url = re.findall('(http://.*?source=portalsite)', apk_download_url[0]['onclick'], 0)[0]
                    # print(apk_download_url)
                    apk_version = soup.select('#bodyonline > div > div.lay-main > div.lay-left.hdn-x > div > div > div.app-info.flt > ul:nth-of-type(2) > li:nth-of-type(4) > span')[0].text
                    # if(len(developers) != len(appnames)):
                    #     print('应用名个数 != 开发商个数')
                    #     print("appnamesNum:" + str(len(appnames)) + appnames)
                    #     print("developersNum:" + str(len(developers)))
                    for file in os.listdir(r'D:\T\1'):
                        file_list.append(file)
                    for apk_exsit in file_list:
                        if appnames in apk_exsit:
                            is_exsit = True
                    if is_exsit:
                        print(appnames + "_V" + apk_version + "已经存在了")
                        continue
                    download(appnames, apk_download_url, developers, apk_version, apk_download_count)
                else:
                    print('获取应用详细页面失败！！！')
            print(" ----------========== 第%s页爬取完成,共%s个应用 ==========----------" % (str(page_num), str(apk_num_inpage)))
            # with open('D:\\T\\1\\wandoujia_BeatifulSoup.txt', 'a+', encoding='utf_8') as ft1:
            #     ft1.write(" ----------========== 第%s页爬取完成,共爬取%s个应用 ==========----------" % (str(page_num), str(apk_num_inpage)) + '\n')
        except Exception as e:
            print(appnames + " : " + str(e))


def download(appnames, apk_download_url, developers, apk_version, apk_download_count):
    global apk_num_total
    global apk_num_download
    PRINT_MSG = ''
    apk_num_total = apk_num_total + 1
    if (len(apk_download_url) == 0):
        return
    print(str(apk_num_total) + '-' + appnames + '\t' + developers[0]['title'] + '\t' + apk_download_count)
    try:
        if appnames.find('上海') >= 0:
            response = requests.get(apk_download_url, headers=headers)
            if response.status_code == 200:
                apk_md5 = hashlib.md5(response.content).hexdigest()
                if len(developers) > 0:
                    PRINT_MSG = developers[0]['title'] + '\t' + appnames + '\tV' + apk_version + '\t' + apk_md5 + '\t' + apk_download_count + '\t' + apk_download_url
                else:
                    PRINT_MSG = '--** 不存在开发商信息 **--' + '\t' + appnames + '\tV' + apk_version + '\t' + apk_md5 + '\t' + apk_download_count + '\t' + apk_download_url
        elif len(developers) != 0 and (str(developers[0]['title']).find('上海') >= 0):
            response = requests.get(apk_download_url, headers=headers)
            if response.status_code == 200:
                apk_md5 = hashlib.md5(response.content).hexdigest()
                PRINT_MSG = developers[0]['title'] + '\t' + appnames + '\tV' + apk_version + '\t' + apk_md5 + '\t' + apk_download_count + '\t' + apk_download_url
        if (PRINT_MSG != ''):
            print(PRINT_MSG)
            apk_num_download += 1
            with open('D:\\T\\1\\huawei_zuche.txt', 'a+', encoding='utf_8') as ft1:
                ft1.write(PRINT_MSG + '\n')
                ft1.close()
            with open('D:\\T\\1\\%s_V%s.apk' % (appnames.strip().replace(' ', '').replace('|', '').replace('/', '').replace('\\', ''), apk_version), 'wb') as ft:
                # with open('D:\\T\\1\\%s_V%s.apk' % (appnames[i].text.strip().replace(' ', '').replace('|', '').replace('/', '').replace('\\', ''), apk_version[i].text), 'wb') as ft:
                ft.write(response.content)
                ft.close()
    except Exception as e:
        print(appnames + " : " + e)


def main():
    if not os.path.exists(root):
        os.mkdir(root)
    url_page_list = get_page_list(total_page_nums)
    parse_html(page_url_list)
    # pool = Pool()
    # pool.map()


# 1.6 定义一个主程序入口
if __name__ == '__main__':
    main()
