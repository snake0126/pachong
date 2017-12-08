import os,urllib2,urllib
import re
from bs4 import BeautifulSoup
import commands


postid = range(1201000,1202000)

def getwebtext(text):
    global Soup
    global htmlPage,UrlUser
    UrlUser = "%s%d%s" % ("http://www.moko.cc/post/", text, ".html")
    response = urllib2.urlopen(UrlUser)
    htmlPage = response.read()
    Soup = BeautifulSoup(htmlPage)
    return

def gettitle():
    global SoupTitle,utfSoup
    SoupTitle = Soup.title.string
    filename = SoupTitle.replace(" ", "")
    utfSoup = SoupTitle.encode('UTF-8')
    print utfSoup

def getpic():
    imgre = re.compile(r"""2=.*.jpg""",re.I)
    imglist = imgre.findall(htmlPage)
    print imglist


def createpicname():
    picname = str(Create + 1) + '.jpg'
    realimglist = imglist[Create]
    rrimglist = realimglist.replace('2="', '')
    finename = os.path.join(path, picname)
    urllib.urlretrieve(rrimglist, finename)
    print finename + ' ok!'


for Idnum in postid:
    getwebtext(Idnum)
    gettitle()
    getpic()
    if "noexist_desc.jpg" in htmlPage:
        print "No User"
    elif 'MOKO.CC' in SoupTitle:
        pass
    else:
        print UrlUser
        print utfSoup
        text = str(zip(imglist))
        path = r'/tmp/testmoko/'+str(Idnum)+utfSoup
        os.mkdir(path)
        for Create in xrange(0,len(imglist)):
            createpicname(Create)