# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
import MainWindow_ui

class MainWindow(QtGui.QDialog) :

	def __init__(self, application) :
		super(MainWindow, self).__init__(None)

		self.m_ui = MainWindow_ui.Ui_MainWindow()
		self.m_ui.setupUi(self)

		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setGeometry(QtGui.QDesktopWidget().screenGeometry(0))

		# self.m_ui.Launcher.resize(self.m_ui.Launcher.sizeHint())
		self.m_ui.Launcher.m_ui.buttonInternet.clicked.connect(self.startInternet)
		self.m_ui.Launcher.m_ui.buttonSkype.clicked.connect(self.startSkype)
		self.m_ui.Launcher.m_ui.buttonMusic.clicked.connect(self.startMusic)
		self.m_ui.Launcher.m_ui.buttonVideo.clicked.connect(self.startVideo)
		self.m_ui.Launcher.m_ui.buttonLoteli.clicked.connect(self.startLoteli)
		
		self.m_ui.Launcher.m_ui.buttonUSB_1.clicked.connect(self.startUSB_1)
		self.m_ui.Launcher.m_ui.buttonUSB_2.clicked.connect(self.startUSB_2)
		self.m_ui.Launcher.m_ui.buttonUSB_3.clicked.connect(self.startUSB_3)
		self.m_ui.Launcher.m_ui.buttonOffice.clicked.connect(self.startOffice)
		self.m_ui.Launcher.m_ui.buttonPower.clicked.connect(self.startPower)
		
		application.installEventFilter(self)
		
	def mousePressEvent(self, event) :
		self.close()
		
	def eventFilter(self, object, event) :
		if (event.type() == QtCore.QEvent.ApplicationDeactivate) :
			self.close()
		return QtGui.QDialog.eventFilter(self, object, event)
		
	def startInternet(self) :
		os.system("chromium")
		self.close()

	def startSkype(self) :
		os.system("skype")
		self.close()

	def startMusic(self) :
		self.close()

	def startVideo(self) :
		self.close()
		
	def startLoteli(self) :
		self.close()

	def startUSB_1(self) :
		os.system("thunar")
		self.close()

	def startUSB_2(self) :
		self.close()

	def startUSB_3(self) :
		self.close()

	def startOffice(self) :
		self.close()

	def startPower(self) :
		os.system("poweroff -i -f")
		self.close()
