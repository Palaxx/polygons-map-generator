import abc
from src.map import Map
class AbstractGenerator(abc.ABC):

    @abc.abstractmethod
    def generate(self, map: Map) -> Map:
        pass