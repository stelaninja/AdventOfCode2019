# PART 1 solved - needs refactoring to continue

from collections import deque
from itertools import islice

# Test strings
# str_signal = "12345678"
# str_signal = "80871224585914546619083218645595"

# Read the input and set the length of the base pattern
with open("AdventOfCode2019/input16.txt") as f:
    str_signal = f.read()

sig_len = len(str_signal)
base_pattern = deque([0, 1, 0, -1]) * int(sig_len / 4)

# Check if signal input is divisible by 4 or add remainder of base pattern
if sig_len % 4 != 0:
    l = sig_len % 4
    bap = deque(islice(base_pattern, 0, l))
    for b in bap:
        base_pattern.append(b)

signal = [int(c) for c in str_signal]


# Set phases and number of turns
phases = 100
turns = len(signal)


# Function to calculate the output
def fft(signal):
    tmp_signal = []
    for turn in range(1, turns + 1):
        new_pattern = deque()

        for num in base_pattern:
            for _ in range(0, turn):
                new_pattern.append(num)
        new_pattern.rotate(-1)
        new_pattern = deque(islice(new_pattern, 0, turns))

        tmp_signal.append(
            abs(sum([o*s for o, s in zip(new_pattern, signal)])) % 10)

    return tmp_signal


# Iterate over the phases
for p in range(phases):
    signal = fft(signal)
    if p % 10 == 0:
        print("Phase", p)

# Print last output and the first 8 digits of the output
result = "".join(map(str, signal))
print(result)
print(result[:8])
