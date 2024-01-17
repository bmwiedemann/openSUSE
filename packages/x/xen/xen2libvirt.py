#!/usr/bin/python3
#
# Copyright (C) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see
# <http://www.gnu.org/licenses/>.
#
# Authors:
#     Jim Fehlig <jfehlig@suse.com>
#
# Read native Xen configuration format, convert to libvirt domXML, and
# import (virsh define <xml>) into libvirt.


import sys
import os
import argparse
import re
from xml.etree import ElementTree

try:
    import libvirt
except ImportError:
    print('Unable to import the libvirt module.  Is libvirt-python installed?')
    sys.exit(1)

parser = argparse.ArgumentParser(description='Import Xen domain configuration into libvirt')
parser.add_argument('-c', '--convert-only', help='Convert Xen domain configuration into libvirt domXML, but do not import into libvirt', action='store_true', dest='convert_only')
parser.add_argument('-r', '--recursive', help='Operate recursivelly on all Xen domain configuration rooted at path', action='store_true')
parser.add_argument('-f', '--format', help='Format of Xen domain configuration.  Supported formats are xm and sexpr', choices=['xm', 'sexpr'], default=None)
parser.add_argument('-v', '--verbose', help='Print information about the import process', action='store_true')
parser.add_argument('path', help='Path to Xen domain configuration')


def print_verbose(msg):
    if args.verbose:
        print(msg)


def check_config(path, config):
    isbinary = os.system('file -b ' + path + ' | grep text > /dev/null')

    if isbinary:
        print('Skipping %s (not a valid Xen configuration file)' % path)
        return 'unknown'

    for line in config.splitlines():
        if len(line) == 0 or line.startswith('#'):
            continue
        if line.startswith('<domain'):
            # XML is not a supported conversion format
            break
        if line.startswith('(domain'):
            print('Found sexpr formatted file %s' % path)
            return 'sexpr'
        if '=' in line:
            print('Found xm formatted file %s' % path)
            return 'xm'
        break

    print('Skipping %s (not a valid Xen configuration file)' % path)
    return 'unknown'


def import_domain(conn, path, format=None, convert_only=False):

    f = open(path, 'r')
    config = f.read()
    print_verbose('Xen domain configuration read from %s:\n %s' % (path, config))
    if format is None:
        format = check_config(path, config)

    if format == 'sexpr':
        print_verbose('scrubbing domid from configuration')
        config = re.sub("\(domid [0-9]*\)", "", config)
        print_verbose('scrubbed sexpr:\n %s' % config)
        xml = conn.domainXMLFromNative('xen-sxpr', config, 0)
    elif format == 'xm':
        xml = conn.domainXMLFromNative('xen-xm', config, 0)
    else:
        # Return to continue on to next file (if recursive) 
        return

    f.close()

    # domUloader is no longer available in SLES12, replace with pygrub
    tree = ElementTree.fromstring(xml)
    bl = tree.find('.//bootloader')
    if bl is not None and bl.text is not None and 'domUloader' in bl.text:
        bl.text = 'pygrub'
    xml = ElementTree.tostring(tree)

    print_verbose('Successfully converted Xen domain configuration to '
                  'libvirt domXML:\n %s' % xml)
    if convert_only:
        print(xml)
    else:
        print_verbose('Importing converted libvirt domXML into libvirt...')
        dom = conn.defineXML(xml.decode("utf-8"))
        if dom is None:
            print('Failed to define domain from converted domXML')
            sys.exit(1)
        print_verbose('domXML successfully imported into libvirt')


args = parser.parse_args()
path = args.path

# Connect to libvirt
conn = libvirt.open(None)
if conn is None:
    print('Failed to open connection to the hypervisor')
    sys.exit(1)

if args.recursive:
    try:
        for root, dirs, files in os.walk(path):
            for name in files:
                abs_name = os.path.join(root, name)
                print_verbose('Processing file %s' % abs_name)
                import_domain(conn, abs_name, args.format, args.convert_only)
    except IOError:
        print('Failed to open/read path %s' % path)
        sys.exit(1)
else:
    import_domain(conn, args.path, args.format, args.convert_only)
