import random


class Call:
    def __init__(self, call):
        self.kind = call[0]
        self.time = float(call[1])
        self.src = int(call[2])
        self.dest = int(call[3])
        self.status = int(call[4])
        self.allocatedTo = int(call[5])

    # def allocate(self, building):
    #     size = len(building.elevators)
    #     num = random.randint(0, size)
    #     self.allocatedTo = 0
    def allocate(self,ind):
        self.allocatedTo = ind
    def get_call(self):
        return self

    def __str__(self):
        return f"{self.kind},{self.time},{self.src},{self.dest},{self.status},{self.allocatedTo}"

