from src.terrain.terrain import Terrain

class BareEarth(Terrain):
    def get_color(self):
        return (136, 136, 136)


    def get_name(self):
        return "bare-earth"