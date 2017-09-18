from pyquery import PyQuery as pq
import requests
url = 'http://www.t-cat.com.tw/Inquire/International.aspx?billID=%s' % input('請輸入單號:')
r = requests.get(url)
html = pq(r.text)('.tablelist').find('tr')#.eq(1)
good = len(html)
for x in range(1,good):
    print(html.eq(x).text())
