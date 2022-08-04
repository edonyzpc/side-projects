#! /usr/bin/python3
# -*- coding: utf-8 -*-

from xml.dom.minidom import parseString
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = 'https://www.edony.ink/sitemap-posts.xml'
    head = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'refere': 'https://edony.ink',
    }
    req = Request(url=url, headers=head)
    posts_xml = urlopen(req).read()

    dom_tree = parseString(posts_xml)
    posts = []
    for item in dom_tree.getElementsByTagName("url"):
        post = item.childNodes[0].childNodes[0].data
        print(f"- {post}")
        posts.append(post)

    print(f"- total posts: {len(posts)}")
