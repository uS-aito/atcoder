n,k=map(int,input().split())
prices = sorted(map(int,input().split()))

print(sum(prices[:k]))