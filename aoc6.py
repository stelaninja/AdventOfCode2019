# Solved with solution from 0x8b: https://github.com/0x8b/advent-of-code-2019

with open("./AdventOfCode2019/input6.txt", "r") as f:
    c = f.read()
    data = c.rstrip().split("\n")


# data = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L"
# data = data.split(",")

num_of_orbits = 1
check_dict = {}
pointer = 0

for i, d in enumerate(data):
    data[i] = data[i].split(")")


next_value = data[0][0]

for d in data:
    if d[0] not in check_dict:
        check_dict[d[1]] = 1
        print(d[0], d[1], check_dict[d[1]])

    elif d[0] in check_dict:
        check_dict[d[1]] = check_dict[d[0]] + 1
        print(d[0], d[1], check_dict[d[0]], "----------")


"""
    if d[0] == next_value and d[0] not in check_dict:
        num_of_orbits += 1
        check_dict[d[1]] = num_of_orbits
        next_value = d[1]
        print(d[0], d[1], num_of_orbits)
        print(check_dict)

    elif d[0] == next_value and d[0] in check_dict:
        next_value = d[1]
        check_dict[d[1]] = num_of_orbits + check_dict[d[0]]
        print(d[0], d[1], num_of_orbits, "----------")
        print(check_dict)

    elif d[0] != next_value and d[0] in check_dict:
        check_dict[d[1]] = check_dict[d[0]] + 1
        next_value = d[1]
        print(d[0], d[1], num_of_orbits)
        print(check_dict[d[0]])

    elif d[0] != next_value and d[0] not in check_dict:
        check_dict[d[1]] = 1
"""

# print(check_dict)
print(check_dict)
print(sum(check_dict.values()))
# print(data)
