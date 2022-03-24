"""Implementierung einer Verketteten Liste

Für Python umgesetzt nach einer Java Version von Rainer Helfrich Oktober 2020.
"""
__version__ = "1.0" # 2022.03
__author__ = "S. Gebert"
__all__ = ['List','ListIterativ']

from typing import Optional
from abc import ABC, abstractmethod
from xml.dom import NOT_FOUND_ERR

class Stacknode():
    """Ein Listen.
    
    Attributes:
        data: Der Datenwert des Listenknotens.
        next_node: Der Nachfolger des Listenknotens.
    """
    data: object
    next_node: Optional['Stacknode']
    
    def __init__(self, data: object, next_node: Optional['Stacknode'] = None):
        self.data = data
        self.next_node = next_node
        
    def __str__(self) -> str:
        return str(self.data)
        
class Stack(ABC):
    """Abstrakte Liste

    Attributes:
        first_node: Der erste Knoten der Liste
    """
    first_node: Optional[Stacknode]
    
    def __bool__(self) -> bool:
        """Gibt zurück, ob die Liste leer ist.

        Returns:
            True, falls die Liste leer ist; False sonst
        """
        return self.first_node == None
    
    @abstractmethod         
    def __getitem__(self, index: int) -> object:
        """Gibt den n-ten Wert (0-basierte Zählweise) der Liste zurück.
        
        Attr:
            index: Der Index des gewünschten Elements
        Returns:
            Den n-ten Wert
        Raises:
            KeyError: Index not found
        """
        pass
    
    @abstractmethod
    def __setitem__(self, index: int, value: object) -> None:
        """Ändert den Wert an der gegebenen Stelle (0-basierte Zählweise) der Liste.

        Attr:
            index: Der Index des zu ändernden Elements
            value: Der neue Wert
        Raises:
            KeyError: Index not found
        """
        pass
    
    @abstractmethod
    def __delitem__(self, index: int) -> None:
        """ Entfernt das Element, das an der angegeben Stelle steht, aus der Liste.
        
        Attr:
            index: Die Stelle, von der der Wert entfernt werden soll
        Raises:
            KeyError: Index not found
        """
        pass
    
    @abstractmethod
    def __contains__(self, value: object) -> bool:
        """Gibt zurück, ob ein Wert sich in der Liste befindet

        Atrr:
            value: Der zu suchende Wert
        Returns:
            True, falls der Wert enthalten ist; False sonst
        """
        pass

    def __iter__(self) -> object:
        """Iterator über die Daten"""
        node = self.first_node
        while node is not None:
            yield node.data
            node = node.next_node
 
    @abstractmethod
    def __len__(self) -> int:
        """Gibt die Anzahl der Elemente der Liste zurück."""
        pass
    
    @abstractmethod
    def append(self, value: object) -> None:
        """Hängt einen neuen Wert hinten an die Liste an.

        Attr:
            value: Der anzuhängende Wert
        """
        pass 
    
    @abstractmethod
    def insert(self, index: int, value: object) -> None:
        """Fügt einen neuen Wert an einer gewünschten Stelle in die Liste ein.
        
        Attr:
            index: Die Stelle, an der der neue Wert stehen soll (0 <= index <= len)
            value: Der einzufügende Wert
        """
        pass
        
    @abstractmethod
    def remove(self, value: object) -> None:
        """ Entfernt den ersten gefundenen Wert aus der Liste.
        
        Attr:
            value: Wert der entfernt werden soll.
        Raises:
            ValueError: List.remove(value): value not in list
        """
        pass
    
    def __str__(self) -> str:
        """Gibt die Listenelemente hintereinander aus."""
        return " ".join([str(e) for e in self]) # type: ignore
        
class Stackiterativ(Stack):
    """Iterative Implementierung einer Verketteten Liste"""
    
    def __init__(self):
        self.first_node = None
        
    def top(self, index: int) -> object:
        node = self.first_node
        while node.next_node is not None:
            node_counter += 1
        counter = 0
        while counter < node_counter:
            node = node.next_node
        return node.data

    def __setitem__(self, index: int, value: object) -> None:
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
        len = 0
        node = self.first_node
        while node is not None:
            node = node.next_node
            len += 1
        return len
    
    def append(self, value: object) -> None:
        neu = Listnode(value, None)
        if self.first_node is None:
            self.first_node = neu
        else:
            node = self.first_node
            while node.next_node is not None:
                node = node.next_node
            node.next_node = neu
    
    def insert(self, index: int, value: object) -> None:
        if index < 0:
            raise IndexError("Index not found")
        if index == 0:
            self.first_node = Listnode(value, self.first_node)
            return
        node = self.first_node
        while index > 1:
            if node is None:
                raise IndexError("Index not found")
            node = node.next_node
            index -= 1
        if node is None:
            raise IndexError("Index not found")
        node.next_node = Listnode(value, node.next_node)
        
    def remove(self, value: object) -> None:
        node = self.first_node
        if node is not None and node.data == value:
            self.first_node = node.next_node      
        previous_node = node
        while node is not None:
            if node.data == value and previous_node is not None:
                previous_node.next_node = node.next_node
#                del node
                return
            previous_node = node
            node = node.next_node
        raise ValueError("List.remove(value): value not in list")
    
        """
        Stack() generates new stack
        push(T, x) adds x on top
        top() queer of latest value
        pop() queer and deletion of lates value
        isEmpty() checks if content; boolean
        """