from noise import snoise2, snoise3
from noise.perlin import SimplexNoise

from src.map import Map
from src.generators.abstract_generator import AbstractGenerator

class ElevationGenerator(AbstractGenerator):

    def __init__(self, freq: float, octaves: int):
        self.frequency = freq * octaves
        self.octaves = octaves
        self.simplex_noise = SimplexNoise()
        self.simplex_noise.randomize(10)

    def generate(self, map: Map) -> Map:
        elevation_map = [[0 for i in range(map.height)] for j in range(map.width)]

        for y in range(map.height):
            for x in range(map.width):
                elevation_map[y][x] = self.__get_elevation(y, x)

        map.set_elevation_matrix(elevation_map)

        return map

    def __get_elevation(self, x : int, y : int):
        noise = self.__get_noise(x, y)* 127 + 128
        return int(noise)

    def __get_noise(self, x: int, y: int):
        noise = 0
        # for octaves in range(self.octaves):
        #     current = pow(2, octaves)
        #     noise += self.simplex_noise.noise2(x *  current, y * current) / current
        #
        # return noise / self.octaves
        return snoise2(x / self.frequency, y / self.frequency, self.octaves)