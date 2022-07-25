#! /usr/bin/python3
# -*- coding: utf-8 -*-

from curses import meta
import os
import argparse
import logging
import json

def cmdline():
    """cmdline parameter"""
    parser = argparse.ArgumentParser(description='Apple Podcast List Parser.')
    parser.add_argument('-f', '--filename', type=str, nargs='?',
                        default="", help='file name to parse')
    return parser.parse_args()

def log_setup():
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
    return logger

def parse_plugin_manifest(filename):
    with open(filename, 'rb') as json_buffer:
        data = json.load(json_buffer)
        return data

def get_plugin_folders(path):
    dirs = list(map(lambda filename: os.path.join("./obsidian/plugins/", filename), os.listdir("./obsidian/plugins/")))
    return list(filter(lambda f: os.path.isdir(f), dirs))

def get_plugins_manifest(root_path):
    dirs = get_plugin_folders(root_path)
    manifests = []
    for dir in dirs:
        manifests.append(os.path.join(dir, "manifest.json"))
    
    return manifests

if __name__ == "__main__":
    logger = log_setup()
    plugins = get_plugin_folders("./obsidian/plugins/")
    logger.debug(plugins)
    plugins_manifests = get_plugins_manifest("./obsidian/plugins/")
    logger.debug(plugins_manifests)
    meta_plugins = {}
    for m in plugins_manifests:
        if os.path.isfile(m):
            logger.debug(m)
            data = parse_plugin_manifest(m)
            if 'authorUrl' in data:
                url = data['authorUrl']
            else:
                url = ''
            meta_plugins[data['name']] = {
                'description': data['description'],
                'version': data['version'],
                'github': url,
                }

    print(meta_plugins)