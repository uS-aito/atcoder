A, B, C = [int(x) for x in input().split(" ")]

if A*C <= B:
    print(C)
else:
    print(int(B/A))