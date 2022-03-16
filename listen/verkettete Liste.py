"""Implementierung einer Verketteten Liste

Für Python umgesetzt nach einer Java Version von Rainer Helfrich Oktober 2020.
"""
__version__ = "1.0" # 2022.03
__author__ = "D. Bieg"
__all__ = ['List','ListIterativ']

from operator import getitem
from typing import Optional
from collections.abc import Collection 

# from abc import abstractmethod

class Listnode():
    """Ein Listen.
    
    Attributes:
        daten: Der Datenwert des Listenknotens.
        nachfolger: Der Nachfolger des Listenknotens.
    """
    data: object
    successor: Optional['Listnode']
    
    def __init__(self, daten, nachfolger):
        self.data = daten
        self.successor = nachfolger

    def __str__(self):
        return str(self.data)
        
class List():
    """Abstrakte Liste

    Attributes:
        anfang: Der erste Knoten der Liste
    """
    
    def __bool__(self) -> bool:
        """Gibt zurück, ob die Liste leer ist.

        Returns:
            True, falls die Liste leer ist; False sonst
        """
        return self.anfang == None
    
             
    def __getitem__(self, index: int) -> object:
        """Gibt den n-ten Wert (0-basierte Zählweise) der Liste zurück.
        
        Attr:
            index: Der Index des gewünschten Elements
        Returns:
            Den n-ten Wert
        :raises:
            KeyError: Index not found
        """
        pass
    
    def __setitem__(self, index:int, value:object) -> None:
        """Ändert den Wert an der gegebenen Stelle (0-basierte Zählweise) der Liste.

        Attr:
            index: Der Index des zu ändernden Elements
            value: Der neue Wert
        :raises:
            KeyError: Index not found
        """
        pass
    
    def __contains__(self, value: object) -> bool:
        """Gibt zurück, ob ein Wert sich in der Liste befindet

        Atrr:
            value: Der zu suchende Wert
        Returns:
            True, falls der Wert enthalten ist; False sonst
        """
        pass

    """__iter__ kann zusätzlich implementiert werden, damit z.B. die for-Schleife mit der Liste funktioniert."""
    
    def __len__(self) -> int:
        """Gibt die Anzahl der Elemente der Liste zurück."""
        pass
    
    def append(self, value: object) -> None:
        """Hängt einen neuen Wert hinten an die Liste an.

        Attr:
            value: Der anzuhängende Wert
        """
        pass 
    
    def insert(self, index: int, value: object) -> None:
        """Fügt einen neuen Wert an einer gewünschten Stelle in die Liste ein.
        
        Attr:
            index: Die Stelle, an der der neue Wert stehen soll (0 <= index <= len)
            value: Der einzufügende Wert
        """
        
    def remove(self, index: int) -> None:
        """ Entfernt das Element, das an der angegeben Stelle steht, aus der Liste.
        
        Attr:
            index: Die Stelle, von der der Wert entfernt werden soll
        """
        pass
    
    def __str__(self):
        """Gibt die Listenelemente hintereinander auf der Konsole aus."""
        return " ".join([str(e) for e in self]) # type: ignore
        
class ListIterativ(List):
    """Iterative Implementierung einer Verketteten Liste"""
    
    def __init__(self):
        self.anfang = None
        
        

    def append(self, value: object) -> None:
        if not self.anfang:
            self.anfang = Listnode(value, None)
            return
        prev_node = None
        next_node = self.anfang
        while next_node is not None:
            prev_node = next_node
            next_node = next_node.successor
        prev_node.successor = Listnode(value, None)
        
    def __iter__(self):
        current_node = self.anfang
        while current_node is not None:
            yield current_node.data
            current_node = current_node.successor
               
    def __getitem__(self, index: int) -> object:
        current_node = self.anfang
        # print(index)
        if index > 0:
            if self.anfang is not None:
                position = 0
                while position != index:
                    position +=1
                    current_node = current_node.successor
                return current_node.data
            elif self.anfang is None:
                return current_node.data
            
    def __setitem__(self, index:int, value:object) -> None:
        next_node = self.anfang
        counter = 0
        while index > counter:
            counter += 1
            next_node = next_node.successor
        next_node.data = value
        """Ändert den Wert an der gegebenen Stelle (0-basierte Zählweise) der Liste.

        Attr:
            index: Der Index des zu ändernden Elements
            value: Der neue Wert
        :raises:
            KeyError: Index not found
        """
        pass
    
    
    def __contains__(self, value: object) -> bool:
        current = self.anfang
        counter = 0
        while current.data is not value:
            current = current.successor
            counter +=1
            if counter is len(self):
                return False
        return True
            
        

    """__iter__ kann zusätzlich implementiert werden, damit z.B. die for-Schleife mit der Liste funktioniert."""
    
    
    def __len__(self) -> int:
        current_node = self.anfang
        counter = 0
        while current_node is not None:
            current_node = current_node.successor
            counter +=1
        return int(counter)
    
    
    
    def insert(self, index: int, value: object) -> None:
        current_node = self.anfang
        # print(index)
        index = index - 1
        counter = 0
        while counter !=index:
            counter +=1
            prev_node = current_node
            current_node = current_node.successor
        to_be_node = Listnode(value, current_node)
        prev_node.successor = to_be_node
        
    def remove(self, index: int) -> None:
        current_node = self.anfang
        # print(index)
        counter = 0
        index = index - 1
        while counter !=index:
            counter +=1
            prev_node = current_node
            current_node = current_node.successor
        prev_node.successor = current_node.successor
        
l = ListIterativ()
l.append(18)
l.append(19)
l.append(20)
l.append(21)
l.append(22)
l.append(23)
l.append(24)
# l[3]=5
# print(l[3])
l.insert(3, 5)
# print(l)
if 23 in l:
    print("yes")
else:
    print("no")