#!/usr/bin/env python
#coding=utf-8

import urllib2
import json
from pprint import pprint
from collections import OrderedDict
url = "http://www.sojson.com/open/api/weather/json.shtml?city="
City = raw_input("Press your City:")

realurl = url+City
urlread = urllib2.urlopen(realurl)
resp = urlread.read()
datadict = json.loads(resp)
pprint(datadict)

print "%s:%s" % (u"当前城市", datadict[u'city'])
print "%s:%s" % (u"当天日期", datadict[u'data'][u'forecast'][0][u'date'])
print "%s:%s" % (u"今日天气", datadict[u'data'][u'forecast'][0][u'type'])
print "%s:%s" % (u"当前空气指数", datadict[u'data'][u'forecast'][0][u'aqi'])
print "%s:%s" % (u"今日最高气温", datadict[u'data'][u'forecast'][0][u'high'])
print "%s:%s" % (u"今日最低气温", datadict[u'data'][u'forecast'][0][u'low'])
