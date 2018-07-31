from src.terrain.terrain import Terrain

class TropicalSeasonalForest(Terrain):
    def get_color(self):
        return (85,153,68)


    def get_name(self):
        return "tropical-seasonal-forest"