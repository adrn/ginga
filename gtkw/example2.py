#! /usr/bin/env python
#
# example1.py -- Simple, configurable FITS viewer.
#
#[ Eric Jeschke (eric@naoj.org) --
#  Last edit: Fri Jun 22 13:41:34 HST 2012
#]
#
# Copyright (c) 2011-2012, Eric R. Jeschke.  All rights reserved.
# This is open-source software licensed under a BSD license.
# Please see the file LICENSE.txt for details.
#
import sys, os
import logging
import pyfits
import gtk

moduleHome = os.path.split(sys.modules[__name__].__file__)[0]
widgetHome = os.path.join(moduleHome, '..')
sys.path.insert(0, widgetHome)
sys.path.insert(0, moduleHome)

import AstroImage
from FitsImageCanvasGtk import FitsImageCanvas
import FileSelection

STD_FORMAT = '%(asctime)s | %(levelname)1.1s | %(filename)s:%(lineno)d (%(funcName)s) | %(message)s'

class FitsViewer(object):

    def __init__(self, logger):

        self.logger = logger
        self.drawcolors = ['white', 'black', 'red', 'yellow', 'blue', 'green']
        self.select = FileSelection.FileSelection()

        root = gtk.Window(gtk.WINDOW_TOPLEVEL)
        root.set_title("FitsImageCanvas Example")
        root.set_border_width(2)
        root.connect("delete_event", lambda w, e: quit(w))
        self.root = root

        vbox = gtk.VBox(spacing=2)

        fi = FitsImageCanvas(logger)
        fi.enable_autolevels('on')
        fi.enable_zoom('on')
        fi.enable_cuts(True)
        fi.enable_flip(True)
        fi.enable_draw(True)
        fi.set_drawtype('ruler')
        fi.set_drawcolor('blue')
        fi.set_callback('drag-drop', self.drop_file)
        #fi.ui_setActive(True)
        self.fitsimage = fi

        w = fi.get_widget()
        w.set_size_request(512, 512)

        vbox.pack_start(w, fill=True, expand=True)

        hbox = gtk.HBox(spacing=5)

        wdrawtype = gtk.combo_box_new_text()
        self.drawtypes = fi.get_drawtypes()
        index = 0
        for name in self.drawtypes:
            wdrawtype.insert_text(index, name)
            index += 1
        index = self.drawtypes.index('ruler')
        wdrawtype.set_active(index)
        wdrawtype.connect('changed', self.set_drawparams)
        self.wdrawtype = wdrawtype

        wdrawcolor = gtk.combo_box_new_text()
        index = 0
        for name in self.drawcolors:
            wdrawcolor.insert_text(index, name)
            index += 1
        index = self.drawcolors.index('blue')
        wdrawcolor.set_active(index)
        wdrawcolor.connect('changed', self.set_drawparams)
        self.wdrawcolor = wdrawcolor

        wclear = gtk.Button("Clear Canvas")
        wclear.connect('clicked', self.clear_canvas)

        wopen = gtk.Button("Open File")
        wopen.connect('clicked', self.open_file)
        wquit = gtk.Button("Quit")
        wquit.connect('clicked', quit)

        for w in (wquit, wclear, wdrawcolor, wdrawtype, wopen):
            hbox.pack_end(w, fill=False, expand=False)

        vbox.pack_start(hbox, fill=False, expand=False)

        root.add(vbox)

    def get_widget(self):
        return self.root

    def set_drawparams(self, w):
        index = self.wdrawtype.get_active()
        kind = self.drawtypes[index]
        index = self.wdrawcolor.get_active()

        params = { 'color': self.drawcolors[index], }
        self.fitsimage.set_drawtype(kind, **params)

    def clear_canvas(self, w):
        self.fitsimage.deleteAllObjects()

    def load_file(self, filepath):
        image = AstroImage.AstroImage()
        image.load_file(filepath)

        self.fitsimage.set_image(image)
        self.root.set_title(filepath)

    def open_file(self, w):
        self.select.popup("Open FITS file", self.load_file)

    def drop_file(self, fitsimage, paths):
        fileName = paths[0]
        self.load_file(fileName)

    def quit(self, w):
        gtk.main_quit()
        return True

        
def main(options, args):

    logger = logging.getLogger("example2")
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(STD_FORMAT)
    stderrHdlr = logging.StreamHandler()
    stderrHdlr.setFormatter(fmt)
    logger.addHandler(stderrHdlr)

    fv = FitsViewer(logger)
    root = fv.get_widget()
    root.show_all()

    if len(args) > 0:
        fv.load_file(args[0])

    gtk.mainloop()
    
if __name__ == '__main__':
    main(None, sys.argv[1:])

# END