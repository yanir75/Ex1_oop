

def calculate_route(call, elev):
    # 1 for UP -1 for DOWN
    call_type = call.status
    src_floor = call.src
    dest_floor = call.dest
    starting_time = call.time
    elev_pos = elev.pos
    elev_state = elev.state
    estimated_time = 0
    # call is up
    if call_type == 1 and (elev_state == 1 or elev_state == 0):
        elev_route = elev.up.copy()
        if len(elev_route) == 0 and elev_pos < src_floor < dest_floor:
            # route is empty
            estimated_time = elev.get_distance(elev_pos, src_floor) + elev.get_distance(src_floor, dest_floor)
        elif len(elev_route) != 0 and elev_pos > src_floor < dest_floor:
            # if the pos of the elev is grater then the src floor ->
            # first finish all the calls up
            # second start doing all the calls down and add the src floor
            # third add the dest to the new route up and finish that call
            for floor in elev_route:
                # finish all the calls up
                estimated_time += elev.get_distance(elev_pos, floor)
            estimated_time = estimated_time * (len(elev_route) / 2)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            elev_route = elev.down.copy()
            # add the src floor
            elev_route.append(src_floor)
            elev_route.sort(reverse=True)
            for floor in elev_route:
                # start to go over all the calls down
                estimated_time += elev.get_distance(last_pos, floor)
            estimated_time = estimated_time * (len(elev_route) / 2)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            estimated_time += elev.get_distance(last_pos, dest_floor)
            # now add the call to the route up again and calculate it
        else:
            # route is not empty and src + dest are up
            elev_route.append(src_floor)
            elev_route.append(dest_floor)
            elev_route.sort()
            for floor in elev_route:
                estimated_time += elev.get_distance(elev_pos, floor)
            estimated_time += estimated_time * (len(elev_route) / 2)
    # call is down
    elif call_type == -1 and (elev_state == 0 or elev_state == -1):
        elev_route = elev.down.copy()
        if len(elev_route) == 0 and elev_pos > src_floor > dest_floor:
            # route is empty
            estimated_time = elev.get_distance(elev_pos, src_floor) + elev.get_distance(src_floor, dest_floor)
        elif len(elev_route) != 0 and elev_pos < src_floor > dest_floor:
            # if the pos of the elev is lower than the src
            # first finish all the calls down
            # second start doing all the calls up and add the src floor
            # third add the dest to the new route down and finish that call
            for floor in elev_route:
                # finish all the calls down
                estimated_time += elev.get_distance(elev_pos, floor)
            estimated_time = estimated_time * (len(elev_route) / 2)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            elev_route = elev.up.copy()
            # add the src floor
            elev_route.append(src_floor)
            elev_route.sort()
            for floor in elev_route:
                # start to go over all the calls up
                estimated_time += elev.get_distance(last_pos, floor)
            estimated_time = estimated_time * (len(elev_route) / 2)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            estimated_time += elev.get_distance(last_pos, dest_floor)
            # now add the call to the route down again and calculate it
        else:
            # route is not empty and src + dest are down
            elev_route.append(src_floor)
            elev_route.append(dest_floor)
            elev_route.sort(reverse=True)
            for floor in elev_route:
                estimated_time += elev.get_distance(elev_pos, floor)
            estimated_time += estimated_time * (len(elev_route) / 2)
    return estimated_time






class MyAlgo:
    def __init__(self, building, calls):
        self.building = building
        self.calls = calls
        self.elevators = building.elevators
        self.route_up = [[]] * len(building.elevators)
        self.route_down = [[]] * len(building.elevators)


    def allocate_an_elevator(self, call):
        call_type = call.status
        src_floor = call.src
        dest_floor = call.dest
        starting_time = call.time
        MIN_estimated_time = 2 ^ 20
        ind_of_elev = -1
        for elev in self.elevators:
            curr_estimated_time = calculate_route(call, elev)
            if curr_estimated_time < MIN_estimated_time:
                MIN_estimated_time = curr_estimated_time
                ind_of_elev = self.elevators.id
#     if len(self.route_up[elev_id]) == 0 and elev_pos < src_floor:
#         self.route_up[elev_id].append(src_floor)
#         self.route_up[elev_id].append(dest_floor)
#     elif len(self.route_up[elev_id]) != 0 and elev_pos < src_floor:
#         self.route_up[elev_id].append(src_floor)
#         self.route_up[elev_id].append(dest_floor)
#         self.route_up[elev_id].sort()
#
#
# else:  # type = -1
#     if len(self.route_down[elev_id]) == 0 and elev_pos > src_floor:
#         self.route_down[elev_id].append(src_floor)
#         self.route_down[elev_id].append(dest_floor)
