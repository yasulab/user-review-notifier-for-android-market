#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import difflib
from lxml import etree
JAPANESE = "ja"
ENGLISH = "en"

def create_url(app_name, lang):
    url = "https://market.android.com/details?id="
    url += app_name
    if lang == JAPANESE:
        url += "&hl=ja"
    elif lang == ENGLISH:
        url += "&hl=en"        
    return url

def get_reviews(url):
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
        # If returned 404
        print "404 Not Found" + BR
        return

    opener = urllib2.build_opener()
    page = opener.open(url)
    charset = page.headers.getparam('charset')
    html_unicode = unicode(html, charset)
    et = etree.fromstring(html_unicode, parser=etree.HTMLParser())
    review_list = []
    for elem in et.xpath("//div[@class='doc-review']"):
        text =  etree.tostring(elem, method="text", encoding="utf-8")
        review_list.append(text)
    if not review_list:
        text = "There are no reviews yet.\n"
        review_list.append(text)
    return review_list
                                                                            
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    if argv_len == 2:
        app_name = sys.argv[1].lower()
        url_ja = create_url(app_name, JAPANESE)
        url_en = create_url(app_name, ENGLISH)
        review_list = get_reviews(url_ja) + get_reviews(url_en)
        result = []
        for r in review_list:
            if not r in result:
                result.append(r)
        for r in result:
            print r
            
