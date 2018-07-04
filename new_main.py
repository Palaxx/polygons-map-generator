import sys
from src.map import Map
from src.map_drawer import MapDrawer
from src.generators.shape_generator import ShapeGenerator
from src.generators.elevation_generator import ElevationGenerator

argv = sys.argv
size = argv[1] if len(argv) > 1 else 100
shape_octaves = argv[2] if len(argv) > 2 else 30
height_octaves = argv[3] if len(argv) > 3 else 5
height_seed = argv[4] if len(argv) > 4 else 0


size = int(size)
shape_octaves = int(shape_octaves)
height_octaves = int(height_octaves)
height_seed = int(height_seed)
map = Map(size, size)

shapeGenerator = ShapeGenerator(16.00, shape_octaves)
elevationGenerator = ElevationGenerator(16.00, height_octaves, height_seed)
map = shapeGenerator.generate(map)
map = elevationGenerator.generate(map)
map.elaborate()
map_drawer = MapDrawer(map, {})
map_drawer.draw_map()


# map.print()