import math

balance_before = 0
balance_a = 100
balance_b = 100

for i in range(3760):
    balance_a += balance_a // 100
    balance_b += math.floor(balance_b*0.01)
    if balance_a != balance_b:
        print(i)
        print(balance_a)
        print(balance_b)
        print(balance_before)
        break
    balance_before = balance_a