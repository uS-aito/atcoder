A, B = [int(x) for x in input().split()]

# xor = A
# for i in range(A+1,B+1):
#     xor = xor ^ i

# print(xor)

# 入力受付
# 一番下の桁の1を判定
# A,Bを2で割ってint
# 繰り返し

# def is_one(A,B):
#     if A%2==0 and B%2==0:
#         num_of_odd = int((B+1-A)/2-0.5)
#     elif (A+B)%2==1:
#         num_of_odd = (B+1-A)/2
#     else:
#         num_of_odd = int((B+1-A)/2+0.5)
    
#     if num_of_odd%2==1:
#         return 1
#     else:
#         return 0

def is_one(target):
    if len(target)%2 == 1:
        return 1
    else:
        return 0

result = ""
# target = list(range(A,B+1))
target = [x/2 for x in range(A,B+1) if x/2!=0]
while True:
    # sum_target = sum(target)
    if(len(target) == 0):
        break

    result = str(is_one(target)) + result
    target = [int(x/2) for x in target]

print(int(result,2))