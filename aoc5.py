# NOT SOLVED PART 2
# Tried to solve part to with solution from 0x8b: https://github.com/0x8b/advent-of-code-2019


data = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,86,8,225,1101,82,69,225,101,36,65,224,1001,224,-106,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,102,52,148,224,101,-1144,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,70,45,225,1002,143,48,224,1001,224,-1344,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1101,69,75,225,1001,18,85,224,1001,224,-154,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,15,59,225,1102,67,42,224,101,-2814,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1101,28,63,225,1101,45,22,225,1101,90,16,225,2,152,92,224,1001,224,-1200,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1101,45,28,224,1001,224,-73,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,14,118,224,101,-67,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,374,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,434,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,539,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,226,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,659,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226"

# data = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,86,8,225,1101,82,69,225,101,36,65,224,1001,224,-106,224,4,224,1002,223,8"
# data = "1001, 4, 3, 4, 33"
data = data.split(",")


# def intcode(opcode):
#     params = []
#     for p in range(1, num_params + 1):
#         params.append(data[opcode + p])

#     if data[opcode] == "01":
#         data[params[2]] = data[params[0]] + data[params[1]]
#         next_opcode += 4
#         return True, next_opcode

#     elif data[opcode] == "02":
#         data[params[2]] = data[params[0]] * data[params[1]]
#         next_opcode += 4
#         return True, next_opcode

#     elif data[opcode] == "99":
#         return False, 0

#     else:
#         return False, 0


# def find_value(instruction_pointer):

#     ## Loop through the data and Intcode it
#     while instruction_pointer + 4 <= len(data):
#         go, instruction_pointer = intcode(instruction_pointer)
#         if go == False:
#             break
#     return data[0], data[1], data[2]


def op_add(position, param_modes, params):
    res = 0
    for i, p in enumerate(param_modes[:2]):
        if p == "0":
            res += int(data[int(params[0])])
            # print(params[0], res)
        if p == "1":
            res += int(params[1])
            # print(params[1], res)
    # print(param_modes[2])
    if param_modes[2] == "0":
        data[int(params[2])] = str(res)
    if param_modes[2] == "1":
        data[pointer + 3] = str(res)
    return res


def op_multi(position, param_modes, params):
    res = 0
    for i, p in enumerate(param_modes[:2]):
        if p == "0":
            res *= int(data[int(params[0])])
            # print(params[0], res)
        if p == "1":
            res *= int(params[1])
            # print(params[1], res)
    # print(param_modes[2])
    if param_modes[2] == "0":
        data[int(params[2])] = str(res)
    if param_modes[2] == "1":
        data[pointer + 3] = str(res)
    return res


pointer = 2
opcode = str(data[0][-2:])
valid_opcodes = ["01", "02", "99"]

while opcode != "99":
    if int(opcode) % 5 == 0:
        print("------------------- ", opcode)

    instruction = data[pointer]
    next_opcode = str(data[pointer + len(instruction)])
    if len(instruction) < 5:
        instruction = f"{instruction:0>5}"

    opcode = instruction[-2:]

    params = list(p for p in data[pointer + 1: pointer + 4])
    param_modes = list(p for p in instruction[-3::-1])
    # print(instruction)
    # print(params)
    # print(param_modes)

    if opcode == "01":
        print(op_add(pointer, param_modes, params))
        opcode = next_opcode
        if int(next_opcode) <= len(data):
            pointer = int(opcode)
        else:
            print("Out of list")
            break

    elif opcode == "02":
        print(op_multi(pointer, param_modes, params))
        print(data)
        opcode = next_opcode
        if int(next_opcode) <= len(data):
            pointer = int(opcode)
        else:
            print("Out of list")
            break

    elif opcode == "03":
        pass

    elif opcode == "99":
        print("OPCODE 99 RECIEVED")
        break

    # elif data[opcode] == "02":
    #     data[params[2]] = data[params[0]] * data[params[1]]
    #     next_opcode += 4

    # elif data[opcode] == "99":
    #     break


"""
for n in data:
      if len(n) < 5:
        n = f"{n:0>5}"

    opcode = n[-2:]
    params = list(p for p in n[-3::-1])
    # print("Opcode:", n[-2:])
    # print("Params 1,2,3:", n[-3::-1])

    print(opcode, params)

n = 4
print(f"{n:03}")
"""
