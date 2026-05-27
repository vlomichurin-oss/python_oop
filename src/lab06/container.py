from typing import TypeVar, Generic, Callable, Optional, List, Protocol
from abc import ABC, abstractmethod


class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


# ===== TypeVar с ограничениями для generics =====

D = TypeVar('D', bound=Displayable)  # Тип, поддерживающий Displayable
S = TypeVar('S', bound=Scorable)     # Тип, поддерживающий Scorable
T = TypeVar('T')                      # Свободный тип для общих коллекций
R = TypeVar('R')                      # Тип результата для map


# ===== Generic-коллекция =====

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    # ===== Базовые методы =====
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError("неверный индекс")
    
    def get_all(self) -> List[T]:
        return list(self._items)
    
    def clear(self) -> None:

        self._items.clear()
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def __str__(self) -> str:
        return "\n".join(str(item) for item in self._items)
    
    # ===== Новые методы =====
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]
    
    
    def any(self, predicate: Callable[[T], bool]) -> bool:
        return any(predicate(item) for item in self._items)
    
    def all(self, predicate: Callable[[T], bool]) -> bool:
        return all(predicate(item) for item in self._items)



def make_displayable(obj: D) -> D:
    return obj


def make_scorable(obj: S) -> S:
    return obj