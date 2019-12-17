import numpy as np
from collections import Counter

with open("./AdventOfCode2019/input8.txt", "r") as f:
    c = f.read()

x = 25
y = 6
z = int(len(c) / (x * y))

data = np.array([int(p) for p in c])
data = np.reshape(data, (z, y, x))

zero_dict = {}
one_dict = {}
two_dict = {}

for i, layer in enumerate(data):

    zeros, ones, twos = 0, 0, 0
    for row in range(len(layer)):
        zeros += Counter(layer[row])[0]
        ones += Counter(layer[row])[1]
        twos += Counter(layer[row])[2]

    zero_dict[i] = zeros
    one_dict[i] = ones
    two_dict[i] = twos

lowest_zero_layer = min(zero_dict, key=zero_dict.get)
ones_in_layer = one_dict[lowest_zero_layer]
twos_in_layer = two_dict[lowest_zero_layer]


print(
    f"Layer {lowest_zero_layer}: {zero_dict[lowest_zero_layer]} zeros, {ones_in_layer} ones and {twos_in_layer} twos."
)

print(f"The product of ones and twos: {ones_in_layer * twos_in_layer}")


image = np.zeros(shape=(y, x))

for layer in data[::-1]:
    image = np.where(layer == 0, "_", image)
    image = np.where(layer == 1, 1, image)


for line in image:
    line_str = np.array_str(line).replace(".", "")
    line_str = line_str.replace("[", "")
    line_str = line_str.replace("]", "")
    line_str = line_str.replace(" ", "")
    line_str = line_str.replace("'", "")
    line_str = line_str.replace("_", " ")
    line_str = line_str.replace("1", "X")
    line_str = line_str.replace("\n", "")
    print(line_str)

