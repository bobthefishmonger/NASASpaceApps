class Resource:
    def __init__(self, name):
        self.name = name
        self.num = 0
        self.demand = 0
        self.excess = self.num - self.demand

    def _calcExcess(self):
        self.excess = self.num - self.demand
    
    def addResource(self, num):
        self.num += self.num
        self._calcExcess()

    def removeResource(self, num):
            self.num -= self.num
            if self.num < 0:
                raise ValueError("Cannot remove from no resources")
            self._calcExcess()

class Power(Resource):
     def __init__(self):
          super().__init__("Power")

class Food(Resource):
     def __init__(self):
          super().__init__("Food")

POWER = Power()
FOOD = Food()
RESOURCES = {
    "Power": POWER,
    "Food": FOOD
}


class Generator():
    def __init__(self, resourceName):
        self.resource = RESOURCES[resourceName]

    def addResource(self, num):
        self.resource.addResource(num)
        
    def removeResource(self, num):
         self.resource.removeResource(num)