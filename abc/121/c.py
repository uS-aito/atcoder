N, M = [int(x) for x in input().split()]
shops = []
for i in range(N):
    shops.append([int(x) for x in input().split()])

shops.sort(key=lambda x:x[0])

money = 0
last = M
for s in shops:
    if s[1] <= last:
        money += s[0] * s[1]
        last -= s[1]
    else:
        money += s[0] * last
        break

print(money)