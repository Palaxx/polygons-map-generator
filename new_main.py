import sys
from src.map import Map
from src.map_drawer import MapDrawer
from src.generators.shape_generator import ShapeGenerator
from src.generators.elevation_generator import ElevationGenerator

argv = sys.argv
size = argv[1] if len(argv) > 1 else 100
size = int(size)
map = Map(size, size)

shapeGenerator = ShapeGenerator(16.00, 30)
elevationGenerator = ElevationGenerator(16.00, 5)
map = shapeGenerator.generate(map)
map = elevationGenerator.generate(map)
map.elaborate()
map_drawer = MapDrawer(map, {})
map_drawer.draw_map()


# map.print()