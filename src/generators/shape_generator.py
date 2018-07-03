from src.map import Map
from noise import snoise2
import math
from src.generators.abstract_generator import AbstractGenerator

class ShapeGenerator(AbstractGenerator):
    a = 0.25
    b = 1.0
    c = 2.0
    max_distance_to_center = 0
    seed = 1001

    def __init__(self, freq: float, octaves: int):
        self.frequency = freq * octaves
        self.octaves = octaves


    def generate(self, map: Map) -> Map:
        self.map = map
        self.max_distance_to_center = self.__get_euclidean_distance(0,0)

        elevation_map = [[0 for i in range(map.height)] for j in range(map.width)]

        for y in range(map.height):
            for x in range(map.width):
                elevation_map[y][x] = self.__get_elevation(y, x)

        map.set_shape_matrix(elevation_map)

        return map

    def __build_elevation_map(self):
        pass

    def __get_elevation(self, x : int, y : int):
        noise = self.__get_noise_value(x, y)
        distance = self.__get_euclidean_distance(x, y) / self.max_distance_to_center
        elevation =  int((noise + self.a - self.b * pow(distance,self.c)) * 127 + 128)
        return 1 if elevation <= 127 else 0


    def __get_noise_value(self, x: int, y: int):
        return snoise2(x / self.frequency, y / self.frequency, self.octaves)

    def __get_euclidean_distance(self, x : int, y:int):
        centerX = int(self.map.width / 2)
        centerY = int(self.map.height / 2)

        return math.sqrt(pow(x - centerX, 2) + pow(y - centerY, 2))