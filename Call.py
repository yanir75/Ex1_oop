from Elevator import Elevator


class Call:
    def __init__(self, call):
        self.kind = call[0]
        self.time = float(call[1])
        self.src = int(call[2])
        self.dest = int(call[3])
        self.status = int(call[4])
        self.allocatedTo = int(call[5])

    def allocate(self, elev):
        self.allocatedTo = elev

    def speed(self, elev):
        el = Elevator(elev)
        timeToSrc = el.closeTime + el.startTime + abs(el.pos - self.src) / el.speed + el.stopTime + el.openTime
        timeToDest = el.closeTime + el.startTime + abs(el.dest - self.src) / el.speed + el.stopTime + el.openTime
        return timeToDest+timeToSrc

    def __str__(self):
        return f"{self.kind},{self.time},{self.src},{self.dest},{self.status},{self.allocatedTo}"
