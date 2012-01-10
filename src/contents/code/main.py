# -*- coding: utf-8 -*- 
#
#   Copyright (C) 2009 Dirk Sarpe
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License version 2,
#   or (at your option) any later version, as published by the Free
#   Software Foundation
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdecore import i18n
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
import dbus

class Counter(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)

        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)

        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
	
	#self.keystroke = QAction(self)
	#self.keystroke.setShortcut(Qt.Key_D)
	
        self.button = Plasma.PushButton(self.applet)
        self.name = "Counts"
	self.counts = 0
	#self.button.setAction(self.keystroke)
        QObject.connect(self.button, SIGNAL("clicked()"), self.count)
        self.layout.addItem(self.button)
        
        self.resetbutton = Plasma.PushButton(self.applet)
	self.resetbutton.setText("Reset")
        QObject.connect(self.resetbutton, SIGNAL("clicked()"), self.reset)
        self.layout.addItem(self.resetbutton)
        
        self.setLayout(self.layout)

    def count(self):
	self.counts = self.counts + 1
	self.button.setText("%s: %d" % (self.name, self.counts))
    
	
    def reset(self):
	self.counts = 0
	self.button.setText("%s: %d" % (self.name, self.counts))
	
def CreateApplet(parent):
    return Counter(parent)