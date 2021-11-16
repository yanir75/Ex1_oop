import random


class Call:
    def __init__(self, call):
        self.kind = call[0]
        self.time = call[1]
        self.src = call[2]
        self.dest = call[3]
        self.status = call[4]
        self.allocatedTo = call[5]

    def allocate(self, building):
        size = len(building.elevators)
        num = random.randint(0, size)
        self.allocatedTo = 0

    def get_call(self):
        return self

    def __str__(self):
        return f"{self.kind},{self.time},{self.src},{self.dest},{self.status},{self.allocatedTo}"

