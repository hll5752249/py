import random
import requests


header_list = [
    #遨游
    {"user-agent" : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
    #火狐
    {"user-agent" : "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
    #谷歌
    {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
]

proxy_list = [
    {"http" : "112.115.57.20:3128"}
    # {"http" : "root:01@124.88.67.81:80"}
]

header = random.choice(header_list)
proxy = random.choice(proxy_list)
url = "https://m.qu.la/booklist/24868.html"
try:
    req=requests.get(url, headers = header,
            proxies=proxy,timeout = 2)
    print(req.text)
except:
    print('no proxies')
