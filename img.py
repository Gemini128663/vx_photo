import os
import urllib.request

from datetime import *
from urllib import request

import requests
from bs4 import BeautifulSoup

start = datetime.now()
headers = {"Referer": "Referer: https://mp.weixin.qq.com/",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) "
                         "Chrome/95.0.4638.54 Safari/537.36",}


url = "https://mp.weixin.qq.com/s/r97DWFOohrR_HBfjjFmJrQ"
path = "./photos"
isExists = os.path.exists(path)
if not isExists:
    os.makedirs(path)
    print("创建文件目录成功")
imagepaths = os.listdir(path)  # 图像文件夹
number = len(imagepaths)
res = requests.get(url, headers=headers,)

html = res.text

soup = BeautifulSoup(html, 'lxml')
tags = soup.find_all(name='img')  # 查找img节点

for tag in tags[1:]:

    # print(tag.attrs.get("data-src")) # 查看节点里的data-src属性值
    try:

        img_name = path + "/" + str(number) + "." + tag.attrs.get("data-type")
        img_url = tag.attrs.get("data-src")
        print(img_url)
        urllib.request.urlretrieve(img_url, img_name)
        print("第" + str(number) + "张下载完成.")
        request.urlcleanup()  # 清除urlretrieve()所产生的缓存
        number += 1
    except Exception as e:
        print(e)

end = datetime.now()
print("耗时", end - start)

print(datetime.now())
