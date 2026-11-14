import resources
from map import STARTINGMAP

tiles = {
    "Farm": [],
    "SolarPanel": [],
    "Habitat": [],
    "MartianSurface": []
}

class Map:
    def __init__(self):
        self.grid = STARTINGMAP
        for i, row in enumerate(STARTINGMAP):
            for j, tile in enumerate(row):
                self.grid[i][j] = tyleskey[tile]()
    
    def build(self, x, y, buildType):
        self.grid[y][x] = tyleskey[buildType]()

    def __str__(self):
        return "\n".join(", ".join(str(item) for item in row) for row in self.grid)


class Tile:
    def __init__(self, name):
        self.name = name
        # !  Click and sprite logic here 
    def __str__(self):
        return self.name
 
class ResourceTile(Tile):
    def __init__(self, name, resource, resourceScale):
            self.resource = resource
            self.workerNum = 0
            self.active = True
            self.resourceModifier = 1
            self.resourceScale = resourceScale
            super().__init__(name)
    
    def generateResource(self):
        if not self.active:
            return 0
    
    def addWorker(self, numWorkers):
        self.workerNum += numWorkers
        self.resource.addResource(self.workerNum * self.resourceModifier * self.resourceScale)

    def removeWorker(self, numWorkers):
        self.workerNum -= numWorkers

    def upgrade(self):
        self.resourceModifier += 1

class Farm(ResourceTile):
    def __init__(self):
        super().__init__("Farm", resources.Generator("Food"), 1)

class SolarPanel(ResourceTile):
    def __init__(self):
        super().__init__("SolarPanel", resources.Generator("Power"), 1)

class NuclearReactor(ResourceTile):
    def __init__(self):
        super().__init__("NuclearReactor", resources.Generator("Power"), 2)

class Habitat(Tile):
    def __init__(self):
        super().__init__("Habitat")

class LaunchSite(Tile):
    def __init__(self):
        super().__init__("LaunchSite")
        
class MartianSurface(Tile):
    def __init__(self):
        super().__init__("Surface")

class ScienceSite(Tile):
    def __init__(self):
        super().__init__("ScienceSite")

class OxygenScrubbers(Tile):
    def __init__(self):
        super().__init__("OxygenScrubber")

tyleskey = {
    0: MartianSurface,
    1: Habitat,
    2: Farm,
    3: SolarPanel,
    4: NuclearReactor,
    5: OxygenScrubbers,
    6: ScienceSite,
    7: LaunchSite
}