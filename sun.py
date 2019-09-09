from bs4 import BeautifulSoup
import commands
import xlrd
import os,urllib2,urllib

exlpath="/data/taobao/csv/"
exlfile="sun.xlsx"


######################################################

marketlist=exlpath+exlfile
book = xlrd.open_workbook(marketlist)
sheet=book.sheet_by_name("Sheet1")

for i in range(0, sheet.nrows):
    row = sheet.row_values(i)
    urltext = sheet.cell(i, 0).value.encode('utf-8')
    print urltext
    response = urllib2.urlopen(urltext)
    htmlPage = response.read()
    soup = BeautifulSoup(htmlPage)
    namenum = +1
    filetitle=soup.title.string
    str_list = filetitle.split(" ")
    filenum=str_list[-1]
    path = r'/data/taobao/pic/' + filenum
    print path
    os.mkdir(path)
    for y in soup.find_all(class_="product_img_thumb_img"):
        fileurl=str(y.get('src'))
#        path = r'/data/taobao/pic/' + filenum
#       print path
#        os.mkdir(path)
        namenum += 1
        filename = "%s/%s-%s.jpg" %(path,filenum,namenum)
        print fileurl,filename
        res2 = urllib.urlretrieve(fileurl, filename)
