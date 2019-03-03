A, B, K = [int(x) for x in input().split(" ")]

warikiru = []
for i in range(1, min([A,B])+1):
    if A % i == 0 and B % i == 0:
        warikiru.append(i)

warikiru.reverse()
print(warikiru[K-1])