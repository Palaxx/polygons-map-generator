from src.terrain.terrain import Terrain

class Shrubland(Terrain):
    def get_color(self):
        return (136, 153, 119)


    def get_name(self):
        return "shrubland"