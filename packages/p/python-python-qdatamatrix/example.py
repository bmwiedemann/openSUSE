#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This file is part of qdatamatatrix.

qdatamatatrix is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

qdatamatatrix is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with qdatamatatrix.  If not, see <http://www.gnu.org/licenses/>.
"""

from datamatrix import DataMatrix
from qdatamatrix import QDataMatrix
import sys
from qtpy import QtWidgets
import qtpy


def show():
	print(qdm._dm)
	for n, c in qdm._dm.columns:
		print(n, repr(c._rowid))


dm = DataMatrix(length=4)
dm.sorted = False
dm.col1 = range(4)
dm.col3 = ['a', 'b', 'c', 'd']
dm.col2 = ['e', 'f', 'g', 'h']
print(dm)
app = QtWidgets.QApplication(sys.argv)
qdm = QDataMatrix(dm, read_only=False)
qdm.resize(600, 400)
qdm.changed.connect(show)
qdm.show()
sys.exit(app.exec_())
