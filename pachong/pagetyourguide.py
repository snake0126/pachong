import os,urllib2,urllib
import re
from bs4 import BeautifulSoup
import commands

indexPage = "https://www.getyourguide.com/zh/sagrada-familia-l2699/sagrada-familia-skip-the-line-ticket-t50027/"
try:
    request = urllib2.Request(indexPage)
    response = urllib2.urlopen(request)
    htmlPage = response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

Soup = BeautifulSoup(htmlPage)
SoupTitle = Soup.title.string


def getTags(html):
    reg = r'<div class="content list">([\s\S]+?)</div>'
    pattern= re.compile(reg)
    tags= re.findall(pattern, html)
    return tags

getTags(SoupTitle)


#findutf8 = str(Soup.find_all('hed'))
#findChinese = findutf8.encode('UTF-8')
#print SoupTitle
#print findChinese