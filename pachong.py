import urllib2

postid = range(1201000,1202000)


for Idnum in postid:
    #Idnum += 1
    UrlUser = "%s%d%s" %("http://www.moko.cc/post/",Idnum,".html")
    response = urllib2.urlopen(UrlUser)
    if "noexist_desc.jpg" in response.read():
        print "No User"
    else:
        print UrlUser


