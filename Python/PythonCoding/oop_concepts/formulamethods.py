from abc import ABC, abstractmethod

class FM(ABC):
    @abstractmethod #decorator
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass