from noise import snoise2, snoise3
from noise.perlin import SimplexNoise

from src.map import Map
from src.generators.abstract_generator import AbstractGenerator

class ElevationGenerator(AbstractGenerator):

    def __init__(self, freq: float, octaves: int, seed: int = 0):
        self.frequency = freq * octaves
        self.octaves = octaves
        self.seed = seed
        self.noise = SimplexNoise()
        self.noise.randomize(self.seed)

    def generate(self, map: Map) -> Map:
        elevation_map = [[0 for i in range(map.height)] for j in range(map.width)]

        for y in range(map.height):
            for x in range(map.width):
                ny = (x/map.height -0.5)
                nx = (y/map.width -0.5)
                elevation_map[y][x] = self.__get_elevation(ny, nx)

        map.set_elevation_matrix(elevation_map)

        return map

    def __get_elevation(self, x : int, y : int):
        # noise = self.__get_noise(x, y)* 127 + 128
        noise = self.__get_noise(x, y)

        return int(noise)

    def __get_noise(self, x: int, y: int):
        value = self.noise.noise2(x, y)
        for i in range(self.octaves):
            multiplier = pow(2, self.octaves)
            value += 1 / multiplier * self.noise.noise2(x * multiplier, y * multiplier)
        return int(value / 2 * 127 + 128)

