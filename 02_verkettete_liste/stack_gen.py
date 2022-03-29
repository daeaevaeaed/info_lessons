"""Implementierung einer Verketteten Liste

Für Python umgesetzt nach einer Java Version von Rainer Helfrich Oktober 2020.
"""
__version__ = "1.0" # 2022.03
__author__ = "S. Gebert"
__all__ = ['List','ListIterativ']

from ast import IsNot
from typing import Optional, TypeVar, Generic
from collections.abc import Collection, Iterator
from abc import ABC, abstractmethod

# from typing_extensions import Self

T = TypeVar("T")

class Stacknode(Generic[T]):
    """Ein Listen.
    
    Attributes:
        data: Der Datenwert des Listenknotens.
        next_node: Der Nachfolger des Listenknotens.
    """
    data: T
    next_node: Optional['Stacknode[T]']
    
    def __init__(self, data: T, next_node: Optional['Stacknode[T]'] = None):
        self.data = data
        self.next_node = next_node
        
    def __str__(self) -> str:
        return str(self.data)
        
class Stack(Collection[T]):
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

    def __iter__(self) -> Iterator[T]:
        """Iterator über die Daten"""
        node = self.first_node
        while node is not None:
            yield node.data
            node = node.next_node
 
    def __str__(self) -> str:
        """Gibt die Listenelemente hintereinander aus."""
        return " ".join([str(e) for e in self])
        
        
class Stackiterative(Stack[T]):
    """Iterative Implementierung einer Verketteten Liste"""
    def __init__(self):
        self.first_node = None
    
    def top(self) -> object:
        if not self.isEmpty():
            node = self.first_node
            while node.next_node is not None:
                node = node.next_node
            return node.data
    
    def push(self, value: object) -> None:
        if not self.first_node:
            self.first_node = Stacknode(value, None)
            return
        prev_node = None
        next_node = self.first_node
        while next_node is not None:
            prev_node = next_node
            next_node = next_node.next_node
        prev_node.next_node = Stacknode(value, None)
        
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
        length = 0
        node = self.first_node
        while node is not None:
            node = node.next_node
            length += 1
        return length
        
    def remove(self, value: T) -> None:
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

    def pop(self):
        print(self.isEmpty())
        if self.isEmpty():
            return
            print("error")
        data = self.top()
        self.remove()
        return data
    
    def isEmpty(self):
        node = self.first_node
        for i in self:
            if node.data == None or node == None or node.next_node == None:
                # print("empty")
                return True
            else:
                # print("full")
                return False
    
    def __len__(self):
        node = self.first_node
        length = 1
        # print("Länge")
        while node is not None:
            length += 1
            node = node.next_node
        return length + 2
    
    def clear(self):
        while(not self.isEmpty()):
            self.remove()
        self.first_node.data = None
        # self.first_node = None
                
    def remove(self):
        if not self.isEmpty:
            node = self.first_node
            prev_node = None
            if self.first_node.next_node is not None:
                while node.next_node is not None:
                    prev_node = node
                    node = node.next_node
                prev_node.next_node = None
            
    def __str__(self) -> str:
        if not self.isEmpty():
            data = ""
            node = self.first_node
            for i in self:
                data  += str(node.data) + " "
                node = node.next_node
            return data
class ArrayStack(Stack[T]):
    data: list[Optional[T]]
    def __init__(self):
        self.data = [None]*10
        self.max_stack_length = 0
        self.top_index = 0
    
    
    
    def push(self, value: object) -> None:
        self.data[self.top_index] = value
        self.top_index += 1
        
    
    def top(self):
        return self.data[self.top_index]
        
    def __len__(self):
        return self.current_length
    
    def __contains__(self, __x: object) -> bool:
        return None
        
                
                
    
s = ArrayStack()
s.push(10)
s.push(11)
s.push(12)
s.push(26)
print(s.top())
print("ende")