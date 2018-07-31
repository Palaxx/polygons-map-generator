from src.terrain.terrain import Terrain

class TemperateDesert(Terrain):
    def get_color(self):
        return (201, 210, 155)


    def get_name(self):
        return "temperate-desert"