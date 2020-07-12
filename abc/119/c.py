N, A, B, C = [int(x) for x in input().split(" ")]
take = []
for i in range(N):
    take.append(int(input()))

# すでに持ってる奴を除く
if A in take:
    take.remove(A)
if B in take:
    take.remove(B)
if C in take:
    take.remove(C)

# 総当たり
# 終了条件：必要な長さを揃える, 揃えなければならない本数より手持ちの本数が少なくなる
# 必要なもの：現在の手持ち    