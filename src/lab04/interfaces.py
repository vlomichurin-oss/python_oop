from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass


class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        pass


class Identifiable(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass