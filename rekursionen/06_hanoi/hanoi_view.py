"""GUI für das Spiel Hanoi.

    nach einer java-version vom Oktober 2020 von Rainer Helfrich)
"""
__version__ = "1.0.0" # 2022.04
__author__ = "S. Gebert"
__all__ = ['TowerView']

from PySide6.QtCore import (Qt, QSize, QRect, QModelIndex)
from PySide6.QtWidgets import (QListView, QItemDelegate, QStyleOptionViewItem, QSizePolicy, QWidget)
from PySide6.QtGui import (QPaintEvent, QPainter, QPen, QBrush, QFont, QColor, QColorConstants)

from hanoi_model import Disk

from collections import namedtuple
Padding = namedtuple("Padding", "top right bottom left")

class DiskDelegate(QItemDelegate):
    colors: list[QColor]
    max_disk_number: int
    _padding: Padding
    _spacing: float #space between disks
    
    def __init__(self, parent=None, max_disk_number:int=14, padding:Padding=Padding(0,0,0,0), spacing:float=0): 
        super().__init__(parent)
        self.colors = [QColorConstants.Svg.black, QColorConstants.Svg.red, QColorConstants.Svg.green,
                       QColorConstants.Svg.blue, QColorConstants.Svg.yellow, QColorConstants.Svg.cyan,
                       QColorConstants.Svg.magenta, QColorConstants.Svg.orange, QColorConstants.Svg.pink,
                       QColorConstants.Svg.gray, QColorConstants.Svg.olivedrab, QColorConstants.Svg.steelblue,
                       QColorConstants.Svg.yellowgreen,QColorConstants.Svg.mediumorchid,QColorConstants.Svg.forestgreen]
        self.max_disk_number = max_disk_number
        self._padding = padding
        self._spacing = spacing
        
    def sizeHint(self, option:QStyleOptionViewItem, index:QModelIndex):
        h = (option.rect.height()-self._padding.top-self._padding.bottom-((self.max_disk_number-2)*self._spacing))/(self.max_disk_number+1)
        if index.data() is None:
            return QSize(0,h)
        disk_size = index.data().size
        scale = (disk_size+1)/self.max_disk_number
        return QSize((option.rect.width()-self._padding.left-self._padding.right)*scale,h)
    
    def paint(self, painter:QPainter, option:QStyleOptionViewItem, index:QModelIndex):
        if index.data() is None: return
        disk_size = index.data().size
        position = index.data().position
        scale = (disk_size+1)/self.max_disk_number
        
        w = (option.rect.width()-self._padding.left-self._padding.right)*scale
        x = (option.rect.width()-self._padding.left-self._padding.right)/2*(1-scale)+self._padding.left+self._spacing
        h = option.rect.height()
        if position == 0:
            y = self._padding.top - h - self._spacing
        else:
            y = self._padding.top+(self.max_disk_number-position)*(h+self._spacing)
               
        painter.save()
        painter.fillRect(QRect(x, y, w, h), QBrush(self.colors[disk_size])) 
        painter.restore()

class TowerView(QListView):
    """Zeichenfläche für die Turmstapel"""
    max_disk_number: int
    padding: Padding
    
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.max_disk_number = 14
        self.setSpacing(5)
        self.padding = Padding(50,20,0,20)
        self.setItemDelegate(DiskDelegate(max_disk_number = self.max_disk_number, padding=self.padding, spacing=self.spacing()))
        self.viewport().setAutoFillBackground( False )
              
    def paintEvent(self, event:QPaintEvent):
        #paint tower
        bar_width = ((self.width()-self.padding.left-self.padding.right)/self.max_disk_number)*0.75
        floor_height = ((self.height()-self.padding.top-self.padding.bottom)/(self.max_disk_number+1))
        
        painter = QPainter(self.viewport())
        brush = QBrush()
        brush.setColor(QColorConstants.Svg.black)
        brush.setStyle(Qt.SolidPattern)
        rect = QRect((self.width()-bar_width)/2, self.padding.top, bar_width,self.height()-self.padding.top)
        painter.fillRect(rect, brush)
        rect2 = QRect(0,self.height()-floor_height+1,self.width(),floor_height)
        painter.fillRect(rect2, brush)
        painter.end()
        super().paintEvent(event)  #paint disks     