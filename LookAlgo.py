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
        for i in self.building.elevators: i.waiting = i.waiting / len(self.calls.calls)

    def aloc(self):
        for i in self.building.elevators:
            if len(self.calls.calls) > self.ind:
                self.firstInd()
            else:
                break
            for k in np.arange(self.ind, len(self.calls.calls), i.waiting):
                if k < len(self.calls.calls) and self.calls.calls[int(k)]==-1:
                    self.calls.calls[int(k)].allocate(i.id)

    def firstInd(self):
        while self.ind<len(self.calls.calls) and self.calls.calls[self.ind].allocatedTo != -1: self.ind += 1
