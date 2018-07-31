from opensimplex import OpenSimplex
from src.generators.noise_generator import NoiseGenerator
from math import sqrt
class OpenSimplexNoise(NoiseGenerator):

    def __init__(self, seed : int = 256, octaves : int = 0):
        self.simplex_noise = OpenSimplex(seed=seed)
        self.octaves = octaves

    def get_noise(self, x: int, y: int):
        noise_value = self.__build_noise(x, y)
        noise_value = noise_value / 2 + 0.5
        if noise_value < 0:
            noise_value = 0
        elevation =noise_value
        elevation = self.__redistribute(noise_value)
        elevation = self.__shape(elevation, x, y)
        elevation = self.__terrace(elevation)
        return int( elevation * 100)

    def __terrace(self, elevation):
        return round(elevation * 40) / 40

    def __redistribute(self, elevation: float)->float:
        return pow(elevation, 0.7)

    def __shape(self, elevation: float, x : float, y: float):
        # distance = 2*sqrt(x*x + y*y)
        max_distance = sqrt(pow(1.98, 2) + pow(1.98, 2))
        distance = sqrt(pow(x-1.98,2) + pow(y-1.98, 2)) / max_distance
        a = 0.05
        b = 1
        c = 1.50
        return elevation + a - b * pow(distance,c)
        # return (elevation + a) * (1.0 - b*pow(distance, c))

    def __build_noise(self, x:int, y:int):
        # noise_value = self.simplex_noise.noise2d(x, y)
        noise_value = 0
        amplitude = 0
        for octave in range(self.octaves):
            exp = pow(2, octave)
            # multiplier = 1 if noise_value == 0 else noise_value
            # amplitude += 1 / exp
            noise_value += self.simplex_noise.noise2d(x * exp, y * exp / 2) / exp


        return noise_value