# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('kiview')

from kiview_lib import Window
from kiview.AboutKiviewDialog import AboutKiviewDialog
from kiview.PreferencesKiviewDialog import PreferencesKiviewDialog

import os

# See kiview_lib.Window.py for more details about how this class works
class KiviewWindow(Window):
    __gtype_name__ = "KiviewWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(KiviewWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutKiviewDialog
        self.PreferencesDialog = PreferencesKiviewDialog

        # Code for other initialization actions should be added here.
        self.button1 = self.builder.get_object("button1")

    def on_button1_clicked(self, widget):
        os.system("screen -d -m -L python /usr/lib/python2.7/dist-packages/kiview/visu.py")
