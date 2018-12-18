#-*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests


'''
类说明:获取网页上单个小说的url（目录页）列表
'''
'''
class Getbookurl:
    def __init__(self):
        pass
'''

'''       
            函数说明：获取小说的目录页
    Parameters:
        url：小说网页
        up_url：上级目录的url
    Returns:无
    Modify:2018-12-4
'''
def getlist(url,up_url):
    print("开始整理小说目录页的url列表，请稍等！")
    req=requests.get(url)
    html=req.text
    div_bf=BeautifulSoup(html,features='lxml')
    div=div_bf.find_all('div', class_='block bd')
    bookurls=[] #小说目录页列表
    booknames=[]#小说名称列表
    for i in range(len(div)):
        a_bf=BeautifulSoup(str(div[i]),features='lxml')
        a=a_bf.find_all('a')    
        booknums=len(a)
        for each in a:
            bookurls.append(up_url+each.get('href'))
            booknames.append(each.string)
    print('小说目录页的url列表整理完成！',bookurls)
    print('所有需要下载的小说',booknames)
    return bookurls,booknames
    