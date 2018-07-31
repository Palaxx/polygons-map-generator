from noise.perlin import SimplexNoise
from src.generators.noise_generator import NoiseGenerator

class Perlin(NoiseGenerator):

    def __init__(self, period : int = 256, octaves : int = 0):
        self.simplex_noise = SimplexNoise(period=period)
        self.octaves = octaves

    def get_noise(self, x: int, y: int):
        noise_value = self.__build_noise(x, y) + 1

        return int(noise_value * 100 / 2)

    def __build_noise(self, x:int, y:int):
        noise_value = self.simplex_noise.noise2(x, y)

        for octave in range(self.octaves):
            exp = pow(2, octave)
            noise_value += self.simplex_noise.noise2(x * exp, y * exp / 2) / exp
        return noise_value