import numpy as np


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
        self.state = 0 # 0 waiting -1 down 1 up
        self.up = np.array([])
        self.down = np.array([])
    def waitingTime(self,time,flag):
        totalTime = 0
        if self.state == 1:
            people=self.waitingPeople
            amountOfFloors = self.up[0] - self.pos
            allSpeed = self.stopTime + self.openTime
            totalTime = curTime = (amountOfFloors/self.speed) + allSpeed
            if curTime >= time:
                return time*people
            totalTime = totalTime*people
            # people --
            ind = 1
            anotherAllSpeed = self.startTime+self.closeTime+allSpeed
            while curTime < time and len(self.up)>ind:
                    amountOfFloors = self.up[ind] - self.up[ind-1]
                    ind+=1
                    curTime = curTime+amountOfFloors*self.speed+anotherAllSpeed
                    #people --





    # current position state =1

    def __str__(self):
        return f"elev ID: {self.id}  start time: {self.startTime}  stop time: {self.stopTime}  open time: {self.openTime} +  close time: {self.closeTime}  max floor: {self.maxFloor}  min floor: {self.minFloor}  speed: {self.speed}  pos: {self.pos} "
