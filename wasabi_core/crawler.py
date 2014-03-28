'''
Created on Mar 24, 2014

@author: josh23941
'''
from bs4 import BeautifulSoup
from persistance import session, Link, add_obj_to_session
from request import request_url
from urlparse import urlparse, urljoin

''' PULLS LINKS FROM HTML DOCUMENT '''
def get_child_links(html_doc):
    soup = BeautifulSoup(html_doc)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    for link in links:
        print link
    return links

'''
make a request > pull links > store links appropriately > ...?
'''
def crawl(url, parent_url, parent_link_level):
    html_doc = request_url(url)
    child_links_list = get_child_links(html_doc)
    for link in child_links_list:
        #first make the url absolute if it is not already (checking if it has scheme already)
        link = link.encode('utf8')
        if urlparse(link).scheme == '':
            link = urljoin(parent_url, link)
        #store the link object (the link, its parent, its 'depth' or level
        link_obj = Link(url=link, parent=parent_url, depth=parent_link_level + 1)
        add_obj_to_session(link_obj)

# this is the entrypoint into the crawler for the actual 'engine'
def start_crawler(target):
    #store the target itself
    target_link_obj = Link(url=target, parent='', depth=0)
    add_obj_to_session(target_link_obj)
    
    #kick off the crawl
    crawl(target,target,0)



'''USING get_child_links      
get_child_links('<html><head><title>The Dormouse\'s story</title></head> \
<body> \
<p class="title"><b>The Dormouse\'s story</b></p> \
<p class="story">Once upon a time there were three little sisters; and their names were \
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,\
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and\
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;\
and they lived at the bottom of a well.</p>')
'''