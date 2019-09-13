#!/usr/bin/python
# vim:sw=4:et

import sys

for filename in sys.argv[1:]:
    try:
        compile(open(filename).read(), filename, 'exec')
    except Exception as e:
        print(e)
        exit(1)
