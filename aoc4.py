import itertools

input_data = range(234208, 765869 + 1)

result = []

# Check that the next number is >= to the former number
for data in input_data:
    test = True
    for l in range(len(str(data)) - 1):
        if str(data)[l] > str(data)[l + 1]:
            test = False
            break

    if test == True:
        result.append(data)

input_data = result
result = []

# Redundant for part 2 when implementing the next check.
"""
# Check that there are two adjacent equal numbers
for data in input_data:
    for l in range(len(str(data)) - 1):
        if str(data)[l] == str(data)[l+1]:
            result.append(data)
            break

input_data = result
result = []

"""
# Check if all two adjacent numbers is more than two
for data in input_data:
    sort = sorted(sum(1 for x in v) for _, v in itertools.groupby(list(str(data))))
    if 2 in sort:
        result.append(data)

print(len(result))
