N = int(input())
otoshidama = []
for i in range(N):
    x, u = input().split(" ")
    otoshidama.append([float(x),u])

ypb = 380000.0
sum = 0.0

for x,u in otoshidama:
    if u == "JPY":
        sum += x
    else:
        sum += ypb * x

print(sum)