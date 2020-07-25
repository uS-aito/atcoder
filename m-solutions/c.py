n,k = map(int,input().split())
a = list(map(int,input().split()))
memo = {}

for i in range(k,n):
    if a[i] > a[i-k]:
        print("Yes")
    else:
        print("No")

# tmp = 0
# before = 1
# for i in range(k):
#     tmp = before
#     before *= a[i]
# memo[k-1][0] = before
# memo[k-1][1] = tmp

# for i in range(k,n):
#     before = memo[i-1][0]
    
#     tmp = 0
#     after = 1
#     for j in range(k):
#         tmp = 
#         after *= a[i-j]
    
#     if before < after:
#         print("Yes")
#     else:
#         print("No")
    
#     memo[i] = after

# tmp = 0
# before = 1
# for j in range(k):
#     tmp = before
#     before *= a[k-j-1]
# memo[k-1] = [before,tmp]

# for i in range(k,n):
#     before = 1
#     after = 1

#     if not(i-1 in memo):
#         tmp = 0
#         for j in range(k):
#             tmp = before
#             before *= a[i-j-1]
#         memo[i-1] = [before,tmp]
#     else:
#         before = memo[i-1][0]

#     after = memo[i-1][1] * a[i]

#     # if not(i in memo):
#     #     for j in range(k):
#     #         after *= a[i-j]
#     #     memo[i] = after
#     # else:    
#     #     print("memoあり！")
#     #     after = memo[i]

#     if after > before:
#         print("Yes")
#     else:
#         print("No")