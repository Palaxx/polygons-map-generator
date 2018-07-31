
from abc import ABC, abstractmethod


class Terrain(ABC):

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


