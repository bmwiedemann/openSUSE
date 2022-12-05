#! /usr/bin/env python3
"""
Synopsis:
Fetch and generate ethercodes data for arpwatch

Usage: {appname} [-hVvfkt][-T sec][-O ouifile][-o outfile][-p spec]
       -h, --help           this message
       -V, --version        print version and exit
       -v, --verbose        verbose mode (cumulative)
       -f, --force          force operation
       -k, --keep           keep existing {ouifile}
       -t, --timestamp      print timestamp
       -T, --deltat sec     tolerance in timestamp comparison
                            (default: {deltat} sec.)
       -O, --ouifile file   IEEE.org host
                            (default: {ouifile})
       -o, --outfile file   arpwatch ethercodes
                            (default: {outfile})
       -p, --patch spec     patch specfile with updated timestamp

Description:
Fetch current IEEE MA-L Assignments file (oui.csv) from IEEE.org,
and generate ethercodes.dat for arpwatch consumption.

Fetch oui.csv only, if the timestamp is newer (unless --force is given).
Similar, generate ethercodes.dat only, if the timestamps don't match
(again, unless --force is given). Use option --keep to (re)generate
ethercodes.dat from an existing oui.csv.

Patch replaces a pattern NNNNNNNN_NNNNNN with the current timestamp
in the given file.

Notes:
The timestamps of oui.csv fluctuate in a 2 seconds range(!). Therefore
compensate the fluctuation by taking a deltat tolerance factor into
account.

Copyright:
(c)2018 by {author} {email}

License:
{license}
"""
#
#

__version__ = '0.3'
__author__ = 'Hans-Peter Jansen'
__email__ = '<hpj@urpla.net>'
__license__ = 'MIT'


import os
import re
import csv
import sys
import time
import getopt
import traceback
import email.utils
import urllib.error
import urllib.parse
import urllib.request

# avoid encoding issues with print() in locale-less environments
os.environ["PYTHONIOENCODING"] = "utf-8"

class gpar:
    """ global parameter class """
    appdir, appname = os.path.split(sys.argv[0])
    if appdir == '.':
        appdir = os.getcwd()
    pid = os.getpid()
    version = __version__
    author = __author__
    email = __email__
    license = __license__
    loglevel = 0
    force = False
    keep = False
    timestamp = False
    deltat = 2.5
    ouifile = 'http://standards-oui.ieee.org/oui/oui.csv'
    outfile = 'ethercodes.dat'
    patchfile = None


def vout(lvl, msg):
    if lvl <= gpar.loglevel:
        print((msg).format(**gpar.__dict__), file = sys.stdout, flush = True)

stderr = lambda *msg: print(*msg, file = sys.stderr, flush = True)

def exit(ret = 0, msg = None, usage = False):
    """ terminate process with optional message and usage """
    if msg:
        stderr('{}: {}'.format(gpar.appname, msg))
    if usage:
        stderr(__doc__.format(**gpar.__dict__))
    sys.exit(ret)


def cmp_ts(t1, t2):
    """ compare timestamps while taking a global tolerance factor into
        account
        return True, if timestamps match
    """
    return abs(t1 - t2) < gpar.deltat


hex = lambda x: int(x, 16)
hexstr = lambda h: format(h, 'x')

def code_key(val):
    """ return the colon formated code key, if val is an exact 24 byte
        hexadecimal string, and None otherwise
        000000 -> 0:0:0
        ABCDEF -> ab:cd:ef
    """
    if len(val) == 6:
        return ':'.join((map(hexstr, map(hex, (val[:2], val[2:4], val[4:])))))


def fetch_infile(infile):
    # check oui.csv parameter
    vout(1, 'check {ouifile}')
    req = urllib.request.urlopen(gpar.ouifile)
    vout(3, 'header info: {}'.format(req.info()))
    header = req.info()
    ouisize = int(header['Content-Length'])
    vout(1, 'oui file size: {}'.format(ouisize))
    ouidate = header['Last-Modified']
    vout(1, 'oui file date: {}'.format(ouidate))
    ouidate = email.utils.parsedate(ouidate)
    ouitime = time.mktime(ouidate)
    vout(3, 'parsed oui file date: {} ({})'.format(
            time.asctime(ouidate), ouitime))

    # check, if local oui.csv is outdated
    fetchoui = False
    if gpar.force:
        fetchoui = True
    elif not os.path.exists(infile):
        vout(1, 'no local file {infile} found')
        fetchoui = True
    elif os.path.getsize(infile) != ouisize:
        vout(1, 'local file size differs: {} vs. {} remote'.format(
                os.path.getsize(infile), ouisize))
        fetchoui = True
    elif not cmp_ts(os.stat(infile).st_mtime, ouitime):
        vout(3, str(os.stat(infile).st_mtime))
        vout(3, str(ouitime))
        mtime = time.localtime(os.stat(infile).st_mtime)
        otime = time.localtime(ouitime)
        vout(1, 'local file date differs: {} vs. {} remote'.format(
                time.asctime(mtime), time.asctime(otime)))
        fetchoui = True
    # fetch oui.csv
    if fetchoui:
        vout(1, 'fetch {ouifile}')
        content = req.read()
        lines = content.split(sep=b'\r')
        heading = lines.pop(0).replace(b'\n', b'', 1)

        sort_dict = {}
        for line in lines:
            stripped = line.replace(b'\n', b'', 1)
            items = stripped.split(b',', 3)
            if len(stripped) == 0:
                continue
            OUI = items[1].decode('ascii').lower()
            if OUI in sort_dict:
                sort_dict[OUI].append(stripped)
            else:
                sort_dict[OUI] = [stripped]

        with open(infile, 'wb') as f:
            CRLF = b'\r\n'
            f.write(heading)
            f.write(CRLF)
            for OUI in sorted(sort_dict.keys()):
                items = sort_dict[OUI]
                for item in items:
                    f.write(item)
                    f.write(CRLF)
                        
        os.utime(infile, (ouitime, ouitime))

    return ouidate


def parse_csv(infile):
    vout(1, 'parse {infile}')
    codes = {}
    with open(infile, newline = '', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            vout(3, str(row))
            # generate
            code = code_key(row[1])
            if code:
                if code in codes and codes[code] != row[2]:
                    vout(1, 'value {} exists already: "{}", "{}"'.format(
                            code, codes[code], row[2]))
                else:
                    codes[code] = row[2]
    return codes


def patch_file(patchfile, timestamp):
    vout(1, 'patch {}'.format(patchfile))
    with open(patchfile, 'r+', encoding = 'utf-8') as f:
        content = f.read()
        patched, count = re.subn('\d{8}_\d{6}', timestamp, content)
        if count and content != patched:
            f.seek(0)
            f.write(patched)
            vout(1, '{} occurances replaced in {}'.format(count, patchfile))
        else:
            vout(1, '{} unchanged'.format(patchfile))


def fetch_ethercodes():
    # extract file argument from URL
    gpar.infile = os.path.basename(urllib.parse.urlparse(gpar.ouifile).path)
    # default: oui.csv
    infile = gpar.infile
    # default: ethercodes.dat
    outfile = gpar.outfile
    if gpar.keep:
        if os.path.exists(infile):
            # force generation of ethercodes.dat from existing oui.csv
            gpar.force = True
            ouidate = time.localtime(os.stat(infile).st_mtime)
        else:
            exit(1, 'keep option selected, but no {infile}')
    else:
        ouidate = fetch_infile(infile)
    ouitime = time.mktime(ouidate)

    # check, if ethercodes.dat is outdated
    gencodes = False
    if gpar.force:
        gencodes = True
    elif not os.path.exists(outfile):
        vout(1, 'no local file {} found'.format(outfile))
        gencodes = True
    elif not cmp_ts(os.stat(outfile).st_mtime, ouitime):
        vout(3, str(os.stat(outfile).st_mtime))
        vout(3, str(ouitime))
        mtime = time.localtime(os.stat(outfile).st_mtime)
        otime = time.localtime(ouitime)
        vout(2, 'local file date differs: {} vs. {} remote'.format(
                time.asctime(mtime), time.asctime(otime)))
        gencodes = True

    # generate ethercodes.dat
    if gencodes:
        codes = parse_csv(infile)
        gpar.nrcodes = len(codes)
        vout(1, 'generate {outfile} with {nrcodes} entries')
        with open(outfile, 'w', newline = '', encoding = 'utf-8') as f:
            for key in sorted(codes.keys()):
                f.write('%s\t%s\n' % (key, codes[key]))
        os.utime(outfile, (ouitime, ouitime))
        vout(1, 'successful')
    else:
        vout(1, 'code file {outfile} up to date already')

    timestamp = time.strftime('%Y%m%d_%H%M%S', ouidate)
    if gpar.timestamp:
        vout(0, 'timestamp: {}'.format(timestamp))

    if gpar.patchfile is not None:
        patch_file(gpar.patchfile, timestamp)

    return 0


def main(argv = None):
    if argv is None:
        argv = sys.argv[1:]

    # yeah, oldschool, I know...
    try:
        optlist, args = getopt.getopt(argv, 'hVvfktT:O:o:p:',
            ('help', 'version', 'verbose', 'force', 'keep', 'timestamp',
             'deltat', 'ouifile', 'outfile', 'patch')
        )
    except getopt.error as msg:
        exit(1, msg, True)

    for opt, par in optlist:
        if opt in ('-h', '--help'):
            exit(usage = True)
        elif opt in ('-V', '--version'):
            exit(msg = 'version %s' % gpar.version)
        elif opt in ('-v', '--verbose'):
            gpar.loglevel += 1
        elif opt in ('-f', '--force'):
            gpar.force = True
        elif opt in ('-k', '--keep'):
            gpar.keep = True
        elif opt in ('-t', '--timestamp'):
            gpar.timestamp = True
        elif opt in ('-T', '--deltat'):
            gpar.deltat = par
        elif opt in ('-O', '--ouifile'):
            gpar.ouifile = par
        elif opt in ('-o', '--outfile'):
            gpar.outfile = par
        elif opt in ('-p', '--patch'):
            gpar.patchfile = par

    try:
        fetch_ethercodes()
    except Exception:
        exit(2, 'unexpected exception occured:\n%s' % traceback.format_exc())


if __name__ == '__main__':
    sys.exit(main())
# vim: ts=8 shiftwidth=8 expandtab
