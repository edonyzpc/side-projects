#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import plistlib as pl
import logging


def cmdline():
    """cmdline parameter"""
    home = os.path.expanduser("~")
    default_apple_podcast_plist = os.path.join(
        home, "Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist")
    parser = argparse.ArgumentParser(description='Apple Podcast List Parser.')
    parser.add_argument('-f', '--filename', type=str, nargs='?',
                        default=default_apple_podcast_plist, help='file name to parse')
    return parser.parse_args()


if __name__ == "__main__":
    # create logger
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    if sys.platform != 'darwin':
        print("only support macOS Podcast app parsing, please make sure run in macOS")
        sys.exit(1)

    args = cmdline()
    logger.debug(args.filename)
    with open(args.filename, 'rb') as buffer:
        lists = pl.load(buffer)
        output = ""
        for item in lists[0]['children'][0]['children']:
            output += f'#### {item["title"]}\nurl: {item["feedUrl"]}\n\n'
        with open("podcast-list.md", 'w', encoding='utf-8') as output_buffer:
            output_buffer.write(output)
