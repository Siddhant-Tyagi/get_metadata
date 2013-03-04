from urllib2 import urlopen
from lxml import etree

def meta_tags(url):
    meta_tags = []
    temp = urlopen(url).read()
    tree = etree.HTML(temp)
    meta = tree.xpath("//meta")
    for tag in meta:
        if etree.tostring(tag).find("description") != -1:
           start_quote = etree.tostring(tag).find('"', etree.tostring(tag).find('content=')+1)
           end_quote = etree.tostring(tag).find('"', start_quote+1)
           meta_tags.append(etree.tostring(tag)[start_quote+1:end_quote])
           
    return meta_tags
