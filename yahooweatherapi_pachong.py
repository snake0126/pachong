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
#pprint(datadict)

print"%s:%s" % ("today high temp", float(datadict[u'query'][u'results'][u'channel'][u'item'][u'forecast'][0]["high"]-32)/1.8)
print"%s:%s" % ("today low temp", datadict[u'query'][u'results'][u'channel'][u'item'][u'forecast'][0][u'low'])
