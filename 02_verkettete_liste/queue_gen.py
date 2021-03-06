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
        node = self.first_node
        counter = 0
        while node is not None:
            node = node.next_node
            counter += 1
        return counter
    
    def isEmpty(self):
        if self.first_node is not None:
            return False
        else: return True
    
    def clear(self):
        for i in self:
            self.remove()
                
    def remove(self):
        if self.isEmpty():
            pass
        else:
            self.first_node = self.first_node.next_node

    def dequeue(self) -> str:
        data = self.front()
        self.remove()
        return data

            
    def __str__(self) -> str:
        if not self.isEmpty():
            data = "["
            node = self.first_node
            for i in self:
                if data != "[":
                    data += " "
                data  += str(node.data)
                if node.next_node:
                    data += ","
                node = node.next_node
            return data + "]"
        else:
            return "Is Empty"
        
    def enqueue(self, value: object) -> None:
        if self.isEmpty():
            self.first_node = Queuenode(value, None)
        else: 
            prev_node = None
            next_node = self.first_node
            while next_node is not None:
                prev_node = next_node
                next_node = next_node.next_node
            prev_node.next_node = Queuenode(value, None)
    
    def front(self) -> str:
        if not self.isEmpty():
            return self.first_node.data
        else:
            return

class ArrayStack(Queue[T]):
    data: list[Optional[T]]
    def __init__(self):
        self.max_stack_length = 10
        self.data = [None]*self.max_stack_length
        self.top_index = 0
        self.current = 0

    def enqueue(self, value: object) -> None:
        if self.top_index < self.max_stack_length:
            self.data[self.top_index] = value
            self.top_index += 1
        else:
            print("muss größer sein")
            temp_array = self.data
            self.max_stack_length *= 2
            self.data = self.data*2
            self.data[self.top_index] = value
            self.top_index += 1
    
    def dequeue(self):
        if 0 < self.top_index:
            data = self.data[self.top_index]
            self.top_index -=1

            return data

    def isEmpty(self):
        if self.top_index > 0:
            # print("IsEmpty")
            return False
        else:
            # print("isFilled")
            return True

    def __str__(self) -> str:
        data = ""
        counter = 0
        while counter is not len(self):
            counter += 1
            data += str(self.data[counter]) + " "
        return data

    def __iter__(self) -> Iterator[T]:
        counter = 0
        while counter is not (len(self)-1):
            counter += 1
            yield self.data[counter]


    def __len__(self) -> int:
        return self.top_index

    def __contains__(self) -> str:
        return

        
q = ArrayStack()
q.enqueue(19)
q.enqueue(20)
q.enqueue(21)
# q.enqueue(22)
# q.enqueue(23)
# q.enqueue(24)
# q.enqueue(25)
# q.enqueue(26)
# q.enqueue(27)
# q.enqueue(28)
# q.enqueue(29)
# q.enqueue(30)
# q.enqueue(31)
# q.enqueue(32)
# print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(999)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# print(len(q))
