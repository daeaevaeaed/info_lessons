"""GUI-Widget, das einen einzelnen Turm für das Spiel Hanoi anzeigt.
"""
__version__ = "1.0.0" # 2022.04
__author__ = "S. Gebert"
__all__ = ['TowerWidget','Disk']

from PySide2.QtCore import (Qt, QSize, QRect, Signal)
from PySide2.QtWidgets import (QWidget)
from PySide2.QtGui import (QPaintEvent, QPainter, QPen, QBrush, QFont, QColor, QColorConstants)

from collections import namedtuple
Disk = namedtuple("Disk", "position size")
Padding = namedtuple("Padding", "top right bottom left")

class TowerWidget(QWidget):
    """Zeichenfläche für die Turmstapel"""
    max_disk_number: int
    colors: list[QColor]
    _padding: Padding
    _spacing: int
    _data: dict[int,int] #key:position, value:size
    
    clicked = Signal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_disk_number = 14
        self.colors = [QColor("#000000"), QColor("#ff0000"), QColor("#00ff00"),
               QColor("#0000ff"), QColor("#ffff00"), QColor("#00ffff"),
               QColor("#ff00ff"), QColor("#ffa500"), QColor("#ffc0cb"),
               QColor("#808080"), QColor("#6b8e23"), QColor("#4682b4"),
               QColor("#9acd32"),QColor("#ba55d3"),QColor("#228b22")]
        self._spacing = 5
        self._padding = Padding(0,20,0,20)
        self._data = {}
    
    def update_data(self, disks: list[Disk]):
        """Updates model data.
        Args:
            disks: list of disks to be changed. A disk is a tuple (position, size)
                position is the position on the tower and size the size of the disk.
        """
        i_size = 1
        i_position = 0
        for disk in disks:
            if disk[i_size] < 0:
                self._data.pop(disk[i_position],None)
            self._data[disk[i_position]]=disk[i_size]
        self.repaint()
    
    def paintEvent(self, e: QPaintEvent):
        painter = QPainter(self)
 
        h = (self.height()-self._padding.top-self._padding.bottom-((self.max_disk_number)*self._spacing))/(self.max_disk_number+2)
        bar_width = min(h, (self.width()-self._padding.left-self._padding.right)*2/self.max_disk_number)*0.75
        floor_height = h
        
        brush = QBrush()
        brush.setColor(QColor("#000000"))
        brush.setStyle(Qt.SolidPattern)
        bar = QRect((self.width()-bar_width)/2, self._padding.top+2*h, bar_width,self.height()-self._padding.top-h)
        painter.fillRect(bar, brush)
        floor = QRect(0,self.height()-floor_height+1,self.width(),floor_height)
        painter.fillRect(floor, brush)
    
        for position, disk_size in self._data.items():
            scale = (disk_size+1)/self.max_disk_number
            w=(self.width()-self._padding.left-self._padding.right)*scale   
            x = (self.width()-self._padding.left-self._padding.right)/2*(1-scale)+self._padding.left
            if position == 0:
                y = self._padding.top+self._spacing
            else:
                y = self._padding.top+(self.max_disk_number+1-position)*(h+self._spacing)
                    
            painter.fillRect(QRect(x, y, w, h), QBrush(self.colors[disk_size]))       
        painter.end()
    
    def mousePressEvent(self, e):
        self.clicked.emit()