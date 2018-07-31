from src.terrain.terrain import Terrain

class Grassland(Terrain):
    def get_color(self):
        return (136,170,85)


    def get_name(self):
        return "grassland"