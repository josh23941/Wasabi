'''
Created on Mar 20, 2014

@author: josh23941
'''
import urllib2
import logging

'''
Default Headers
'''
DEFAULT_HEADERS = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',
                   'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language' : 'en-US,en;q=0.5',
                   }

def request_url(url):
    #print "requesting" + url
    request = urllib2.Request(url, None, DEFAULT_HEADERS)
    #print(request.get_method() + ' ' + request.get_full_url() + ' HTTP/1.1')
    #for pair in request.header_items():
    #    print(pair[0] + ": " + pair[1])
    #print
    response = urllib2.urlopen(request)
    #print response.getcode()
    #print response.info()
    #print response.read()
    return response.read()



    