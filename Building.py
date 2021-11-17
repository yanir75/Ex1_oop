import Elevator


class Building:

    def __init__(self, elevators):
        self.maxFloor = elevators[0].maxFloor
        self.elevators = elevators
        self.minFloor = elevators[0].minFloor
        self.total = sum([a.speed for a in elevators])
        self.update()

    def getElev(self, elev):
        return self.elevators[elev]

    def update(self):
        for a in self.elevators: a.waiting = a.speed / self.total
