import numpy as np
import Building
import Calls
import Call
import Elevator


class Algo:
    def __init__(self, building, calls):
        self.building = building
        self.calls = calls
        self.ind = 0
        self.avg()
        self.aloc()

    def avg(self):
        for i in self.building.elevators: i.waiting = self.calls.length/(self.calls.length*i.waiting)

    def aloc(self):
        self.avg()
        for elev in self.building.elevators:
            for ind in range(self.calls.length):
                self.firstInd()
                if ind*elev.waiting < self.calls.length:
                    ind1 = ind * elev.waiting
                    self.calls.calls[int(ind1)].allocate(elev.id)


    def firstInd(self):
        while self.ind<len(self.calls.calls) and self.calls.calls[self.ind].allocatedTo != -1: self.ind += 1
