from PIL import ImageDraw, Image
import numpy as np

class MapDrawer:

    def __init__(self, map, size: int):
        self.map = map
        self.size = size
        self.tile_size = 1

    def set_tile_size(self, size: int):
        self.tile_size = size

    def draw_map(self):
        map_size = self.size * self.tile_size
        image = Image.new('RGB', (map_size,map_size))
        drawer = ImageDraw.Draw(image)
        terrains, colors = self.__group_by_terrain()

        for terrain_name, coords in terrains.items():
            drawer.point(coords, colors[terrain_name])
        image.save("outputs/map.png")

    def __group_by_terrain(self):
        terrains = dict()
        colors = dict()
        for coord, terrain in np.ndenumerate(self.map):
            if not terrain.get_name() in terrains:
                terrains[terrain.get_name()] = []
            if not terrain.get_name() in colors:
                colors[terrain.get_name()] = terrain.get_color()

            self.append_coords(terrains[terrain.get_name()], coord)
        return terrains, colors

    def append_coords(self, terrain_list: list, coord : tuple):
        for y in range(self.tile_size):
            for x in range(self.tile_size):
                terrain_list.append((coord[0]*self.tile_size+y, coord[1]*self.tile_size+x))




