from src.terrain.terrain import Terrain

class Scorched(Terrain):
    def get_color(self):
        return (85, 85, 85)


    def get_name(self):
        return "scorched"