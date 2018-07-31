from argparse import ArgumentParser
from src.terrain.factory import TerrainFactory
from src.drawer.map_drawer import MapDrawer
import numpy as np

from src.generators.perlin_noise import Perlin
from src.generators.open_simplex_noise import OpenSimplexNoise
from src.generators.generator_factory import GeneratorFactory

argumentParser = ArgumentParser()
argumentParser.add_argument('--size', type=int)
argumentParser.add_argument('--seed', type=int)
argumentParser.add_argument('--octaves', type=int)
argumentParser.add_argument('--noise', type=str)
argumentParser.add_argument('--tile_size', type=int)

args = argumentParser.parse_args()
size = args.size if args.size else 100
seed = args.seed if args.seed else 256
octaves = args.octaves if args.octaves else 0
noise = args.noise if args.noise else None
tile_size = args.tile_size if args.tile_size else 1
coord_factor = size / 4

elevation_generator = GeneratorFactory.make_generator(noise, octaves, seed)
moisture_generator = GeneratorFactory.make_generator(noise, octaves, seed)


# map =  [[0 for col in range(size)] for row in range(size)]
elevation = np.zeros((size, size), dtype=float)
moisture = np.zeros((size,size),dtype=float)
terrainFactory = TerrainFactory()

for coord, value in np.ndenumerate(elevation):
    x = coord[0]
    y = coord[1]
    elevation[y][x] = elevation_generator.get_noise(x / coord_factor, y / coord_factor)
    moisture[y][x] = moisture_generator.get_noise(x / coord_factor, y / coord_factor)


# trasformamre mappa interi in mappa di terreni
terrains = np.zeros((size,size),dtype=np.object)
for coord, value in np.ndenumerate(elevation):
    x = coord[0]
    y = coord[1]
    terrains[y][x] = terrainFactory.make_terrain(elevation[y][x], moisture[y][x])

map_drawer = MapDrawer(terrains, size)
map_drawer.set_tile_size(tile_size)
map_drawer.draw_map()