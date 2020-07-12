import math
import sys

antenas = []
for i in range(5):
    antenas.append(int(input()))
k = int(input())

for f in antenas:
    for d in antenas:
        if abs(f-d) > k:
            print(":(")
            sys.exit(0)

print("Yay!")