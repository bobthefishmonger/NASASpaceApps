class Population:
    def __init__(self, size):
        self.size = size
        self.assigned = 0
        self.unassigned = self.size - self.assigned

    def assignWorkers(self, numWorkers):
        if self.unassigned >= numWorkers:
            self.assigned += numWorkers
            self.unassigned -= numWorkers
            return True
        return False

    def unassignWorkers(self, numWorkers):
        if numWorkers <= self.assigned:
            self.assigned -= numWorkers
            self.unassigned += numWorkers
            return True
        return False

    def addWorkers(self, numWorkers):
        self.size += numWorkers
        self._setUnassignedWorkers()

    def removeWorkers(self, numWorkers):
        if numWorkers >= self.size:
            raise Exception("Loss of all Workers")
        self.size -= numWorkers
        self.assignWorkers -= numWorkers
