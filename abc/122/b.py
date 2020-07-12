import math

menu = []
for i in range(5):
    menu.append(int(input()))

menu.sort(key = lambda x: int(x%10) if int(x%10) != 0 else 9,reverse=True)

sum = 0
for m in menu[:-1]:
    sum += math.ceil(m/10)*10

print(sum+menu[-1])