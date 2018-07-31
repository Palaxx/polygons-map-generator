from src.terrain.terrain import Terrain

class Taiga(Terrain):
    def get_color(self):
        return (153, 170, 119)


    def get_name(self):
        return "taiga"