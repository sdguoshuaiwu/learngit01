# -*- coding=utf-8 -*-
'''
程序说明：爬虫小说网站的主程序
'''
from spider01 import down2file,get_book_url
from multiprocessing import  Pool


myurl='https://www.biqukan.com/paihangbang/' #这个是排行榜那个网址
myup_url='http://www.biqukan.com'#这个是网站url，用于后面程序的生成url时补全头部
get01=get_book_url #实例化
mybookurllist,mybooknamelist=get01.getlist(url=myurl,up_url=myup_url) #获取小说目录页url的列表、小说名称
book=down2file #实例化

for i in range(len(mybookurllist)):
    book.down_file(myup_url,mybookurllist[i],mybooknamelist[i])  #逐本下载
print("所有下载都已完成")