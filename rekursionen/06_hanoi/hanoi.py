"""Das Spiel der Türme von Hanoi.

    Idee nach einer java-version vom Oktober 2020 von Rainer Helfrich
"""
__version__ = "1.1.0" # 2022.04
__author__ = "S. Gebert"
__all__ = ['HanoiGame']

from stack import *

class HanoiGame:
    """Das Spiel Hanoi. Scheiben werden als Ganzahl 1-14 dargestellt. Dabei ist 1 die kleinste und 14 die größte Scheibe.

    Attributes:
        size: Anzahl der Scheiben im Spiel (1-14)
    """
    size: int
    _towers: list[Stack[int]]
    
    def __init__(self, size:int=7):
        self.size = size
        self._towers = [ListStack(),ListStack(),ListStack()]
        for i in range(self.size,0,-1):
            self._towers[0].push(i)
        
    def get_disk(self, t:int, n:int) -> int:
        """Gibt die n-te Scheibe auf Turm t zurück. n wird von oben gezählt, d.h. n = 0 ist die oberste Scheibe.
     
        Args:
            t: Die Nummer des Turmes (0 = links, 1 = mitte, 2 = rechts)
            n: Die Nummer der Scheibe (0 <= n < get_height(t))
        Returns: Die gewünschte Scheibe
        Raises:
            IndexError: Reached bottom of tower, disk does not exist
        """
        temp_stack: Stack = ListStack()
        try:
            while n > 0:
                if self._towers[t].empty():
                        raise IndexError("Reached bottom of tower, disk does not exist")     
                temp_stack.push(self._towers[t].pop())
                n -= 1
            disk = self._towers[t].top()
        finally:
            while not temp_stack.empty():
                self._towers[t].push(temp_stack.pop())
        return disk
    
    def get_disks(self, t:int) -> list[int]:
        """Gibt alle Scheiben auf Turm t zurück.

        Returns: Liste aller Scheiben, wobei die unterste Scheibe zuerst, die oberste zuletzt angefügt wird.
        """
        l = []
        temp_stack: Stack = ListStack()  
        while not self._towers[t].empty():
            temp_stack.push(self._towers[t].pop())
        while not temp_stack.empty():
            l.append(temp_stack.top())
            self._towers[t].push(temp_stack.pop())
        return l
        
    def get_height(self, t:int):
        """Gibt die Höhe des Turms zurück
     
        Args:
            t: Die Nummer des Turmes (0 = links, 1 = mitte, 2 = rechts)
        Returns: Die Höhe des Turms
        """
        h = 0
        temp_stack: Stack = ListStack()  
        while not self._towers[t].empty():
            temp_stack.push(self._towers[t].pop())
            h += 1
        while not temp_stack.empty():
            self._towers[t].push(temp_stack.pop())
        return h
        
    def move_disk(self, src:int, dst:int) -> bool:
        """Verschiebt eine Scheibe von einem Turm auf den anderen, falls der Zug erlaubt ist.
     
        Args:
            src: Die Nummer des Turms (0 = links, 1 = mitte, 2 = rechts), von dem weggezogen wird
            dst: Die Nummer des Turms (0 = links, 1 = mitte, 2 = rechts), auf den hingezogen wird
        Returns: True, falls der Zug erlaubt war; False sonst
        """
        src = src%3
        dst = dst%3
        if src == dst:
            return False
        if self._towers[src].empty():
            return False
        if not self._towers[dst].empty() and self._towers[src].top() > self._towers[dst].top():
            return False
        
        self._towers[dst].push(self._towers[src].pop())
        return True

    def solve(self, number: int, src:int, dst:int, via: int) -> int:
        print("solving")
        if number == 1:
            self.move_disk(src, dst)
        else:
            self.solve(number - 1, src, via, dst)
            self.move_disk(src, dst)
            self.solve(number - 1, via, dst, src)   