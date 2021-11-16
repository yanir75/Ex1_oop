import csv
import json
from Building import Building
from Call import Call
from Calls import Calls
from Elevator import Elevator


def building_from_json(file_name):
    f = open(file_name)
    data = json.load(f)
    f.close()
    l1 = []
    for Any in data['_elevators']:
        l1.append(Elevator(Any))
    b = Building(l1[0].minFloor, l1[0].maxFloor, l1)
    return b


def calls_from_CSV(file_name):
    f = open(file_name)
    csv_reader = csv.reader(f)
    li = []
    for call in csv_reader:
        li.append(Call(call))
    return Calls(li)


def read_calculate_write(building_file, calls_file):
    try:
        with open(building_file) as parser:
            building = json.load(parser)
    except:
        print("The file is not a Json file!!")
    curr_building = Building(building)
    ind = 0
    for elev in building['_elevators']:

    print()

b = building_from_json("B5.json")
f = calls_from_CSV("Calls_d.csv")
f.alloc(b)
f.write_to_csv()
