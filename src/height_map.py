from src.map import Map
from noise import snoise2
from PIL import Image, ImageDraw
class HeightMap:

    def __init__(self, map: Map):
        self.width = map.width
        self.height = map.height
        self.height_map = [[0 for col in range(self.width)] for row in range(self.height)]
        self.map = map
        self.point_height = {}

    def generate(self, octaves : int, max_value : int = 255):
        freq = 16.0 * octaves
        for x in range(self.width):
            for y in range(self.height):
                self.height_map[x][y] = int ( snoise2(x / freq, y / freq, octaves) * int(max_value/2) + int(max_value/2))

    def get_point_height(self, x : int, y : int) -> int:
        return self.height_map[x][y]

    def apply_height_map(self):
        for ind, r in enumerate(self.map.regions):
            point = self.map.get_region_point(ind)
            x, y = self.map.get_region_point_coord(point)
            self.point_height[point] = self.get_point_height(x, y)

    def draw_full_image(self, filename:str):
        image = Image.new("L", (self.map.width, self.map.height))
        fileDrawer = ImageDraw.Draw(image)

        for x in range(self.width):
            for y in range(self.height):
                fileDrawer.point((x, y), fill=self.height_map[x][y])

        image.save(filename)
        image.close()

    def draw_simple_image(self, filename:str):
        image = Image.new("L", (self.map.width, self.map.height))
        fileDrawer = ImageDraw.Draw(image)

        for x in range(self.width):
            for y in range(self.height):
                color = int(self.height_map[x][y] / 128)
                color = "#000000" if color == 1 else "#ffffff"
                fileDrawer.point((x, y), fill=color)

        image.save(filename)
        image.close()