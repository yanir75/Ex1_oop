class Building:

    def __init__(self, building):
        self.maxFloor = building['_maxFloor']
        self.elevators = building['_elevators']
        self.minFloor = building['_minFloor']

    def getElev(self, elev):
        return self.elevators[elev]
