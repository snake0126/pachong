import os,urllib2,urllib
import re
from bs4 import BeautifulSoup
import commands

postid = range(1201000,1202000)



for Idnum in postid:
    UrlUser = "%s%d%s" %("http://www.moko.cc/post/",Idnum,".html")
    response = urllib2.urlopen(UrlUser)
    htmlPage = response.read()
    Soup = BeautifulSoup(htmlPage)
    SoupTitle = Soup.title.string
    filename = SoupTitle.replace(" ", "")
    #reg = r'http://img1qn.moko.cc/.*.(?:jpg|jpeg)'
    imgre = re.compile(r"""2=.*.jpg""",re.I)
    imglist = imgre.findall(htmlPage)
    utfSoup = SoupTitle.encode('UTF-8')
    if "noexist_desc.jpg" in response.read():
        print "No User"
    elif 'MOKO.CC' in SoupTitle:
        pass
    else:
        #print htmlPage
        print UrlUser
        print utfSoup
        text = str(zip(imglist))
        path = r'/tmp/testmoko/'+str(Idnum)+utfSoup
        os.mkdir(path)
        for Create in xrange(0,len(imglist)):
            picname = str(Create+1) + '.jpg'
            realimglist = imglist[Create]
            rrimglist = realimglist.replace('2="', '')
            #commands.getoutput("mkdir -p"+path)
            #print rrimglist
            #finename = os.path.join(path, picname)
            #realimglist = text.replace('2="', '')
            finename = os.path.join(path, picname)
            #print rrrimglist
            #print("wget -P /tmp/testmoko"+rrimglist)
            #commands.getoutput("wget\ -\P\ /tmp/testmoko"+rrimglist)
            urllib.urlretrieve(rrimglist, finename)
            #print finename + ' ok!'


