from src.terrain.terrain import Terrain

class Beach(Terrain):
    def get_color(self):
        return 	(244, 164, 96)


    def get_name(self):
        return "sand"