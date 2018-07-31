from src.terrain.terrain import Terrain

class TropicalRainForest(Terrain):
    def get_color(self):
        return (51,119,85)


    def get_name(self):
        return "tropical-rain-forest"