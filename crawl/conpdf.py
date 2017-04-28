# To crawl the pdf

import requests
from bs4 import BeautifulSoup
import os
import time
import socket
import errno
##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上）
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

def savePdf(url, name):
    global headers
    src = 'http://dl.acm.org/'
    pdf_html = requests.get(url, headers = headers)
    Soup = BeautifulSoup(pdf_html.text, 'lxml')
    pdf = src + Soup.find('a', title = 'FullText PDF')['href']
    print("name = %s, pdf = %s"%(name, pdf))
    downloadPdf(name, pdf)
    #一定记得关闭requests
    pdf_html.close()

def downloadPdf(name, url):
    global headers
    path = "D:\\python_Code\\crawl\\Mobicom2016\\"
    name = name.strip().replace(':','_').replace('?','')
    f = open(path + name + '.pdf','ab')
    paper = requests.get(url, headers = headers)
    f.write(paper.content)
    f.close()
    #一定记得关闭requests
    paper.close()
    #睡眠一会儿
    time.sleep(20)
    
def main():
    global headers
    timeout = 20    
    socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
    
    all_url = 'https://www.sigmobile.org/mobicom/2016/program.php'  ##开始的URL地址
    start_html = requests.get(all_url,  headers=headers)

    #print(start_html.text)
    Soup = BeautifulSoup(start_html.text, 'lxml')

    # find the schedule
    all_day = Soup.find_all('div', id='program3') ##意思是先查找 id为 program3 的div标签，然后查找所有的<li>标签。
    count = 1

    # each day's schedule
    for day in all_day:
        all_paper = day.find_all('li')
        for li in all_paper:
            title = li.find('b')
            pdfurl = "None";
            if (title == None):
                title = li.get_text().replace('\n','')
            else:
                title = title.get_text()
                pdfurl = li.find_all('a');
                if (pdfurl != []):
                    #download the pdf
                    pdfurl = pdfurl[-1]['href']
                    savePdf(pdfurl, title)
                    
                    
    start_html.close();


if __name__ == "__main__":
    main();

