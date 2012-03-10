#!/usr/bin/env python2
# coding=utf-8
import sys
import json
import urllib2

def makequeryurl(word):
    baseurl = 'http://dict.qq.com/dict?q='
    return baseurl + word

def getpage(url):
    request = urllib2.Request(url)
    page = urllib2.urlopen(request)
    return page

def localdict(data):
    for local in data['local']:
        for des in local['des']:
            if type(des) is dict:
                print des['d']
            else:
                print des

if len(sys.argv) < 2:
    print 'Error, please type word.'
page = getpage(makequeryurl(sys.argv[1]))
if page.code is 200:
    data = page.read()
    data = json.loads(data)
    if 'err' in data:
        print 'Not Found.'
    elif 'local' in data:
        localdict(data)
    else:
        print 'Local dict have not this word, but net dict had.'
