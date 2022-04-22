#! /usr/bin/python3
# -*- coding: utf-8 -*-

import urllib
import urllib.request
from xml.dom.minidom import parseString

if __name__ == "__main__":
    posts_xml = urllib.request.urlopen(
        'https://www.edony.ink/sitemap-posts.xml').read()

    dom_tree = parseString(posts_xml)
    posts = []
    for item in dom_tree.getElementsByTagName("url"):
        post = item.childNodes[0].childNodes[0].data
        print(f"- {post}")
        posts.append(post)

    print(f"- total posts: {len(posts)}")
