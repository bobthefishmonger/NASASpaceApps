class Resource:
    def __init__(
        self,
        name,
    ):
        self.name = name
        self.num = 0
        self.demand = 0
        self.excess = self.num - self.demand
        self.modifier = 1

    def _calcExcess(self):
        self.excess = self.num - self.demand

    def addResource(self, num):
        self.num += num * self.modifier
        self._calcExcess()

    def removeResource(self, num):
        self.num -= num
        if self.num < 0:
            raise ValueError("Cannot remove from no resources")
        self._calcExcess()

    def setDemand(self, demand):
        self.demand = demand
        self._calcExcess()

    def setModifier(self, modifier):
        self.modifier = modifier


class Power(Resource):
    def __init__(self):
        super().__init__("Power")


class Food(Resource):
    def __init__(self):
        super().__init__("Food")


POWER = Power()
FOOD = Food()
RESOURCES = {"Power": POWER, "Food": FOOD}


class Generator:
    def __init__(self, resourceName):
        self.resource = RESOURCES[resourceName]

    def addResource(self, num):
        self.resource.addResource(num)

    def removeResource(self, num):
        self.resource.removeResource(num)

    def setModifier(self, modifier):
        self.resource.setModifier(modifier)


PERCENTPERTICK = 1


class Oxygen:
    def __init__(self):
        self.level = 100
        self.activeScrubbers = 0

    def addScrubber(self):
        self.activeScrubbers += 1

    def removeScrubber(self):
        self.activeScrubbers -= 1

    def ontick(self):
        insuffiency = 5 - self.activeScrubbers
        self.level = max(self.level + round(insuffiency * PERCENTPERTICK), 100)
        if self.level <= 0:
            raise Exception("Oxygen Depleted")

    def getLevel(self):
        return self.level
