import math

import numpy as np

from Calls import Calls


class Elevator:

    def __init__(self, elev):
        self.pos = 0
        self.stopTime = elev['_stopTime']
        self.startTime = elev['_startTime']
        self.openTime = elev['_openTime']
        self.closeTime = elev['_closeTime']
        self.maxFloor = elev['_maxFloor']
        self.minFloor = elev['_minFloor']
        self.speed = elev['_speed']
        self.id = elev['_id']
        self.waitingPeople = 0
        self.state = 0  # 0 waiting -1 down 1 up
        self.up = []
        self.down = []
        self.calls = []# self.calls_of_elev = Calls()
        self.sim = []

    def get_distance(self, src, dest):
        dif = abs(src - dest)
        dist = self.openTime + self.stopTime + self.closeTime + self.startTime + (dif / self.speed)
        return dist
    # def add_to_route(self, elev):
    #     elev_calls = self.calls_of_elev.calls
    #     if len(self.calls_of_elev.calls) == 1:
    #         if self.pos > elev_calls[0].src:
    #             self.down.append(elev_calls[0].src)
    #         elif self.pos < elev_calls[0].src:
    #             self.up.append(elev_calls[0].src)
    #         if elev_calls[0].dest > elev_calls[0].src or self.pos < elev_calls[0].dest:
    #             self.up.append(elev_calls[0].dest)
    #         else:
    #             self.down.append(elev_calls[0].dest)

    def __str__(self):
        return f"elev ID: {self.id}  start time: {self.startTime}  stop time: {self.stopTime}  open time: {self.openTime} +  close time: {self.closeTime}  max floor: {self.maxFloor}  min floor: {self.minFloor}  speed: {self.speed}  pos: {self.pos} "
