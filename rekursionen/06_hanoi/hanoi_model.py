"""GUI für das Spiel Hanoi.

    nach einer java-version vom Oktober 2020 von Rainer Helfrich)
"""
__version__ = "1.0.0" # 2022.04
__author__ = "S. Gebert"
__all__ = ['TowerModel', 'Disk']

from PySide6.QtCore import (Qt, QPoint, QAbstractListModel, QModelIndex)
from PySide6.QtGui import (QPainter, QColor)
from collections import namedtuple

Disk = namedtuple("Disk", "position size")

class TowerModel(QAbstractListModel):
    max_disk_number: int
    _data: dict[int,int] #key:position, value:size
    
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.max_disk_number = 14
        self._data = {}
        
    def rowCount(self, parent:QModelIndex=QModelIndex()):
        return self.max_disk_number

    def data(self, index, role:Qt.DisplayRole=Qt.DisplayRole):
        if not index.isValid():
            return None
        if index.row() not in self._data:
            return None
        if role == Qt.DisplayRole:
            return Disk(index.row(),self._data[index.row()])
        return None
    
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
        self.layoutChanged.emit()