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

dm = DataMatrix(length=3)
dm.col1 = 1, 2, 3
dm.col2 = 'a', 'b', 'c'
print(dm)

app = QtWidgets.QApplication(sys.argv)
qdm = QDataMatrix(dm)
qdm.resize(600,400)
# qdm.refresh()
qdm.show()
sys.exit(app.exec_())
