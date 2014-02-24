# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
import Launcher_ui

class Launcher(QtGui.QFrame) :

	def __init__(self, parent) :
		super(Launcher, self).__init__(parent)

		self.m_ui = Launcher_ui.Ui_Launcher()
		self.m_ui.setupUi(self)

		self.m_ui.buttonInternet.installEventFilter(self)
		self.m_ui.buttonSkype.installEventFilter(self)
		self.m_ui.buttonMusic.installEventFilter(self)
		self.m_ui.buttonVideo.installEventFilter(self)
		self.m_ui.buttonLoteli.installEventFilter(self)
		
		self.m_ui.buttonUSB_1.installEventFilter(self)
		self.m_ui.buttonUSB_2.installEventFilter(self)
		self.m_ui.buttonUSB_3.installEventFilter(self)
		self.m_ui.buttonOffice.installEventFilter(self)
		self.m_ui.buttonPower.installEventFilter(self)
		
	def mousePressEvent(self, event) :
		event.accept()
		
	def eventFilter(self, object, event) :
		if (event.type() == QtCore.QEvent.KeyPress) :
			if (event.key() != QtCore.Qt.Key_Escape) :
				return True
		return QtGui.QFrame.eventFilter(self, object, event)
 