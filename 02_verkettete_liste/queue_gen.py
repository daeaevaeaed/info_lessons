"""Implementierung einer Verketteten Liste

Für Python umgesetzt nach einer Java Version von Rainer Helfrich Oktober 2020.
"""
__version__ = "1.0" # 2022.03
__author__ = "S. Gebert"
__all__ = ['List','ListIterativ']

from typing import Optional, TypeVar, Generic
from collections.abc import Collection, Iterator
from abc import ABC, abstractmethod
# from typing_extensions import Self

T = TypeVar("T")

class Queuenode(Generic[T]):
    """Ein Listen.
    
    Attributes:
        data: Der Datenwert des Listenknotens.
        next_node: Der Nachfolger des Listenknotens.
    """
    data: T
    next_node: Optional['Queuenode[T]']
    
    def __init__(self, data: T, next_node: Optional['Queuenode[T]'] = None):
        self.data = data
        self.next_node = next_node
        
    def __str__(self) -> str:
        return str(self.data)
        
class Queue(Collection[T]):
    """Abstrakte Liste

    Attributes:
        first_node: Der erste Knoten der Liste
    """
    first_node: Optional[Queuenode]
    
    def __bool__(self) -> bool:
        """Gibt zurück, ob die Liste leer ist.

        Returns:
            True, falls die Liste leer ist; False sonst
        """
        return self.first_node == None
    
    # @abstractmethod         
    # def __getitem__(self, index: int) -> T:
    #     """Gibt den n-ten Wert (0-basierte Zählweise) der Liste zurück.
        
    #     Attr:
    #         index: Der Index des gewünschten Elements
    #     Returns:
    #         Den n-ten Wert
    #     Raises:
    #         KeyError: Index not found
    #     """
    #     pass
    
    # @abstractmethod
    # def __setitem__(self, index: int, value: T) -> None:
    #     """Ändert den Wert an der gegebenen Stelle (0-basierte Zählweise) der Liste.

    #     Attr:
    #         index: Der Index des zu ändernden Elements
    #         value: Der neue Wert
    #     Raises:
    #         KeyError: Index not found
    #     """
    #     pass
    
    # @abstractmethod
    # def __delitem__(self, index: int) -> None:
    #     """ Entfernt das Element, das an der angegeben Stelle steht, aus der Liste.
        
    #     Attr:
    #         index: Die Stelle, von der der Wert entfernt werden soll
    #     Raises:
    #         KeyError: Index not found
    #     """
    #     pass
    
    # @abstractmethod
    # def __contains__(self, value: object) -> bool:
    #     """Gibt zurück, ob ein Wert sich in der Liste befindet

    #     Atrr:
    #         value: Der zu suchende Wert
    #     Returns:
    #         True, falls der Wert enthalten ist; False sonst
    #     """
    #     pass

    def __iter__(self) -> Iterator[T]:
        """Iterator über die Daten"""
        node = self.first_node
        while node is not None:
            yield node.data
            node = node.next_node
 
    # @abstractmethod
    # def __len__(self) -> int:
    #     """Gibt die Anzahl der Elemente der Liste zurück."""
    #     pass
    
    # @abstractmethod
    # def append(self, value: T) -> None:
    #     """Hängt einen neuen Wert hinten an die Liste an.

    #     Attr:
    #         value: Der anzuhängende Wert
    #     """
    #     pass 
    
    # @abstractmethod
    # def insert(self, index: int, value: T) -> None:
    #     """Fügt einen neuen Wert an einer gewünschten Stelle in die Liste ein.
        
    #     Attr:
    #         index: Die Stelle, an der der neue Wert stehen soll (0 <= index <= len)
    #         value: Der einzufügende Wert
    #     """
    #     pass
        
    # @abstractmethod
    # def remove(self, value: T) -> None:
    #     """ Entfernt den ersten gefundenen Wert aus der Liste.
        
    #     Attr:
    #         value: Wert der entfernt werden soll.
    #     Raises:
    #         ValueError: List.remove(value): value not in list
    #     """
    #     pass
    
    def __str__(self) -> str:
        """Gibt die Listenelemente hintereinander aus."""
        return " ".join([str(e) for e in self])
        
class Queueiterative(Queue[T]):
    """Iterative Implementierung einer Verketteten Liste"""
    def __init__(self):
        self.first_node = None
    
        
    def __getitem__(self, index: int) -> T:
        if index < 0:
            raise IndexError("Index not found")
        node = self.first_node
        while node is not None:
            if index==0:
                return node.data
            node = node.next_node
            index -= 1
        raise IndexError("Index not found")

    def __setitem__(self, index: int, value: T) -> None:
        if index < 0:
            raise IndexError("Index not found")
        node = self.first_node
        while index > 0:
            if node is None:
                raise IndexError("Index not found")
            node = node.next_node
            index -= 1
        if node is None:
            raise IndexError("Index not found")
        node.data = value
    
    def __delitem__(self, index: int) -> None:
        if index < 0 or self.first_node is None:
            raise KeyError("Index not found")
        if index == 0:
            tmp = self.first_node
            self.first_node = self.first_node.next_node
            del tmp
            return
        node = self.first_node
        while index > 1 and node.next_node is not None:
            node = node.next_node
            index -= 1
        if node is None or node.next_node is None:
            raise IndexError("Index not found")
        tmp = node.next_node
        node.next_node = tmp.next_node
        del tmp
          
    def __contains__(self, value: object) -> bool:
        node = self.first_node
        while node is not None:
            if node.data == value:
                return True
            node = node.next_node
        return False
    
    def __len__(self) -> int:
        pass
        
    def remove(self, value: T) -> None:
        pass

    def pop(self):
        pass
    
    def isEmpty(self):
        pass
    
    def __len__(self):
        pass
    
    def clear(self):
        pass
                
    def remove(self):
        pass
            
    def __str__(self) -> str:
        pass
        
    def enqueue(self, value: object) -> None:
        if not self.first_node:
            self.first_node = Queuenode(value, None)
            return
        prev_node = None
        next_node = self.first_node
        while next_node is not None:
            prev_node = next_node
            next_node = next_node.next_node
        prev_node.next_node = Queuenode(value, None)
    
    def front(self):
        return self.first_node.data
        
q = Queueiterative()
q.enqueue(19)
q.enqueue(20)
print(q.front())
