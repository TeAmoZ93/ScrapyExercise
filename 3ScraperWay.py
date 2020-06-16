#-*-coding:utf-8 -*-
'''
Created on 2020年1月14日
@author: ZachTao
'''
from bs4 import BeautifulSoup
import requests
import urllib
import random
from lxml import etree
from tqdm import tqdm
import re
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
      'Connection': 'close'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
'Connection': 'close'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',
'Connection': 'close'}]
urls=['https://book.douban.com/top250?start={}'.format(str(i)) for i in range (0,250,25)]
saveDir="e:\Pythoncode\download\\"
picGoal=[]

'''
lxml
'''
def lxml_get(urls):
    for url in urls:
        htmll=requests.get(url,headers=hds[random.randint(0,2)])
        selector=etree.HTML(htmll.text)
        infos=selector.xpath('//tr[@class="item"]')
        for info in infos:
#         //*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[1]/a/img
            pic=info.xpath('td/a/img/@src')[0]
            picGoal.append(pic) 
    
'''
re
'''
def re_get(urls):
    for url in urls:
        htmll=requests.get(url,headers=hds[random.randint(0,2)])
        htm=htmll.text
#         repeach=r'<img data-v-54931436 src=".*?\.jpg" alt class="item_img" />'
        repeach=r'<img src=".*?\.jpg" width="90" />'    #适用豆瓣图片
        pattenn=re.compile(repeach)
        imgpic=re.findall(pattenn, htm) 
#再匹配一次把jpg以外的字符去掉，加入列表
        for picc in imgpic:
            ref=r'http.*?\.jpg'
            reff=re.compile(ref)
            pic=re.findall(reff, picc)
            for air in pic:
                picGoal.append(air)

'''
beautifulsoup
'''  
def BeautifulSoup_get(urls):
    for url in urls:
        res=requests.get(url,headers=hds[random.randint(0,2)])
        soup=BeautifulSoup(res.text,'lxml')
        imgs=soup.select('a > img')
        for img in imgs:
            imgg=img.get('src')
            picGoal.append(imgg)

if __name__=='__main__':
#     BeautifulSoup_get(urls)
    re_get(urls)
#     lxml_get(urls)
    i=1
    for picture in tqdm(picGoal):
        urllib.urlretrieve(picture, saveDir+'%s.jpg'%i) 
        i+=1 
           


