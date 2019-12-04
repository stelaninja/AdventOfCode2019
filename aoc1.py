import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import timeit

from math import floor

inputs = [
    115919,
    56833,
    117651,
    56733,
    89472,
    91010,
    119618,
    85667,
    141042,
    106401,
    121495,
    50136,
    83755,
    122558,
    149188,
    110381,
    132060,
    145791,
    141381,
    136467,
    104712,
    133530,
    65297,
    52640,
    59637,
    78410,
    107791,
    96909,
    136738,
    109794,
    66831,
    58426,
    97955,
    90496,
    119294,
    83101,
    80466,
    114370,
    67631,
    106482,
    73996,
    50367,
    113976,
    68998,
    109714,
    96308,
    89350,
    143077,
    102052,
    93325,
    86870,
    94449,
    119448,
    53472,
    140668,
    64989,
    112056,
    88880,
    131335,
    94943,
    88061,
    122883,
    129059,
    55345,
    82362,
    60500,
    147652,
    83147,
    87106,
    97384,
    136883,
    62198,
    130290,
    129715,
    93082,
    72179,
    72109,
    70604,
    94894,
    98139,
    97056,
    86236,
    144191,
    108008,
    79225,
    93551,
    103116,
    130702,
    87599,
    143630,
    104476,
    108922,
    134209,
    85636,
    81591,
    127980,
    90425,
    126133,
    118135,
    93722,
]
test_input = [90, 150, 210]


def fuel_calc(w):
    x = floor(w / 3) - 2
    if x <= 0:
        return 0
    else:
        return x


fuel_required = []
fuel_for_fuel = []

for i in inputs:
    x = fuel_calc(i)
    # print(x)
    fuel_required.append(x)
# print("---")
print(sum(fuel_required))
# print("---")

fr_df = pd.Series(fuel_required)

for f in fuel_required:
    x = fuel_calc(f)
    # print(x)
    if x > 0:
        fuel_required.append(x)
        fuel_for_fuel.append(x)

print("---")
print(sum(fuel_required))

ff_df = pd.Series(fuel_for_fuel)

df = fr_df.append(ff_df, ignore_index=True)

# df = pd.concat([fr_df, ff_df], axis=1)
# df.columns = ["FR", "FF"]
# print(df.head())

x_lab = list(range(0, 878, 10))


fig, ax = plt.subplots(figsize=(15, 10))

ax = sns.barplot(x=df.index, y=df.values)

ax.set_xticks(x_lab)
ax.set_xticklabels(x_lab)

plt.xticks(rotation=90)
plt.xlabel("Iteration")
plt.ylabel("Fuel Mass")

plt.ion()
plt.show()
# plt.close()

