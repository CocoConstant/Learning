import requests
from bs4 import BeautifulSoup
import bs4

def gethtmltext(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillunivlist(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            univ = tds[1].find('a').string
            ulist.append([tds[0].string, univ, tds[4].string])
    pass

def printunivlist(ulist, num):
    tplt = "{0:^10}{1:{3}^10}{2:^10}"
    print(tplt.format('序号', '学校名称', '分数', chr(12288)))
    for i in range(num):
        u = ulist[i]
        a = u[0].strip()
        b = u[1].strip()
        c = u[2].strip()
        print(tplt.format(a, b, c, chr(12288)))

def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/202211'
    html = gethtmltext(url)
    fillunivlist(uinfo, html)
    printunivlist(uinfo, 30)

main()