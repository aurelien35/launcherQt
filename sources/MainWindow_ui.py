# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources/MainWindow.ui'
#
# Created: Mon Feb 24 14:41:05 2014
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(652, 458)
        MainWindow.setStyleSheet(_fromUtf8("#backgroundFrame\n"
"{\n"
"    background-color:    rgba(0, 0, 0, 190);\n"
"}\n"
""))
        self.gridLayout = QtGui.QGridLayout(MainWindow)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.backgroundFrame = QtGui.QFrame(MainWindow)
        self.backgroundFrame.setAutoFillBackground(True)
        self.backgroundFrame.setObjectName(_fromUtf8("backgroundFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.backgroundFrame)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 215, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(311, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.Launcher = Launcher(self.backgroundFrame)
        self.Launcher.setAutoFillBackground(True)
        self.Launcher.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Launcher.setFrameShadow(QtGui.QFrame.Raised)
        self.Launcher.setObjectName(_fromUtf8("Launcher"))
        self.gridLayout_2.addWidget(self.Launcher, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(310, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 212, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout.addWidget(self.backgroundFrame, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog", None))

from Launcher import Launcher
