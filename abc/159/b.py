s = input()
n = len(s)

s_lh_r = s[n//2+1:][::-1]
s_fh = s[:n//2]

if not s_lh_r == s_fh:
    print("No")
    exit()

n = len(s_fh)

if not s_fh[:n//2] == s_fh[n//2+1:][::-1] or not s_lh_r[:n//2] == s_lh_r[n//2+1:][::-1]:
    print("No")
    exit()

print("Yes")
