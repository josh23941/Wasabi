'''
Created on Mar 24, 2014

@author: josh23941
'''
from bs4 import BeautifulSoup

''' PULLS LINKS FROM HTML DOCUMENT '''
def get_child_links(html_doc):
    soup = BeautifulSoup(html_doc)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

def init_crawl(target):
    '''STORE TARGET IN DB WITH LEVEL 0'''
    
        
get_child_links('<html><head><title>The Dormouse\'s story</title></head> \
<body> \
<p class="title"><b>The Dormouse\'s story</b></p> \
<p class="story">Once upon a time there were three little sisters; and their names were \
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,\
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and\
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;\
and they lived at the bottom of a well.</p>')

