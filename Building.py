class Building:

    def __init__(self, building):
        self.maxFloor = building[0].maxFloor
        self.elevators = building
        self.minFloor = building[0].minFloor

    def getElev(self, elev):
        return self.elevators[elev]
