#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'blue'
import os
import requests
from multiprocessing import Pool

def temp(i):
        #  https://cn2.okokyun.com/20171128/JQPNBqRh/800kb/hls/HEUm0Cr44867012.ts
    url = "https://cn2.okokyun.com/20171128/JQPNBqRh/800kb/hls/HEUm0Cr4486%03d.ts" % i
    print(url)
    name = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        ts_file = url.split("/")[-1]
        length = len(ts_file)  # 14
        name = url[-length:]
        print(name+":"+str(length))
        with open("./m3u8/{}".format(name), "wb") as fp:
            fp.write(response.content)
        print(name)


def generatemp4(path):
    mp4file = os.path.join(path, "yiren.mp4")
    if os.path.exists(mp4file):
        os.system("del mp4file")
    os.system("copy /b C:\\Users\\xucongxiang\\PycharmProjects\\fridaHook\\tmp\\m3u8\\*.ts {}".format(mp4file))
    if os.path.exists(mp4file):
        # os.system("del *.ts")
        print("ts文件已经删除")
    else:
        print("生成电影失败！！")

if __name__=='__main__':
    pool = Pool(20)
    for i in range(7013):
        pool.apply_async(temp, (i,))
    pool.close()
    pool.join()
    generatemp4(r'C:\Users\xucongxiang\PycharmProjects\fridaHook\tmp\m3u8')
