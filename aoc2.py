orig_data = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    1,
    9,
    19,
    1,
    13,
    19,
    23,
    2,
    23,
    9,
    27,
    1,
    6,
    27,
    31,
    2,
    10,
    31,
    35,
    1,
    6,
    35,
    39,
    2,
    9,
    39,
    43,
    1,
    5,
    43,
    47,
    2,
    47,
    13,
    51,
    2,
    51,
    10,
    55,
    1,
    55,
    5,
    59,
    1,
    59,
    9,
    63,
    1,
    63,
    9,
    67,
    2,
    6,
    67,
    71,
    1,
    5,
    71,
    75,
    1,
    75,
    6,
    79,
    1,
    6,
    79,
    83,
    1,
    83,
    9,
    87,
    2,
    87,
    10,
    91,
    2,
    91,
    10,
    95,
    1,
    95,
    5,
    99,
    1,
    99,
    13,
    103,
    2,
    103,
    9,
    107,
    1,
    6,
    107,
    111,
    1,
    111,
    5,
    115,
    1,
    115,
    2,
    119,
    1,
    5,
    119,
    0,
    99,
    2,
    0,
    14,
    0,
]


# dataX = [2, 4, 4, 5, 99, 0]


def intcode(opcode):
    params = []
    for p in range(1, num_params + 1):
        params.append(data[opcode + p])

    if data[opcode] == 1:
        data[params[2]] = data[params[0]] + data[params[1]]
        opcode += 4
        return True, opcode

    elif data[opcode] == 2:
        data[params[2]] = data[params[0]] * data[params[1]]
        opcode += 4
        return True, opcode

    elif data[opcode] == 99:
        return False, 0

    else:
        return False, 0


def find_value(noun, verb, instruction_pointer):
    data[1] = noun
    data[2] = verb

    ## Loop through the data and Intcode it
    while instruction_pointer + 4 <= len(data):
        go, instruction_pointer = intcode(instruction_pointer)
        if go == False:
            break
    return data[0], data[1], data[2]


## Set parameters and input
num_params = 3
test_value = 19690720
go = True
instruction_pointer = 0


for n in range(100):
    for v in range(100):
        # Reset parameters
        data = orig_data[:]
        instruction_pointer = 0
        go = True

        # Run test and return first three adresses in data
        d1, d2, d3 = find_value(n, v, instruction_pointer)
        # print(n, v, d1)

        if d1 == test_value:
            print(d1, d2, d3)
            print(100 * d2 + d3)
            break

