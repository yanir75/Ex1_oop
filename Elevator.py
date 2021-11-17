

from Calls import Calls
from Call import Call
import copy
import Building


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
        self.calls = []  # self.calls_of_elev = Calls()
        self.sim = []
        self.flag = 0
        self.num_of_floors = 0
        self.fixed_dist = 0
        self.startFrom = 0
        self.time = 0
        self.ind = 0
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

    def check_done_calls(self , li):
        for i in li:
            if i.status==3:
                li.remove(i)
                return False
        return True
    def curr_pos(self):
        ind = 0
        self.time = 0
        li = self.timeBetweenCalls()
        g = len(li)
        while self.ind < g:
            i = li[ind]
            self.ind+=1
            f=len(self.sim)
            if f>0 and self.fixed_dist > 0:
                dif = abs(self.pos - self.sim[0])
                self.time = self.dister(self.fixed_dist, i, dif,self.startFrom)

            if f>0:
                dif = abs(self.pos - self.sim[0])
                dist = self.openTime + self.stopTime + self.closeTime + self.startTime + (dif / self.speed)
                self.time = self.dister(dist,i,dif)
                while self.time == -2:
                    self.pos = self.sim[0]
                    del self.sim[0]
                    self.fixed_dist = 0
                    if f == 0 and self.check_done_calls(self.calls):
                            self.fixed_dist = 0
                            self.state = 0
                            return None
                    else:
                        if f > 0:
                            self.time = i - dist
                        dif = abs(self.pos - self.sim[0])
                        dist = self.openTime + self.stopTime + self.closeTime + self.startTime + (dif / self.speed)
                        self.time = self.dister(dist, self.time, dif)
                    if f == 0:
                        self.time = -3
                        self.flag=0
                if self.time == -1:
                    self.pos = self.sim[0]
                    del self.sim[0]
                if self.flag == 1:
                    self.flag = 1
                    self.fixed_dist = self.time
                if self.flag > 2:
                    self.fixed_dist = self.time
            if self.sim ==0:
                self.state = 0
            for i in self.calls:
                lc = len(self.calls)
                if self.state == 1 and ind < lc:
                    self.add_call_to_route_1(self.self.callsls[ind])
                    ind+=1
                if self.state == -1 and ind < lc:
                    self.add_call_to_route_2(self.calls[ind])
                    ind+=1
                if self.state == 0 and ind < lc:
                    self.add_call_to_route_0(self.calls[ind])
                    ind+=1

    def dister(self,dist,time,dif,start=-1):
        if dist < time and start <0:
                self.flag = -1
                return -2
        elif dist == time and start <0:
                self.flag = -1
                return -1
        if time >= self.closeTime and start < 1:
            dist = dist - self.closeTime
            time = time - self.closeTime
            self.startFrom =1
        else:
            self.flag = 0
            self.startFrom = 0
            return dist - time
        if time >= self.startTime and start < 2:
            dist = dist - self.startTime
            time = time - self.startTime
            self.startFrom =2
        else:
            self.flag = 1
            self.startFrom = 1
            return dist - time
        if time >= dif/self.speed and start < 3:
            dist = dist - dif/self.speed
            time = time - dif/self.speed
            self.startFrom = 3
        else:
            self.flag = 2
            ind = 0.0
            count = 0
            while ind < dif:
                if ind/self.speed < time:
                    if self.state == 1:
                        count+=1
                    if self.state == -1:
                        count+=-1
                    ind+=1
            self.num_of_floors = count
            self.startFrom =2
            self.pos = self.pos + count
            return dist - time
        self.pos = self.sim[0]
        del self.sim[0]
        if time >= self.stopTime and start < 4:
            self.flag = 4
            dist = dist - self.stopTime
            time = time - self.stopTime
            self.startFrom =4
        else:
            self.startFrom = 3
            return dist-time
        if time >= self.closeTime:
            self.startFrom =0
            self.flag = 0
            self.fixed_dist = 0
            return -2
        self.flag == 4
        return dist - time

    def add_call_to_route_0(self, call):
        self.sim.append(call.src)
        call.status = 2
        if call.src > self.pos:
            self.state == 1
        elif call.src < self.pos:
            self.state == -1
        else:
            self.sim.remove(call.src)
            if call.dest > self.pos:
                self.state == 1
                self.sim.append(call.dest)
                call.status = 3
            elif call.dest < self.pos:
                self.state == -1
                self.sim.append(call.dest)
                call.status = 3

    def add_call_to_route_1(self, call):
        if call.src >= self.pos:
            self.sim.append(call.src)
            call.status = 2
        if call.dest >= call.src >= self.pos:
            self.sim.append(call.dest)
            call.status = 3

    def add_call_to_route_2(self, call):
        if call.src <= self.pos:
            self.sim.append(call.src)
            call.status = 2
        if call.dest <= call.src <= self.pos:
            self.sim.append(call.dest)
            call.status = 3

    def timeBetweenCalls(self):
        l = len(self.calls)
        if l > 0:
            li = [float(self.calls[0].time)]
            for i in range(1, l):
                li.append(float(self.calls[i].time) - float(self.calls[i - 1].time))
            return li
        return []
