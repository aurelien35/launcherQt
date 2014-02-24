# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources/Launcher.ui'
#
# Created: Mon Feb 24 14:41:04 2014
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

class Ui_Launcher(object):
    def setupUi(self, Launcher):
        Launcher.setObjectName(_fromUtf8("Launcher"))
        Launcher.resize(906, 429)
        Launcher.setAutoFillBackground(False)
        Launcher.setStyleSheet(_fromUtf8("#Launcher\n"
"{\n"
"    border-style:            solid;\n"
"    border-width:             3px;\n"
"    border-radius:            12px;\n"
"    border-color:            #FFFFFF;\n"
"    background-color:    #444444;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color:                        #FFFFFF;\n"
"    font-weight:            bold;\n"
"    font-style:                italic;\n"
"    font-size:                    20pt;\n"
"    font-family:                \"Verdana\"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color:                        #000000;\n"
"    border-style:            inset;\n"
"    border-width:             3px;\n"
"    border-radius:            24px;\n"
"    border-color:            #000000;\n"
"    background-color:    qlineargradient(    spread:pad,\n"
"                                                                x1:0, y1:0,\n"
"                                                                x2:0, y2:1,\n"
"                                                                stop:0        #FFFFFF,\n"
"                                                                stop:1        #D4D4D4);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:                        #000000;\n"
"    border-style:            inset;\n"
"    border-width:             5px;\n"
"    border-radius:            24px;\n"
"    border-color:            #000000;\n"
"    background-color:    qlineargradient(    spread:pad,\n"
"                                                                x1:0, y1:0,\n"
"                                                                x2:0, y2:1,\n"
"                                                                stop:0        #D4D4D4,\n"
"                                                                stop:1        #FFFFFF);\n"
" }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:                        #000000;\n"
"    border-style:            inset;\n"
"    border-width:             4px;\n"
"    border-radius:            24px;\n"
"    border-color:            #000000;\n"
"    background-color:    qlineargradient(    spread:pad,\n"
"                                                                x1:0, y1:0,\n"
"                                                                x2:0, y2:1,\n"
"                                                                stop:0        #CCCCCC,\n"
"                                                                stop:1        #999999);\n"
"}\n"
"\n"
""))
        Launcher.setFrameShape(QtGui.QFrame.StyledPanel)
        Launcher.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(Launcher)
        self.gridLayout_2.setMargin(20)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        spacerItem = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Launcher)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 3)
        self.buttonVideo = QtGui.QPushButton(Launcher)
        self.buttonVideo.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonVideo.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonVideo.setIconSize(QtCore.QSize(96, 96))
        self.buttonVideo.setObjectName(_fromUtf8("buttonVideo"))
        self.gridLayout_6.addWidget(self.buttonVideo, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 3, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        self.label = QtGui.QLabel(Launcher)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.buttonInternet = QtGui.QPushButton(Launcher)
        self.buttonInternet.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonInternet.setMaximumSize(QtCore.QSize(128, 128))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/chrome.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonInternet.setIcon(icon)
        self.buttonInternet.setIconSize(QtCore.QSize(96, 96))
        self.buttonInternet.setObjectName(_fromUtf8("buttonInternet"))
        self.gridLayout_3.addWidget(self.buttonInternet, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_7 = QtGui.QLabel(Launcher)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_9.addWidget(self.label_7, 1, 0, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 0, 0, 1, 1)
        self.buttonUSB_2 = QtGui.QPushButton(Launcher)
        self.buttonUSB_2.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonUSB_2.setMaximumSize(QtCore.QSize(128, 128))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/usb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUSB_2.setIcon(icon1)
        self.buttonUSB_2.setIconSize(QtCore.QSize(96, 96))
        self.buttonUSB_2.setObjectName(_fromUtf8("buttonUSB_2"))
        self.gridLayout_9.addWidget(self.buttonUSB_2, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_9, 1, 1, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        spacerItem6 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Launcher)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 3)
        spacerItem7 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 0, 2, 1, 1)
        self.buttonUSB_1 = QtGui.QPushButton(Launcher)
        self.buttonUSB_1.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonUSB_1.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonUSB_1.setIcon(icon1)
        self.buttonUSB_1.setIconSize(QtCore.QSize(96, 96))
        self.buttonUSB_1.setObjectName(_fromUtf8("buttonUSB_1"))
        self.gridLayout_8.addWidget(self.buttonUSB_1, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        spacerItem8 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem8, 0, 0, 1, 1)
        self.buttonUSB_5 = QtGui.QPushButton(Launcher)
        self.buttonUSB_5.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonUSB_5.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonUSB_5.setIcon(icon1)
        self.buttonUSB_5.setIconSize(QtCore.QSize(96, 96))
        self.buttonUSB_5.setObjectName(_fromUtf8("buttonUSB_5"))
        self.gridLayout_12.addWidget(self.buttonUSB_5, 0, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem9, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(Launcher)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_12.addWidget(self.label_10, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout_12, 1, 4, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(Launcher)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 3)
        spacerItem10 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 0, 0, 1, 1)
        self.buttonMusic = QtGui.QPushButton(Launcher)
        self.buttonMusic.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonMusic.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonMusic.setIconSize(QtCore.QSize(96, 96))
        self.buttonMusic.setObjectName(_fromUtf8("buttonMusic"))
        self.gridLayout_5.addWidget(self.buttonMusic, 0, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem11, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 2, 1, 1)
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        spacerItem12 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem13, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(Launcher)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_11.addWidget(self.label_9, 1, 0, 1, 3)
        self.buttonUSB_4 = QtGui.QPushButton(Launcher)
        self.buttonUSB_4.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonUSB_4.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonUSB_4.setIcon(icon1)
        self.buttonUSB_4.setIconSize(QtCore.QSize(96, 96))
        self.buttonUSB_4.setObjectName(_fromUtf8("buttonUSB_4"))
        self.gridLayout_11.addWidget(self.buttonUSB_4, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_11, 1, 3, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        spacerItem14 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem14, 0, 0, 1, 1)
        self.buttonUSB_3 = QtGui.QPushButton(Launcher)
        self.buttonUSB_3.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonUSB_3.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonUSB_3.setIcon(icon1)
        self.buttonUSB_3.setIconSize(QtCore.QSize(96, 96))
        self.buttonUSB_3.setObjectName(_fromUtf8("buttonUSB_3"))
        self.gridLayout_10.addWidget(self.buttonUSB_3, 0, 1, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem15, 0, 2, 1, 1)
        self.label_8 = QtGui.QLabel(Launcher)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_10.addWidget(self.label_8, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout_10, 1, 2, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem16 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem16, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Launcher)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 3)
        self.buttonSkype = QtGui.QPushButton(Launcher)
        self.buttonSkype.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonSkype.setMaximumSize(QtCore.QSize(128, 128))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/skype.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSkype.setIcon(icon2)
        self.buttonSkype.setIconSize(QtCore.QSize(96, 96))
        self.buttonSkype.setObjectName(_fromUtf8("buttonSkype"))
        self.gridLayout_4.addWidget(self.buttonSkype, 0, 1, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem17, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem18 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem18, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Launcher)
        self.label_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 3)
        self.buttonOffice = QtGui.QPushButton(Launcher)
        self.buttonOffice.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonOffice.setMaximumSize(QtCore.QSize(128, 128))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/libreoffice.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonOffice.setIcon(icon3)
        self.buttonOffice.setIconSize(QtCore.QSize(96, 96))
        self.buttonOffice.setObjectName(_fromUtf8("buttonOffice"))
        self.gridLayout_7.addWidget(self.buttonOffice, 0, 1, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(13, 125, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem19, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_7, 0, 4, 1, 1)

        self.retranslateUi(Launcher)
        QtCore.QMetaObject.connectSlotsByName(Launcher)

    def retranslateUi(self, Launcher):
        self.label_5.setText(_translate("Launcher", "Vidéo", None))
        self.label.setText(_translate("Launcher", "Internet", None))
        self.label_7.setText(_translate("Launcher", "USB", None))
        self.label_4.setText(_translate("Launcher", "USB", None))
        self.label_10.setText(_translate("Launcher", "USB", None))
        self.label_3.setText(_translate("Launcher", "Musique", None))
        self.label_9.setText(_translate("Launcher", "USB", None))
        self.label_8.setText(_translate("Launcher", "USB", None))
        self.label_2.setText(_translate("Launcher", "Skype", None))
        self.label_6.setText(_translate("Launcher", "Office", None))

import resources_rc
