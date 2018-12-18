# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
 
"""
类说明:根据提供的网站url（用于程序中url的补全）和小说的目录页url，实现了内容的获取（函数）和文件写入（函数）
Parameters:
    server：网站url（用于程序中url的补全）
    bookurl：小说的目录页url
Returns:
    无
Modify:
    2018-12-4
"""
class downloader(object):
 
    def __init__(self,server,bookurl):
        self.server = server
        self.target = bookurl
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数
 
    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-12-4
    """
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,features='lxml')
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),features='lxml')
        a = a_bf.find_all('a')
        self.nums = len(a[12:])                                #剔除不必要的章节，并统计章节数
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
 
    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2018-12-4
    """
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,features='lxml')
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
 
    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2018-12-4
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
 
