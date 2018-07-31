
from abc import ABC, abstractmethod

class NoiseGenerator(ABC):

    @abstractmethod
    def get_noise(self, x : float, y : float) -> int:
        pass