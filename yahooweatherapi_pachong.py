#!/usr/bin/env python
#coding=utf-8

import urllib2
import json
from pprint import pprint
from collections import OrderedDict
url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22"
City = raw_input("Press your City:")
values = "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
realurl = url+City+values
urlread = urllib2.urlopen(realurl)
resp = urlread.read()
datadict = json.loads(resp)
pprint(datadict)

hightemp = datadict[u'query'][u'results'][u'channel'][u'item'][u'forecast'][0]["high"]
hightemp = str(hightemp)
hightemp = int(hightemp)
hightempC = ((hightemp)-32.0)//1.8+1

lowtemp = datadict[u'query'][u'results'][u'channel'][u'item'][u'forecast'][0][u'low']
lowtemp = str(lowtemp)
lowtemp = int(lowtemp)
lowtempC = ((lowtemp)-32.0)//1.8+1

todayweather = datadict[u'query'][u'results'][u'channel'][u'item'][u'forecast'][0][u'text']
weatherlist = { 'Showers': u'阵雨', 'Snow': u'雪' ,'Rain': u'雨' , 'Rain And Snow':'雨夹雪', 'Partly Cloudy':'局部阴天'}

print"%s:%s" % (u"今日天气", weatherlist[todayweather])
print"%s:%s%s" % (u"今日最高温度", hightempC, u'°C')
print"%s:%s%s" % (u"今日最低温度", lowtempC,u'°C')

if __name__ == '__mian__':
    main()
