from src.generators.noise_generator import NoiseGenerator
from src.generators.perlin_noise import Perlin
from src.generators.open_simplex_noise import OpenSimplexNoise
class GeneratorFactory:

    @staticmethod
    def make_generator(type:str, octaves: int, seed : int) -> NoiseGenerator:
        map = {
            'perlin' : Perlin,
            'simplex' : OpenSimplexNoise
        }

        if type in map:
            return map[type](seed, octaves)

        return OpenSimplexNoise(seed, octaves)