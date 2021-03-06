#
# FitsImageCanvasQt.py -- A FITS image widget with canvas drawing in Qt
# 
# Eric Jeschke (eric@naoj.org)
#
# Copyright (c) Eric R. Jeschke.  All rights reserved.
# This is open-source software licensed under a BSD license.
# Please see the file LICENSE.txt for details.
#
from ginga import FitsImage, Mixins
from ginga.qtw import FitsImageQt
from ginga.qtw.FitsImageCanvasTypesQt import *


class FitsImageCanvasError(FitsImageQt.FitsImageQtError):
    pass

class FitsImageCanvas(FitsImageQt.FitsImageZoom,
                      DrawingMixin, CanvasMixin, CompoundMixin):

    def __init__(self, logger=None, settings=None, render=None):
        FitsImageQt.FitsImageZoom.__init__(self, logger=logger,
                                           settings=settings,
                                           render=render)
        CompoundMixin.__init__(self)
        CanvasMixin.__init__(self)
        DrawingMixin.__init__(self, drawCatalog)

        self.setSurface(self)
        self.ui_setActive(True)

    def canvascoords(self, data_x, data_y, center=True):
        # data->canvas space coordinate conversion
        x, y = self.get_canvas_xy(data_x, data_y, center=center)
        return (x, y)

    def redraw_data(self, whence=0):
        super(FitsImageCanvas, self).redraw_data(whence=whence)

        if not self.pixmap:
            return
        self.draw()

        
#END
