#!/usr/bin/env python3

import requests
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import os
from datetime import datetime
import re
import tarfile

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.files = []
        self.directories = {}
        self.content = {}
        self.idx = 0
        self.last_time = datetime.strptime('1970-01-01', '%Y-%m-%d')

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr != 'href':
                continue
            if value.endswith("/"):
                self.directories[self.idx] = value
                continue
            elif value.startswith("SKK-JISYO") or value.startswith("ChangeLog") or value == "committers.txt":
                if value != "SKK-JISYO.edict":
                    self.files.append(value)

    def handle_data(self, data):
        patt = re.compile(r'\d+-[A-Za-z]+-\d+')
        match = patt.search(data)
        if match:
            mtime = datetime.strptime(match.group(), "%d-%b-%Y")
            if mtime > self.last_time:
                self.last_time = mtime
        else:
            self.content[self.idx] = data
            self.idx += 1

    def clean_parent(self):
        j = 0
        for i, v in self.directories.items():
            if self.content[i] == 'Parent Directory':
                j = i
                break
        del self.directories[j]

SKKDIC_DIR="./skkdic"
SERVER_PATH="http://openlab.ring.gr.jp/skk/skk/dic/"

def fetch_url(url, files):
    response =  requests.get(url)
    if response.status_code == 200:
        parser = Parser()
        parser.feed(str(response.content))
        parser.clean_parent()
        last_time = parser.last_time
        for file in parser.files:
            files.append(urljoin(url, file))
        if len(parser.directories) > 0:
            for directory in parser.directories.values():
                mtime = fetch_url(urljoin(url, directory), files)
                if mtime > last_time:
                    last_time = mtime
        return last_time

def download_files(files, last_time):
    for file in files:
        relpath = file.replace(SERVER_PATH, "")
        response = requests.get(file)
        if response.status_code == 200:
            dest = os.path.join(SKKDIC_DIR + "-" + last_time, relpath)
            parent = os.path.dirname(dest)
            if not os.path.exists(parent):
                os.makedirs(parent)
            with open(dest, 'wb') as f:
                f.write(response.content)

def remove_dir(directory):
    for f in os.listdir(directory):
        f = os.path.join(directory, f)
        if os.path.isfile(f):
            os.remove(f)
        elif os.path.isdir(f):
            remove_dir(f)
    os.removedirs(directory)

def main():
    files = []
    last_time = datetime.strftime(fetch_url(SERVER_PATH, files), "%Y%m%d")
    download_files(files, last_time)

    dest = SKKDIC_DIR + "-" + last_time

    with tarfile.open(dest + ".tar.xz", 'w:xz') as archive:
        for f in os.listdir(dest):
            archive.add(os.path.join(dest, f))
    
    remove_dir(dest)

main()
