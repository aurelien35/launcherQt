# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
import MainWindow

application	= QtGui.QApplication(sys.argv)
mainWindow	= MainWindow.MainWindow(application)

mainWindow.show()

application.setQuitOnLastWindowClosed(True)
application.exec_()
