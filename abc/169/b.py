input()
nums = list(map(int,input().split()))

if nums.count(0):
    print(0)
    exit(0)

result=1
for i in nums:
    result *= i
    if result > (10**18):
        print(-1)
        exit(0)
print(result)