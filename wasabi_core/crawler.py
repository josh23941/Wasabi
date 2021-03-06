'''
Created on Mar 24, 2014

@author: josh23941
'''
from bs4 import BeautifulSoup
from persistance import Link, add_obj_to_session, query_table
from request import request_url
from urlparse import urlparse, urljoin

#placeholder for config
this_config = {}

''' PULLS LINKS FROM HTML DOCUMENT '''
def get_child_links(html_doc):
    soup = BeautifulSoup(html_doc)
    links = []
    for link in soup.find_all('a'):
        if link.get('href') != None:
            links.append(link.get('href'))
    for link in links:
        print link
    return links

'''
make a request > pull links > store links appropriately > ...?
'''
def crawl(url, parent_url, parent_link_level):
    res = request_url(url)
    if res:
        html_doc = res.read()
        child_links_list = get_child_links(html_doc)
        for link in child_links_list:
        #first make the url absolute if it is not already (checking if it has scheme already)
            link = link.encode('utf8')
            if urlparse(link).scheme == '':
                link = urljoin(parent_url, link)
            #store the link object (the link, its parent, its 'depth' or level
            link_obj = Link(url=link, parent=parent_url, depth=parent_link_level + 1)
            add_obj_to_session(link_obj)
            try:
                if parent_link_level < int(this_config['depth']):
                    crawl(link, url, parent_link_level + 1)
            except:
                print 'Error in crawl(), check that depth is a number in your config'

# this is the entrypoint into the crawler for the actual 'engine'
def start_crawler(config):
    #store the target itself
    global this_config
    this_config = config
    target = this_config['target']
    target_link_obj = Link(url=target, parent='', depth=0)
    add_obj_to_session(target_link_obj)
    
    #kick off the crawl
    crawl(target,target,0)

def crawl_report():
    query_table(Link)

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