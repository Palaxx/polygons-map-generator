from src.terrain.terrain import Terrain

class Tundra(Terrain):
    def get_color(self):
        return (187, 187, 170)


    def get_name(self):
        return "tundra"