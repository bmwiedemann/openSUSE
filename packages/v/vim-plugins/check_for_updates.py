#!/usr/bin/python3

import argparse
import re
import requests
import rpm
import sys
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token')
args = parser.parse_args()

ts = rpm.TransactionSet()
spec = ts.parseSpec('vim-plugins.spec')

ver_re = re.compile(r"https://github\.com/(?P<org>[^/]+)/(?P<repo>[^/]+)/(?:archive/refs/tags|releases/download/(?P<rel>[^/]+))/(?P<ver>[^/]+)\.tar\.gz#")

for src in spec.sources:
    if src[2] != 1: # Source
        continue

    m = ver_re.match(src[0])
    if m is None:
        continue

    org = m.group('org')
    repo = m.group('repo')
    rel = m.group('rel')
    ver = m.group('ver')
    if ver is None:
        continue

    print(colored(f"Checking {org}/{repo} (current rel='{rel}' ver='{ver}')", 'green'))

    url_suffix = 'tags'
    if rel is not None:
        url_suffix = 'releases/latest'
        ver = rel

    headers = {}
    if args.token:
        headers['Authorization'] = f"token {args.token}"
    get = requests.get(f"https://api.github.com/repos/{org}/{repo}/{url_suffix}", headers=headers)
    if not get.ok:
        print(f"bad HTTP reply for {org}/{repo}: {get.status_code} {get.reason}")
        sys.exit(1)

    js = get.json()
    if rel is None:
        js = js[0] # take the latest tag only

    ver2 = js['name'] or js['tag_name']
    if ver != ver2:
        print(colored(f"\t{ver2} available", 'red'))
