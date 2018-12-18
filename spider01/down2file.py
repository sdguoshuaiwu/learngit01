from spider01 import downbook
import sys ,random
from time import sleep
'''
本程序内类主要实现调用downbook的downloader类，
逐页下载写入相应文件
'''


class down_file:
    def __init__(self,server,bookurl,bookname):
        self.server=server
        self.bookurl=bookurl
        self.bookname=bookname
        dl = downbook.downloader(server=self.server,bookurl=self.bookurl)
        dl.get_download_url()
        print('《 %s》开始下载：'%self.bookname)
        #for i in range(2):
        for i in range(dl.nums):
            sleep(10+random.random())#添加random时间
            dl.writer(dl.names[i], '%s.txt'%self.bookname, dl.get_contents(dl.urls[i]))
            sys.stdout.write("  %s已下载:%.3f%%" %  (self.bookname,float(i/dl.nums)) + '\r')
            sys.stdout.flush()
        print('《%s》下载完成'%self.bookname)