import resources
from map import STARTINGMAP
from population import Population

tiles = {
    "Farm": [],
    "SolarPanel": [],
    "NuclearReactor": [],
    "Habitat": [],
    "LaunchSite": [],
    "MartianSurface": [],
    "ScienceSite": [],
    "OxygenScrubber": [],
}


class Map:
    def __init__(self):
        self.grid = STARTINGMAP
        for i, row in enumerate(STARTINGMAP):
            for j, tile in enumerate(row):
                self.grid[i][j] = tileskey[tile](j, i)

    def build(self, x, y, buildType):
        self.grid[y][x] = tileskey[buildType]()

    def getTile(self, x, y):
        return self.grid[y][x]

    def __str__(self):
        return "\n".join(", ".join(str(item) for item in row) for row in self.grid)


class Tile:
    def __init__(self, name, x, y):
        self.coords = (x, y)
        self.name = name
        tiles[self.name].append(self)

    def onclick(self): ...

    def __str__(self):
        return self.name


class ResourceTile(Tile):
    def __init__(self, name, x, y, resource, resourceScale):
        self.resource = resource
        self.workerNum = 0
        self.active = True
        self.resourceModifier = 1
        self.resourceScale = resourceScale
        self.resource.setModifier(self.resourceModifier)
        super().__init__(name, x, y)

    def destory(self):
        self.active = False
        GamePopulation.removeWorkers(self.workerNum)

    def repair(self):
        self.active = True

    def generateResource(self):
        if not self.active:
            return 0

    def addWorker(self, numWorkers):
        if GamePopulation.assignWorkers(numWorkers):
            self.workerNum += numWorkers
            self.resource.addResource(self.workerNum)
        else:
            raise Exception("Insufficient Workers")

    def removeWorker(self, numWorkers):
        if GamePopulation.unassignWorkers(numWorkers):
            self.workerNum -= numWorkers
            self.resource.removeResource(self.workerNum)
        else:
            raise Exception("Insufficient Workers")

        self.workerNum -= numWorkers

    def upgrade(self):
        self.resourceModifier += 1
        self.resources.setModifiers(self.resourceModifier)


class Farm(ResourceTile):
    def __init__(self, x, y):
        super().__init__("Farm", x, y, resources.Generator("Food"), 1)


class SolarPanel(ResourceTile):
    def __init__(self, x, y):
        super().__init__("SolarPanel", x, y, resources.Generator("Power"), 1)


class NuclearReactor(ResourceTile):
    def __init__(self, x, y):
        super().__init__("NuclearReactor", x, y, resources.Generator("Power"), 2)


class Habitat(Tile):
    def __init__(self, x, y):
        super().__init__("Habitat", x, y)


class LaunchSite(Tile):
    def __init__(self, x, y):
        super().__init__("LaunchSite", x, y)


class MartianSurface(Tile):
    def __init__(self, x, y):
        super().__init__("MartianSurface", x, y)


class ScienceSite(Tile):
    def __init__(self, x, y):
        self.workerNum = 0
        self.active = True
        super().__init__("ScienceSite", x, y)

    def addWorker(self, numWorkers):
        if GamePopulation.assignWorkers(numWorkers):
            self.workerNum += numWorkers
        else:
            raise Exception("Insufficient Workers")

    def removeWorker(self, numWorkers):
        if GamePopulation.unassignWorkers(numWorkers):
            self.workerNum -= numWorkers
        else:
            raise Exception("Insufficient Workers")

    def destroy(self):
        GamePopulation.removeWorkers(self.assigned)
        self.active = False

    def repair(self):
        self.active = True


class OxygenScrubber(Tile):
    def __init__(self, x, y):
        self.active = True
        super().__init__("OxygenScrubber", x, y)

    def destroy(self):
        self.active = False
        GameOxygen.removeScrubber()

    def repair(self):
        self.active = True
        GameOxygen.addScrubber()


tileskey = {
    0: MartianSurface,
    1: Habitat,
    2: Farm,
    3: SolarPanel,
    4: NuclearReactor,
    5: OxygenScrubber,
    6: ScienceSite,
    7: LaunchSite,
}

GameMap = Map()
GamePopulation = Population(100)
GameOxygen = resources.Oxygen()
