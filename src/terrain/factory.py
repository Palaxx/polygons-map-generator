from src.terrain.water import Water
from src.terrain.grassland import Grassland
from src.terrain.beach import Beach
from src.terrain.temperate_rain_forest import TemperateRainForest
from src.terrain.subtropicaldesert import SubtropicalDesert
from src.terrain.temperate_decidious_forest import TemperateDecidiousForest
from src.terrain.snow import Snow
from src.terrain.scorched_earth import Scorched
from src.terrain.bare_earth import BareEarth
from src.terrain.tundra import Tundra
from src.terrain.taiga import Taiga
from src.terrain.shrubland import Shrubland
from src.terrain.temperate_desert import TemperateDesert
from src.terrain.tropical_seasonal_forest import TropicalSeasonalForest
from src.terrain.tropical_rain_forest import TropicalRainForest


class TerrainFactory:
    def make_terrain_from_elevation(self, elevation: int):
        if elevation < 10:
            return Water()
        elif elevation < 20:
            return Beach()
        elif elevation < 30:
            return Grassland()
        elif elevation < 50:
            return TemperateRainForest()
        elif elevation < 70:
            return TemperateDecidiousForest()
        elif elevation < 90:
            return SubtropicalDesert()
        else:
            return Snow()

    def make_terrain(self, elevation: int, moisture: int):
        if elevation < 10:
            return Water()
        if elevation < 12:
            return Beach()

        if elevation > 80:
            if moisture < 10:
                return Scorched()
            if moisture < 20:
                return BareEarth()
            if moisture < 50:
                return Tundra()
            return Snow()

        if elevation > 60:
            if moisture < 33:
                return TemperateDesert()
            if moisture < 66:
                return Shrubland()
            return Taiga()

        if elevation > 30:
            if moisture < 16:
                return TemperateDesert()
            if moisture < 50:
                return Grassland()
            if moisture < 83:
                return TemperateDecidiousForest()
            return TemperateRainForest()

        if moisture < 16:
            return SubtropicalDesert()
        if moisture < 33:
            return Grassland()
        if moisture < 66:
            return TropicalSeasonalForest()
        return TropicalRainForest()
