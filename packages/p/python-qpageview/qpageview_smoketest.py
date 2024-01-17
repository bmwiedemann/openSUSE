# https://qpageview.org/index.html
import qpageview

from PyQt5.Qt import QApplication
a = QApplication([])

v = qpageview.View()
v.show()
v.loadPdf("qpageview.pdf")

v.close()
a.quit()

print("Sucessfully opened and closed a widget")
