import os
import requests
from lxml import etree

url = r"http://kaoshi.jhwx.com/index.php?exam-app-lesson"
bas_url = r"http://kaoshi.jhwx.com"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "exam_currentuser=%25C3pm%25A0%25E0%25A9%25A0%2596%2596nX%25AC%25C8%25AA%25D4%259B%25D0%259F%25AC%25AC%259A%25AA%25A1%25CAUt%25ABqgk%2583c%2595ii%2599%2587q%25D9%259F%2594ip%255B%25D6%259C%25D4%25A5%25CA%25A0%25A5%25A9%2596%25AB%25AB%25DD%25A2%25AB%259CYm%25A4%259Bd%2594pW%25CA%25C9h%259E%2599%25C6%2596g%259B%25C7%2599%2595j%2597hhnm%2599q%259Fci%259Djk%2597%2592g%2599gm%2588%25A0%25A9%25A0%259E%259DV%25A9%259E%25D6%25AA%25CA%25A1%25CF%259A%25A7%255Bp%25ABr%2597gsZlk_%2592b%2593df%259F%259Dd%2597%2595%259BVq%25AC%259Dh%2595l%2583%25A4%259C%25AC%25A8%25A1%25A7%25D4%259A%25AB%25A7%25AC%25A2%259A%25C5S%259D%25A9o%2597%259FX%259E%2587%259E%25A7pj%2599q%2583%25A5%25C6%25A4%25AA%25A2%25A4%25A6%25A4%25D5%259A%25A2%25A6%25AB%259B%259E%25C6S%259D%259Fo%2597%259Aj%259A%2596%259Cllm%2594r%25D4l%2592fq%255B%25A8%259D%25AB%25D9%259C%25A8%25A6%25AC%25A5%2596%25D3%259F%25C3%25A3%259A%2588%25A0%25A9%25A0%2596%2594nX%25AC%25D2%25A5%25C8%259C%25CA%2592%25A5%25A1%25AA%2599Z%25A1%25A6simlS%25D4%2596%25D5%25A9%259E%25D5%25D3%25AA%25CF%25D2%25C8%25A0%259F%25A6%25CC%25AB%2583m%25CAkhnili%259Fkolhm%25A4%259Bj%259CX%25A8%25CB%25D8%25A9%25CF%25D4%25D1%259D%259A%255B%259E%25AA%259Bd%2597kYkhm%25A7%25D5%259B%25A9%259F%25A1b%2593%25D5j%25D8m%259E%25DB%25D0g%25D0%25CF%25D4%259D%25AC%25AD%2593Y%259C%25AF; PHPSESSID=6j326iehe7ik8a2ojd9d7m6bp3; exam_knowsid=7; exam_questype=2; exam_number=1",
    "Host": "kaoshi.jhwx.com",
    "Referer": "http://kaoshi.jhwx.com/index.php?exam-app-lesson-paper",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

response = requests.get(url, headers=headers)
base = r"C:\Users\xucongxiang\Desktop\消防员考试-2018\1"
if response.status_code == 200:
    xpath_obj = etree.HTML(response.text)
    for i in range(1, 6):
        sections = xpath_obj.xpath('/html/body/div[3]/div/div/div[2]/table[{}]/tr[1]/td/text()'.format(str(i)))
        for section in sections:
            try:
                if not os.path.exists(os.path.join(base, section)):
                    os.makedirs(os.path.join(base, section))
                print(section)
            except Exception as e:
                print(e)
                pass
            chapters = xpath_obj.xpath('/html/body/div[3]/div/div/div[2]/table[{}]/tr/td/a/text()'.format(str(i)))
            knowsid = 5
            for chapter in chapters:
                print("\t" + chapter)
                if not os.path.exists(os.path.join(base, section, chapter)):
                    os.mkdir(os.path.join(base, section, chapter))
                    # sub_chapters_url = xpath_obj.xpath('/html/body/div[3]/div/div/div[2]/table[{}]/tr[2]/td/a/@href'.format(str(i)))
                    # for item in sub_chapters_url:
                    #     sub_chapters_url = bas_url + os.sep + str(item)
                    #     print(sub_chapters_url)
                    #     headers2 = {
                    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    #         "Accept-Encoding": "gzip, deflate",
                    #         "Accept-Language": "zh-CN,zh;q=0.9",
                    #         "Cache-Control": "max-age=0",
                    #         "Connection": "keep-alive",
                    #         "Cookie": "exam_currentuser=%25C3pm%25A0%25E0%25A9%25A0%2596%2596nX%25AC%25C8%25AA%25D4%259B%25D0%259F%25AC%25AC%259A%25AA%25A1%25CAUt%25ABqgk%2583c%2595ii%2599%2587q%25D9%259F%2594ip%255B%25D6%259C%25D4%25A5%25CA%25A0%25A5%25A9%2596%25AB%25AB%25DD%25A2%25AB%259CYm%25A4%259Bd%2594pW%25CA%25C9h%259E%2599%25C6%2596g%259B%25C7%2599%2595j%2597hhnm%2599q%259Fci%259Djk%2597%2592g%2599gm%2588%25A0%25A9%25A0%259E%259DV%25A9%259E%25D6%25AA%25CA%25A1%25CF%259A%25A7%255Bp%25ABr%2597gsZlk_%2592b%2593df%259F%259Dd%2597%2595%259BVq%25AC%259Dh%2595l%2583%25A4%259C%25AC%25A8%25A1%25A7%25D4%259A%25AB%25A7%25AC%25A2%259A%25C5S%259D%25A9o%2597%259FX%259E%2587%259E%25A7pj%2599q%2583%25A5%25C6%25A4%25AA%25A2%25A4%25A6%25A4%25D5%259A%25A2%25A6%25AB%259B%259E%25C6S%259D%259Fo%2597%259Aj%259A%2596%259Cllm%2594r%25D4l%2592fq%255B%25A8%259D%25AB%25D9%259C%25A8%25A6%25AC%25A5%2596%25D3%259F%25C3%25A3%259A%2588%25A0%25A9%25A0%2596%2594nX%25AC%25D2%25A5%25C8%259C%25CA%2592%25A5%25A1%25AA%2599Z%25A1%25A6simlS%25D4%2596%25D5%25A9%259E%25D5%25D3%25AA%25CF%25D2%25C8%25A0%259F%25A6%25CC%25AB%2583m%25CAkhnili%259Fkolhm%25A4%259Bj%259CX%25A8%25CB%25D8%25A9%25CF%25D4%25D1%259D%259A%255B%259E%25AA%259Bd%2597kYkhm%25A7%25D5%259B%25A9%259F%25A1b%2593%25D5j%25D8m%259E%25DB%25D0g%25D0%25CF%25D4%259D%25AC%25AD%2593Y%259C%25AF; PHPSESSID=6j326iehe7ik8a2ojd9d7m6bp3; exam_knowsid={}; exam_questype=2".format(str(knowsid)),
                    #         "Host": "kaoshi.jhwx.com",
                    #         "Upgrade-Insecure-Requests": "1",
                    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
                    #     }
                    #     knowsid = knowsid + 2
                    #     response = requests.get(sub_chapters_url, headers=headers2)
                    #     if response.status_code == 200:
                    #         xpath_obj2 = etree.HTML(response.text)
                    #         jie1 = xpath_obj2.xpath('/html/body/table/tbody/tr[2]/td[1]/a/text()')[0] + ".txt"
                    #         jie2 = xpath_obj2.xpath('/html/body/table/tbody/tr[2]/td[2]/a/text()')[0] + ".txt"
                    #         print(jie1)
                    #         os.mkdir(os.path.join(base, section, chapter, jie1))
                    #         os.mkdir(os.path.join(base, section, chapter, jie2))
                    #     else:
                    #         print("jie", response.status_code)
else:
    print(response.status_code)

