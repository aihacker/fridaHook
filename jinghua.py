#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'blue'
# date：20181208
import re
import os
import time
import requests
from lxml import etree

url_list = []
section1 = {
    "第一章 燃烧基础知识": {"single_selection": 47, "multiple_selection": 35},
    "第二章 火灾基础知识": {"single_selection": 69, "multiple_selection": 25},
    "第三章 爆炸基础知识": {"single_selection": 54, "multiple_selection": 23},
    "第四章 易燃易爆危险品消防安全知识": {"single_selection": 43, "multiple_selection": 26}
}
section2 = {
    "第一章 概述": {"single_selection":0, "multiple_selection":0},
    "第二章 生产和储存物品的火灾危险性分类": {"single_selection":79, "multiple_selection":30},
    "第三章 建筑分类与耐火等级": {"single_selection":102, "multiple_selection":22},
    "第四章 总平面布局和平面布置": {"single_selection":84, "multiple_selection":28},
    "第五章 防火防烟分区与分隔": {"single_selection":97, "multiple_selection":30},
    "第六章 安全疏散": {"single_selection":84, "multiple_selection":48},
    "第七章 建筑电气防火": {"single_selection":23, "multiple_selection":19},
    "第八章 建筑防爆": {"single_selection":29, "multiple_selection":19},
    "第九章 建筑设备防火防爆": {"single_selection":28, "multiple_selection":13},
    "第十章 建筑装修、保温材料防火": {"single_selection":56, "multiple_selection":15},
    "第十一章 灭火救援设施": {"single_selection":79, "multiple_selection":16}}
section3 = {
    "第一章 概述": {"single_selection":5, "multiple_selection":5},
    "第二章 室内外消防给水系统": {"single_selection":79, "multiple_selection":6},
    "第三章 自动喷水灭火系统": {"single_selection":79, "multiple_selection":4},
    "第四章 水喷雾灭火系统": {"single_selection":35, "multiple_selection":4},
    "第五章 细水雾灭火系统": {"single_selection":48, "multiple_selection":5},
    "第六章 气体灭火系统": {"single_selection":84, "multiple_selection":8},
    "第七章 泡沫灭火系统": {"single_selection":62, "multiple_selection":6},
    "第八章 干粉灭火系统": {"single_selection":41, "multiple_selection":6},
    "第九章 火灾自动报警系统": {"single_selection":88, "multiple_selection":40},
    "第十章 防烟排烟系统": {"single_selection":89, "multiple_selection":22},
    "第十一章 消防应急照明和疏散指示系统": {"single_selection":42, "multiple_selection":12},
    "第十二章 城市消防远程监控系统": {"single_selection":32, "multiple_selection":14},
    "第十三章 建筑灭火器配置": {"single_selection":70, "multiple_selection":18},
    "第十四章 消防供配电": {"single_selection":43, "multiple_selection":15}}
section4 = {
    "第一章 概述": {"single_selection":0, "multiple_selection":0},
    "第二章 石油化工防火": {"single_selection":37, "multiple_selection":17},
    "第三章 地铁防火": {"single_selection":37, "multiple_selection":8},
    "第四章 城市交通隧道防火": {"single_selection":34, "multiple_selection":11},
    "第五章 加油加气站防火": {"single_selection":59, "multiple_selection":13},
    "第六章 发电厂防火": {"single_selection":43, "multiple_selection":12},
    "第七章 飞机库防火": {"single_selection":59, "multiple_selection":14},
    "第八章 汽车库、修车库防火": {"single_selection":114, "multiple_selection":12},
    "第九章 洁净厂房防火": {"single_selection":41, "multiple_selection":23},
    "第十章 信息机房防火": {"single_selection":41, "multiple_selection":8},
    "第十一章 古建筑防火": {"single_selection":27, "multiple_selection":20},
    "第十二章 人民防空工程防火": {"single_selection":80, "multiple_selection":43}}
section5 = {
    "第一章 概述": {"single_selection":9, "multiple_selection":9},
    "第二章 火灾风险识别": {"single_selection":33, "multiple_selection":16},
    "第三章 火灾风险评估方法概述": {"single_selection":25, "multiple_selection":18},
    "第四章 建筑性能化防火设计评估": {"single_selection":38, "multiple_selection":12}}
sections = {
    "第一篇 消防基础知识": section1,
    "第二篇 建筑防火": section2,
    "第三篇 建筑消防设施": section3,
    "第四篇 其他建筑、场所防火": section4,
    "第五篇 消防安全评估": section5
}


def extract_text(section_name, chapter_name, file_name, knowsid, selection_type):
    title_count = re.findall("\d+", file_name)[0]
    file_path = r"C:\Users\xucongxiang\Desktop\消防员考试-2018\注册消防工程师——技术实务-课后练习\1"
    for page in range(1, int(title_count) + 1):
        # http://kaoshi.jhwx.com/index.php?exam-app-lesson-ajax-questions&number=1
        login_url = "http://kaoshi.jhwx.com/index.php?user-app-login"
        url = "http://kaoshi.jhwx.com/index.php?exam-app-lesson-ajax-questions"
        url_list.append(url)
        payload = {
            'number': page
        }
        headers21 = {  # ={}".format(str(page-1)),
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "exam_currentuser=%25C3pm%25A0%25E0%25A9%25A0%2596%2596nX%25AC%25C8%25AA%25D4%259B%25D0%259F%25AC%25AC%259A%25AA%25A1%25CAUt%25ABqgk%2583c%2595ii%2599%2587q%25D9%259F%2594ip%255B%25D6%259C%25D4%25A5%25CA%25A0%25A5%25A9%2596%25AB%25AB%25DD%25A2%25AB%259CYm%25A4%259Bd%2594pW%25CA%25C9h%259E%2599%25C6%2596g%259B%25C7%2599%2595j%2597hhnm%2599q%259Fci%259Djk%2597%2592g%2599gm%2588%25A0%25A9%25A0%259E%259DV%25A9%259E%25D6%25AA%25CA%25A1%25CF%259A%25A7%255Bp%25ABr%2597gsZlk_%2592b%2593df%259F%259Dd%2597%2595%259BVq%25AC%259Dh%2595l%2583%25A4%259C%25AC%25A8%25A1%25A7%25D4%259A%25AB%25A7%25AC%25A2%259A%25C5S%259D%25A9o%2597%259FX%259E%2587%259E%25A7pj%2599q%2583%25A5%25C6%25A4%25AA%25A2%25A4%25A6%25A4%25D5%259A%25A2%25A6%25AB%259B%259E%25C6S%259D%259Fo%2597%259Aj%259A%2596%259Cllm%2594r%25D4l%2592fq%255B%25A8%259D%25AB%25D9%259C%25A8%25A6%25AC%25A5%2596%25D3%259F%25C3%25A3%259A%2588%25A0%25A9%25A0%2596%2594nX%25AC%25D2%25A5%25C8%259C%25CA%2592%25A5%25A1%25AA%2599Z%25A1%25A6simlS%25D4%2596%25D5%25A9%259E%25D5%25D3%25AA%25CF%25D2%25C8%25A0%259F%25A6%25CC%25AB%2583m%25CAkhnili%259Fkolhm%25A4%259Bj%259CX%25A8%25CB%25D8%25A9%25CF%25D4%25D1%259D%259A%255B%259E%25AA%259Bd%2597kYkhm%25A7%25D5%259B%25A9%259F%25A1b%2593%25D5j%25D8m%259E%25DB%25D0g%25D0%25CF%25D4%259D%25AC%25AD%2593Y%259C%25AF; PHPSESSID=6j326iehe7ik8a2ojd9d7m6bp3; exam_knowsid={0}; exam_questype={1}; exam_number=0".format(str(knowsid), str(selection_type)),
            "Host": "kaoshi.jhwx.com",
            "Origin": "http://kaoshi.jhwx.com",
            "Referer": "http://kaoshi.jhwx.com/index.php?exam-app-lesson-paper",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        # proxies = {'http': '180.104.107.46:45700', 'https': '180.104.107.46:45700'}
        # username = "aihacker"
        # password = "nidayede"
        # requests.get(login_url, auth=(username, password))
        response = requests.post(url, data=payload, headers=headers21)

        if response.status_code == 200:
            xpath_obj = etree.HTML(response.text)

            if not os.path.exists(file_path + os.sep + section_name + os.sep + chapter_name):
                os.makedirs(file_path + os.sep + section_name + os.sep + chapter_name)
            full_path = file_path + os.sep + section_name + os.sep + chapter_name + os.sep + file_name + ".txt"
            with open(full_path, "a+", encoding="utf-8") as fp:  # 合法的mode 有r、rb、r+、rb+、w、wb、w+、wb+、a、ab、a+、ab+
                title = xpath_obj.xpath('//h4[@class="title"]/text()')[0].strip()
                print(title, end=" ")
                fp.write(title)
                desc = xpath_obj.xpath('//div[@class="choice"]/p/text()')
                if len(desc) == 0:
                    desc = xpath_obj.xpath('//div[@class="choice"]/text()')
                for item in desc:
                    if len(item.strip()) != 0:
                        if item != desc[0]:
                            print("\t", end="")
                            fp.write("\t")
                        print(item.strip(), "\r\n")
                        fp.write(item.strip() + "\r\n")
                answer = xpath_obj.xpath('//tr[@class="info"]/td/text()')
                if not len(answer) == 0:
                    for item in answer:
                        print(item.strip(), end=" ")
                        fp.write(item.strip())
                    print("\r\n")
                    fp.write("\r\n")
                analyze = xpath_obj.xpath('//table[@class="table table-hover table-bordered"]/tr[2]/td/p/text()')
                if len(analyze) == 0:
                    analyze = xpath_obj.xpath('//table[@class="table table-hover table-bordered"]/tr[2]/td/text()')
                if not len(analyze) == 0:
                    for item in analyze:
                        print(item.strip(), end=" ")
                        fp.write(item.strip())
                mp3 = xpath_obj.xpath('//source[@type="audio/mp3"]/@src')
                if not len(mp3) == 0:
                    for item in mp3:
                        print(item.strip(), end=" ")
                        fp.write(item.strip())
                print("\r\n\r\n")
                fp.write("\r\n\r\n")
                del title
                del desc
                del answer
                del analyze
                del mp3
                # time.sleep(1)
        else:
            print(headers21.get("Cookie")[-10:])
            print(response.status_code)

if __name__ == '__main__':
    knowsid = 5
    for section_name, section_content in sections.items():
        section_ = section_name
        print(section_)
        for chapter_name, selection in section_content.items():
            chapter_ = chapter_name
            print("\t", chapter_)
            print("\t\t", "single_selection: ", selection["single_selection"])
            print("\t\t", "multiple_selection: ", selection["multiple_selection"])
            single_selection = selection["single_selection"]
            multiple_selection = selection["multiple_selection"]
            single_selection_file_name = r"单项选择题（共{}题）".format(str(single_selection))
            multiple_selection_file_name = r"多选题（共{}题）".format(str(multiple_selection))
            extract_text(section_name, chapter_name, single_selection_file_name, knowsid, 1)
            extract_text(section_name, chapter_name, multiple_selection_file_name, knowsid, 2)
            knowsid = knowsid + 2