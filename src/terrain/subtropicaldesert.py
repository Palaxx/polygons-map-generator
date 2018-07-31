from src.terrain.terrain import Terrain

class SubtropicalDesert(Terrain):
    def get_color(self):
        return (210, 185, 139)


    def get_name(self):
        return "desert"