from src.terrain.terrain import Terrain

class Snow(Terrain):
    def get_color(self):
        return (221,221,228)


    def get_name(self):
        return "snow"