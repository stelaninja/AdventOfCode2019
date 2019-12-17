# NOT SOLVED

import numpy as np
import json

with open("./AdventOfCode2019/input12.txt") as file:
    data = [line.rstrip("\n") for line in file.readlines()]

new_data = []
for row in data:
    row = row.replace("<", "{").replace(">", "}").replace("=", ":")
    row = row.replace("x", '"x"').replace("y", '"y"').replace("z", '"z"')
    new_data.append(row)


data_dict = {}

for i, row in enumerate(new_data):
    planet = i
    data_dict[planet] = dict(json.loads(row))
    # print(row)

# print(data_dict)
# print(data_dict["P0"]["x"])


# Add velocity keys to planet dictionarys
vel = {"xv": 0, "yv": 0, "zv": 0}

for d in data_dict:
    data_dict[d].update(vel)

for row in data_dict:
    ax = 0
    ay = 0
    az = 0

    if row == len(data_dict) - 1:
        c = 0
    else:
        c = row + 1

    if data_dict[row]["x"] > data_dict[c]["x"]:
        ax += 1

    elif data_dict[row]["x"] < data_dict[c]["x"]:
        ax -= 1

        print(data_dict[row]["x"])
