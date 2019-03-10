N, M, C = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
A = []
for i in range(N):
    A.append([int(x) for x in input().split()])

count = 0
for a in A:
    tmp = 0
    for i, j in zip(a,B):
        tmp += i*j
    tmp += C
    if tmp > 0:
        count += 1

print(count)