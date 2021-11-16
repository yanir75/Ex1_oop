import csv
import random

import Call


class Calls:

    def __init__(self, calls):
        self.calls = calls
        self.spaceBetweenCall = self.timeBetweenCalls()

    # def __init__(self):
    #     self.calls = []
    #     self.spaceBetweenCall = -1

    def timeBetweenCalls(self):
        li = [float(self.calls[0].time)]
        for i in range(1, len(self.calls)):
            li.append(float(self.calls[i].time) - float(self.calls[i - 1].time))
        return li

    def write_to_csv(self):
        # https://www.pythontutorial.net/python-basics/python-write-csv-file/
        f = open("output.csv", "x")
        writer = csv.writer(f)
        for i in self.calls:
            li = [i.kind, i.time, i.src, i.dest, i.status, i.allocatedTo]
            writer.writerow(li)
        f.close()

    def alloc(self, b):
        size = len(b.elevators) - 1
        for i in self.calls:
            num = random.randint(0, size)
            i.allocatedTo = num
