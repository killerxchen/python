import urllib.request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
proxy_support = urllib.request.ProxyHandler({'http': 'proxy.huawei.com:8080'})
opener = urllib.request.build_opener(proxy_support)
r = opener.open(url)
urllib.request.install_opener(opener)

print(r.read())
page = urllib.request.urlopen(url)
html = page.read()
soup = BeautifulSoup(html,"html.parser")
print (soup)
