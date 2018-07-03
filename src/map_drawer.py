from src.map import Map
from src.height_map import HeightMap
from PIL import ImageDraw, Image

class MapDrawer:

    def __init__(self, map : Map, colors: dict):
        self.map = map
        self.colors = colors

    def draw_map(self):
        for key, matrix in self.map.matrix.items():
            self.__draw_matrix(key, matrix)


    def __draw_matrix(self, key: str, matrix):
        type = 'RGB' if key == 'map' else 'L'
        image = Image.new(type, (self.map.width, self.map.height))
        drawer = ImageDraw.Draw(image)
        for y in range(self.map.height):
            for x in range(self.map.width):
                value = matrix[y][x]
                drawer.point((y,x), self.__get_color(key, value))

        image.save("outputs/"+key+".png")


    def __get_color(self, type:str , value: int):
        map = {
            'shape' : self.__get_shape_color,
            'elevation' : self.__get_elevation_color,
            'map' : self.__get_result_color
        }
        if type in map:
            return map[type](value)
        else:
            return self.__get_result_color(value)

    def __get_shape_color(self, value: int):
        if value > 0:
            return 255
        return 0

    def __get_elevation_color(self, value: int):
        return value

    def __get_result_color(self, value: int):
        try:
            value = int(value / 25)
        except Exception:
            value = 0

        colors = [
            (70, 130, 180),
            (240, 230, 140),
            (255,215,0),
            (144, 238, 144),

            (152, 251, 152),
            (50, 205, 50),
            (34, 139, 34),
            (128, 128, 0),

            (139, 69, 19),
            (105, 105, 105),
            (220, 220, 220),
            (255, 255, 255)
        ]
        if value >= len(colors):
            value = len(colors) - 1

        return colors[value]
