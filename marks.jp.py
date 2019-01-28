#!/usr/bin/env python
#coding=utf-8

import os,urllib2,urllib
import re
from bs4 import BeautifulSoup
import commands
#import print_function

UrlUser=raw_input("输入连接:")
#UrlUser = "%s" %("https://www.online-marks.com/all-EDiT+%E6%89%8B%E5%B8%B3%E3%82%AB%E3%83%90%E3%83%BC+1%E6%97%A51%E3%83%9A%E3%83%BC%E3%82%B8%E7%94%A8+B6%E5%A4%89%E5%9E%8B+%E3%83%A9%E3%82%A6%E3%83%B3%E3%83%89%E3%82%B8%E3%83%83%E3%83%97%E3%82%B1%E3%83%BC%E3%82%B9%E4%BB%98%E3%81%8D%E3%82%B8%E3%83%A3%E3%82%B1%E3%83%83%E3%83%88+%E3%83%AA%E3%83%95%E3%82%A3%E3%83%AB(%E3%83%AC%E3%83%95%E3%82%A3%E3%83%AB)%E5%88%A5%E5%A3%B2%E3%82%8A/brandproduct/all/0/DA-DC41/?cat=902004002&swrd=")
response = urllib2.urlopen(UrlUser)
htmlPage = response.read()
soup = BeautifulSoup(htmlPage)
f1=open('./testfile', 'w+')
print >> f1, soup
filename = "./testfile"
#seapic = "grep jpg %s|grep %s |awk %s > ./seapic.txt" % (filename,"LL","'{print $14}'")
seapic = "grep jpg %s|grep %s " % (filename,"LL")
#seapic = "grep jpg %s|grep %s |awk %s " % (filename,"LL","'{print $20}'")
srcname = os.popen(seapic)
srcread = srcname.read()
srcrepl1 = re.sub('.*src=\"','', srcread)
srcrepl2 = re.sub('jpg.*','', srcrepl1)
srcrepl3 = srcrepl2.replace("\n","")
url1 = srcrepl3
#print url1
url = "%s%s" % (url1,"jpg")
#print url
#print "%s%s" % ("https://www.online-marks.com",url)

##############################################################
#ALL PIC
seapic1 = "grep jpg %s|grep %s " % (filename,"sub")
srcname1 = os.popen(seapic1)
srcread1 = srcname1.read()
#print srcread1
srcrepl11 = re.sub('.*src=\"','', srcread1)
srcrepl21 = re.sub('.jpg.*','', srcrepl11)
#print srcrepl21
srcrepl31 = srcrepl21.replace("\n","L.jpg\n")
url11 = srcrepl31
#print url11
url2 = "%s" % (url11)
#savefile = "echo %s > ./fileline.txt" % (url2)
#os.system(savefile)
fileline = open("./fileline.txt",'w')
fileline.write(url2)
fileline.close()
################################################################
#NAME
seaname = "grep jpg %s|grep %s " % (filename,"LL")
srcname2 = os.popen(seaname)
srcread2 = srcname2.read()
srcrepl13 = re.sub('.*src=\"','', srcread2)
srcrepl23 = re.sub('jpg.*','', srcrepl13)
srcrepl33 = re.sub('.*/','', srcrepl23)
replacename = re.sub('_.*','', srcrepl33)
print replacename

################################################################
#prise
prise = "grep productPrice %s|grep %s " % (filename, "span")
priline = os.popen(prise)
priread = priline.read()
prinum1 = re.sub('.*<span>', '', priread)
prinum2 = re.sub('\<\/sp.*', '', prinum1)
prinum3 = re.sub('\,', '', prinum2)
prinum4 = prinum3.replace("\n","")

#################################################################
#SAVE PIC
namerepl = replacename.replace("\n","")
path = r'/data/taobao/pic/'+namerepl
#print path
os.mkdir(path)
filelineop = open("./fileline.txt")
namenum = 1
for line in filelineop:
    newline = "%s%s" % ("https://www.online-marks.com",line)
    print newline
    pathrepl = path.replace("\n","")
    print pathrepl
    namenum += 1
    picpath = "%s%s%s%s%s%s%s" % (pathrepl,"/",namenum,namerepl,"-",namenum,".jpg")
    print picpath
    res2 = urllib.urlretrieve(newline , picpath)
#    txtpath = "%s%s%s%s" % (pathrepl,"/",namerepl,".txt")

#################################################################
#SAVE TXT
txtpath = "%s%s%s%s" % (pathrepl,"/",namerepl,".txt")
fileinfo = "%s %s%s %s %s" % ("Name:", namerepl, "\nPrise:", prinum4, "JPY\n")
prisefile=open(txtpath, 'w+')
prisefile.write(fileinfo)
prisefile.close
