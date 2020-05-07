#!/usr/bin/python3

# This script is licensed under the GPL-3.0-or-later license.

# Automatically group the font files by family names and style names,
# and assume each bitmap font only contains one font face.
# This tool requires ftdump and fonttosfnt.

# Some changes by Hans Ulrich Niedermann and Antonio Larrosa.

import sys
import subprocess

usage = '''
convertfont.py [BITMAPFONTFILE]...
'''

fontnames = dict()

# get font family name and style name by ftdump
def getfullname(fontname):
    output = subprocess.check_output(
        'ftdump ' + fontname,
        shell = True)

    output = output.decode('utf8')
    # only contain one font face
    assert not 'Face number: 1' in output
    result = {}
    for row in output.split('\n'):
        if ':' in row:
            key, value = row.split(': ')
            result[key.strip()] = value.strip()

    familyname, stylename = result['family'], result['style']
    if stylename == 'Regular':
        return familyname
    else:
        return familyname + ' ' + stylename


def generate_fonts():
    for fullname, filenames in fontnames.items():
        outputfilename = fullname.replace(' ', '-')  + '.otb'
        argv = 'fonttosfnt -b -c -g 2 -m 2 -o'.split(' ')
        argv.append(outputfilename)
        argv.extend(filenames)
        print(' '.join(argv))
        print(subprocess.check_output(argv).decode('utf8'))


if __name__ == '__main__':
    for bitmapfontname in sys.argv[1:]:
        fullname = getfullname(bitmapfontname)
        if fullname in fontnames:
            fontnames[fullname].append(bitmapfontname)
        else:
            fontnames[fullname] = [bitmapfontname]

    generate_fonts()
