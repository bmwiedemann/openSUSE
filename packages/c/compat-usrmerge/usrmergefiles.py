#!/usr/bin/python3
# Copyright (c) 2021 SUSE LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from itertools import filterfalse, chain, islice
from lxml import etree as ET
from urllib.parse import urljoin
import argparse
import gzip
import hashlib
import io
import logging
import re
import requests
import sys


def parse_repomd(baseurl, what, code):
    url = urljoin(baseurl, 'repodata/repomd.xml')
    repomd = requests.get(url)
    if repomd.status_code != requests.codes.ok:
        return False

    ns = {'r': 'http://linux.duke.edu/metadata/repo'}
    root = ET.fromstring(repomd.content)
    filelists = root.find('.//r:data[@type="{}"]'.format(what), ns)
    location = filelists.find('r:location', ns).get('href')
    sha256_expected = filelists.find('r:checksum[@type="sha256"]', ns).text

    url = urljoin(baseurl, location)
    with requests.get(url, stream=True) as res:
        if res.status_code != requests.codes.ok:
            raise Exception(url + ' does not exist')
        sha256 = hashlib.sha256(res.content).hexdigest()
        if sha256 != sha256_expected:
            raise Exception('checksums do not match {} != {}'.format(sha256, sha256_expected))

        content = gzip.GzipFile(fileobj=io.BytesIO(res.content))

        root = ET.fromstring(content.read())
        code(root)

    return False

def ignored(package):
    # busybox has stuff in / that is normally not there
    return package.startswith('busybox-') or package.endswith("-32bit")

def ddd(a, l):
    if len(a) < l:
        return a

    return chain(islice(a, l), ['...'])


def printaslua(files, name):
    pkgs = dict()
    for fn in sorted(files.keys()):
        pkgs.setdefault(' '.join(ddd(sorted(files[fn]), 5)), set()).add(fn)
    print('{} = {{'.format(name))
    for p in sorted(pkgs.keys()):
        print("-- "+p)
        for fn in sorted(pkgs[p]):
            print('["{}"] = 1,'.format(fn))

    print('}')


def handle_filelists(root):
    files = dict()
#    umr = re.compile(r'^\/(s?bin|lib(?:64)?)/([^/]+)')
    umr = re.compile(r'^\/(s?bin)/([^/]+)')
    ns = {'r': 'http://linux.duke.edu/metadata/filelists'}
    for pn in root.findall(".//r:package", ns):
        package = pn.get('name')
        if ignored(package):
            continue
        for fn in pn.findall("r:file", ns):
            m = umr.match(fn.text)
            if m:
#                print("{}: {} {}".format(package, m.group(1), m.group(2)))
                files.setdefault(fn.text, set()).add(package)

    printaslua(files, 'usrmerge_files')


def handle_requires(root):
    files = dict()
    umr = re.compile(r'^\/(s?bin)/([^/]+)')
    ns = {'c': 'http://linux.duke.edu/metadata/common',
          'r': 'http://linux.duke.edu/metadata/rpm' }
    for pn in root.findall(".//c:package", ns):
        package = pn.find('c:name', ns).text
        if ignored(package):
            continue
        for rn in pn.findall(".//r:requires", ns):
            for fn in rn.findall(".//r:entry", ns):
                r = fn.get('name')
                m = umr.match(r)
                if m:
                    files.setdefault(r,set()).add(package)

    printaslua(files, 'usrmerge_binsbindeps')

def main(args):

    # do some work here
    logger = logging.getLogger("usrmergefiles")
    logger.info("main")

    if args.files:
        parse_repomd(args.url[0], "filelists", handle_filelists)

    if args.requires:
        parse_repomd(args.url[0], "primary", handle_requires)

    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='boilerplate python commmand line program')
    parser.add_argument("--dry", action="store_true", help="dry run")
    parser.add_argument("--debug", action="store_true", help="debug output")
    parser.add_argument("--verbose", action="store_true", help="verbose")
    parser.add_argument("--files", action="store_true", help="dump /bin and /sbin files")
    parser.add_argument("--requires", action="store_true", help="dump requires of /bin and /sbin")
    parser.add_argument("url", nargs='*', help="some file name")

    args = parser.parse_args()

    if args.debug:
        level  = logging.DEBUG
    elif args.verbose:
        level = logging.INFO
    else:
        level = None

    logging.basicConfig(level = level)

    sys.exit(main(args))

# vim: sw=4 et
