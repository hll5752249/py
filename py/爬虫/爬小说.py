import requests
from bs4 import BeautifulSoup as bs
import lxml

def get_book_index(url, headers):
    r = requests.get(url, headers = headers)
    soup = bs(r.text, 'lxml')
    BookName = soup.find("span").text
    BookIndex = soup.body.div.find_all('p')
    print("{}，共{}章".format(BookName, len(BookIndex)))
    return [BookIndex, BookName]

def get_book(href):
    import re
    r1 = requests.get(href)
    soup1 = bs(r1.text, 'lxml')
    read = soup1.body.find_all("div")[1].text
    read = re.sub("[\s\a-z\|\{\}\』\『]", "", readinline, count = 0)
    read = read.split("点此举报")[1].split("加入书签")[0].replace(" ", "")
    return read

def mkdir(path):
    import os
    #移除首尾的空格
    path.strip()  
    #去除末尾的\
    path.rstrip('\\')
    #判断目录是否存在 
    isExists = os.path.exists(path)
    #如果目录不存在，则创建   
    if not isExists:      
        os.makedirs(path)        
        #并提示已创建目录        
        print(path, '创建成功')    
        #否则提示该目录已存在   
    else:     
        print(path, '目录已存在')
        
def safe_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    print(path, "成功保存")

    
url = "https://m.qu.la/booklist/24868.html"
headers = {"user-agent":"Mozilla/5.0 (Macintosh;Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KH    TML, like Gecko) Chrome/17.0.963.56 Safari/53    5.11"}
book = get_book_index(url, headers)[0]

BookIndex = book[0]
BookName = book[1]

path =  "/data/data/com.termux/files/home/py/爬虫" + str(BookName)
mkdir(path)

for i in range(1, len(BookIndex)):
    total = i
    section = BookIndex[i].text    
    href = "https://m.qu.la/" + BookIndex[i].a['href']
    print("开始下载", section, href)
    data = get_book(href)
    path = BookName+'/' + section
    safe_file(path, data)

print(本书下载完成)
