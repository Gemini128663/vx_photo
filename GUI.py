import urllib.request
import threading
import os
import requests
from tkinter import *
from bs4 import BeautifulSoup
from urllib import request
from datetime import *
import tkinter as tk

class gui:
    def __init__(self, root):
        self.root = root

    def set(self):
        self.root.title("微信公众号<背景小生>壁纸采集")
        self.root.minsize("500", "300")
        self.root.maxsize("500", "300")
        self.lable = Label(self.root, text="URL :").place(x=40, y=50)
        self.lable1 = Label(self.root, text="文件保存在同级目录下photos文件内").place(x=120,y=20)
        self.entry = Entry(self.root, width=50)
        self.entry.place(x=80, y=50)
        self.button = Button(self.root, text="开始采集", command=lambda: self.thread_it(self.spyider)).place(x=220, y=85)

        self.sb = Scrollbar(self.root)  # 滚动条
        self.sb.pack(side='right', fill='y')
        self.lb = Listbox(self.root)
        self.lb.config(yscrollcommand=self.sb.set)
        self.lb.pack(side='bottom', fill=BOTH)  # fill = BOTH 用来横向铺满整个窗口，side=bottom放置在窗口底部
        self.sb.config(command=self.lb.yview)

    def spyider(self):
        start = datetime.now()
        url = self.entry.get()
        path = "./photo"
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            self.lb.insert('end', '文件目录创建成功')
        imagepaths = os.listdir(path)
        number = len(imagepaths)
        res = requests.get(url)
        html = res.text

        soup = BeautifulSoup(html, 'lxml')
        print(soup)
        tags = soup.find_all(name='img')

        for tag in tags[1:]:
            try:
                img_name = path + "/" + str(number) + "." + tag.attrs.get("data-type")
                img_url = tag.attrs.get('data-src')
                urllib.request.urlretrieve(img_url, img_name)
                self.lb.insert('end', "第" + str(number) + "张下载完成.")
                request.urlcleanup()
                number += 1
            except TypeError:
                pass
        end = datetime.now()
        self.lb.insert('end', '全部下载完成', '耗时:', end - start)

    def thread_it(self, func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()


root = tk.Tk()
vx = gui(root)
vx.set()
root.mainloop()
