a,b,c,k = map(int,input().split())

s=0
s += a
s -= (k-a-b) if k > a+b else 0

print(s)