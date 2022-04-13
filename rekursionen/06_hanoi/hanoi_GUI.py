"""GUI für das Spiel der Türme von Hanoi.
"""
__version__ = "1.0.0" # 2022.04
__author__ = "S. Gebert"

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QLineEdit)

# Only needed for access to command line arguments
import sys

from ui.ui_hanoi import Ui_MainWindow
from tower_widget import *
from hanoi import *
from collections import namedtuple
from typing import Optional

DiskSel = namedtuple("DiskSel","tower, position, size")

class HanoiGUI(QMainWindow, Ui_MainWindow):
    towers: list[TowerWidget]
    moveCounter: QLineEdit
    game: HanoiGame
    _game_size: int
    _max_disk_number: int
    _sel_disk: Optional[DiskSel]
    _move_count: int
    

    def __init__(self):
        super().__init__()
        #Setup UI
        self.setupUi(self)
        self.towers = [self.tower0, self.tower1, self.tower2]
        #Setup Game
        self._max_disk_number = 14
        self.game_size = 4
        self._setup_game()

        #setup meta
        self.move_count = 0
    
    @property
    def move_count(self) -> int:
        """Number of moves done, since game start."""
        return self._move_count
    @move_count.setter
    def move_count(self, count: int) -> None:
        self._move_count = count
        self.moveCounter.setText(str(self._move_count))
        self.moveCounter.repaint()
        
    @property
    def game_size(self) -> int:
        """Number of disks the game is played with."""
        self._game_size = max(0, min(14,int(self.gameSize.text())))
        return self._game_size
    @game_size.setter
    def game_size(self, size:int) -> None:
        self._game_size = size
        self.gameSize.setText(str(self._game_size))
        self.gameSize.repaint()

    def reset_count(self):
        self.move_count = 0
    def restart_game(self):
        self.reset_count()
        empty_tower = [Disk(i,-1) for i in range(self._max_disk_number+1)]
        for tower in self.towers:
            tower.update_data(empty_tower)
        self._setup_game()

    def _setup_game(self):
        self.game = HanoiGame(self.game_size)
        self._sel_disk = None
        disks = []
        for i, disk in enumerate(self.game.get_disks(0), start=1):
             disks.append(Disk(i,disk))
        self.towers[0].update_data(disks)
    
    def _tower_clicked(self, t:int):
        if self._sel_disk is not None: #a disk has already been selected
            if self._sel_disk.tower == t: #putting disk back on tower it has been selected from
                self.towers[t].update_data([Disk(self._sel_disk.position,self._sel_disk.size),Disk(0,-1)])
                self._sel_disk = None
            else: #moving disc from another tower, if possible
                move_success: bool = False
                t_left = (t-1)%3 # tower on the left side of t
                t_right = (t+1)%3 # tower on the right side of t
                if self._sel_disk.tower == t_left:
                    if self.game.move_disk(t_left,t): #move from left tower, if possible
                        h = self.game.get_height(t)
                        self.towers[t_left].update_data([Disk(self._sel_disk.position,-1),Disk(0,-1)])
                        self.towers[t].update_data([Disk(h,self._sel_disk.size)])
                        move_success = True
                elif self._sel_disk.tower == t_right:
                    if self.game.move_disk(t_right,t): #move from right tower, if possible
                        h = self.game.get_height(t)
                        self.towers[t_right].update_data([Disk(self._sel_disk.position,-1),Disk(0,-1)])
                        self.towers[t].update_data([Disk(h,self._sel_disk.size)])
                        move_success = True
                if move_success: #move has been successfull
                    self._sel_disk = None
                    self.move_count += 1
        else: #select a disc
            h = self.game.get_height(t)
            if h > 0:
                disk = self.game.get_disk(t,0)
                self._sel_disk = DiskSel(t,h,disk)
                self.towers[t].update_data([Disk(0,disk),Disk(h,-1)])        
    
    def tower0_clicked(self):
        self._tower_clicked(0)
        
    def tower1_clicked(self):
        self._tower_clicked(1)

    def tower2_clicked(self):
        self._tower_clicked(2)
    def solve_clicked(self):
        self.game.solve(self.game_size, 0, 2, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HanoiGUI()
    window.show()
    app.exec_()

    # Your application won't reach here until you exit and the event
    # loop has stopped.
