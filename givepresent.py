#!/bin/usr/python

import urllib2

with open('present.txt','r') as f:
	lines = f.readlines()

url = 'http://google.com'

for line in lines:
	header = {'User-agent':line}
	req = urllib2.Request(url,None,header)
	reply = urllib2.urlopen(req).read()
