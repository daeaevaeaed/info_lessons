"""Stack"""
__version__ = "1.0" # 2022.03
__author__ = "S. Gebert"
__all__ = ['Stack','ListStack']

from typing import Optional, TypeVar, Generic
from collections.abc import Collection, Iterator
from abc import ABC, abstractmethod

T = TypeVar("T")

class Listnode(Generic[T]):
    """Ein Listen.
    
    Attributes:
        data: Der Datenwert des Listenknotens.
        next_node: Der Nachfolger des Listenknotens.
    """
    data: T
    next_node: Optional['Listnode[T]']
    
    def __init__(self, data: T, next_node: Optional['Listnode[T]'] = None):
        self.data = data
        self.next_node = next_node
        
    def __str__(self) -> str:
        return str(self.data)
        
class Stack(Generic[T]):
    """Abstrakte Liste"""

    @abstractmethod
    def __bool__(self) -> bool:
        """Gibt zurück, ob die Liste leer ist.

        Returns:
            True, falls die Liste nicht leer ist; False sonst
        """
        pass
 
    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """Iterator über die Daten"""
        pass
    
    def empty(self) -> bool:
        return not bool(self)
 
    @abstractmethod
    def __len__(self) -> int:
        """Gibt die Anzahl der Elemente im Stack zurück."""
        pass
    
    @abstractmethod
    def push(self, value: T) -> None:
        """Legt einen neuen Wert auf den Stapel.

        Attr:
            value: Der Wert der gepusht werden soll.
        """
        pass 
    
         
    @abstractmethod
    def pop(self) -> T:
        """ Nimmt den obersten Wert vom Stapel
        
        Returns: Der oberste Wert.
        Raises:
            IndexError: Stack.pop() from empty stack 
        """
        pass
    
    @abstractmethod
    def top(self) -> T:
        """Gib den obersten Wert vom Stapel zurück

        Returns: Der oberste Wert.
        Raises:
            IndexError: Stack.top() on empty stack
        """
    
    
    def __str__(self) -> str:
        """Gibt die Listenelemente hintereinander aus."""
        return " ".join([str(e) for e in self])
        
class ListStack(Stack[T]):
    """Implementierung eines verketteten Stacks

    Attributes:
        top_node: Der oberste Knoten des Stacks
    """
    
    top_node: Optional[Listnode]
    
    def __bool__(self) -> bool:
        """Gibt zurück, ob die Liste leer ist.

        Returns:
            True, falls die Liste nicht leer ist; False sonst
        """
        return self.top_node is not None
    
    def __init__(self):
        self.top_node = None
      
    def __iter__(self) -> Iterator[T]:
        """Iterator über die Daten"""
        node = self.top_node
        while node is not None:
            yield node.data
            node = node.next_node
    
    def __len__(self) -> int:
        len = 0
        node = self.top_node
        while node is not None:
            node = node.next_node
            len += 1
        return len
    
    def push(self, value: T) -> None:
        """Hängt einen neuen Wert hinten an die Liste an.

        Attr:
            value: Der anzuhängende Wert
        """
        self.top_node = Listnode(value, self.top_node)
       
    def pop(self) -> T:
        """ Nimmt den obersten Wert vom Stapel
        
        Returns: Der oberste Wert.
        Raises:
            IndexError: Stack.pop() from empty stack
        """
        if self.top_node is None:
            raise IndexError("Stack.pop() from empty stack")
        node = self.top_node
        self.top_node = self.top_node.next_node
        return node.data
    
    def top(self) -> T:
        if self.top_node is None:
            raise IndexError("Stack.top() on empty stack")
        return self.top_node.data

