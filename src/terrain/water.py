from src.terrain.terrain import Terrain

class Water(Terrain):
    def get_color(self):
        return (0,0,128)


    def get_name(self):
        return "water"