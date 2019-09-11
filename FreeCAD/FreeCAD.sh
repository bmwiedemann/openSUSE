#!/bin/sh
# let Python pick up /usr/lib64/FreeCAD/bin/PySide
cd /usr/lib64/FreeCAD/bin
# temporary workaround for a bug somewhere around python3 in Factory leading to memory corruption
LC_ALL=C ./FreeCAD $@
