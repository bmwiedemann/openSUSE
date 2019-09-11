# NetWare-specific operations
#
# Copyright (c) 2013 Suse Linux Products.
# Author: Charles Arnold <carnold@suse.com>
#
# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# 51 Franklin St, Boston, MA 02110

# Binary patching of xnloader.sys
# For launching NetWare on Xen 4.2 and newer


import os, sys, base64

CODE_OFFSET=0x49F5
NUMBER_OF_CODE_BYTES=17
ORIGINAL_CODE="BA00080000C786FC1F0000FFFFFFFF31C9"
PATCHED_CODE="BAF8070000834C961CFFB9080000009090"
XNLOADER_SYS_MD5SUM="eb76cce2a2d45928ea2bf26e01430af2"

def patch_netware_loader(loader):
    """Open the given xnloader.sys file and patch the relevant code hunk."""

    # domUloader calls this with all kernels so perhaps this is not the NetWare loader
    md5sum_cmd = 'md5sum ' + loader
    p = os.popen(md5sum_cmd)
    sum = p.read().split()[0]
    p.close()
    if sum != XNLOADER_SYS_MD5SUM:
        return

    try:
        fd = os.open(loader, os.O_RDWR)
    except Exception as e:
        print(e, file=sys.stderr)
        raise

    # Validate minimum size for I/O
    stat = os.fstat(fd)
    if stat.st_size < CODE_OFFSET+NUMBER_OF_CODE_BYTES:
        os.close(fd)
        return

    # Seek to location of code hunk
    os.lseek(fd, CODE_OFFSET, os.SEEK_SET)

    # Read code bytes at offset
    buf = os.read(fd, NUMBER_OF_CODE_BYTES)

    code_as_hex = base64.b16encode(buf)
    code_as_hex = code_as_hex.decode('utf-8')
    if code_as_hex == ORIGINAL_CODE:
        # Seek back to start location of the code hunk
        os.lseek(fd, CODE_OFFSET, os.SEEK_SET)
        # Convert the PATCHED_CODE string to raw binary
        code_as_bin = base64.b16decode(PATCHED_CODE)
        # Write the patched code
        os.write(fd, code_as_bin)
    os.close(fd)

