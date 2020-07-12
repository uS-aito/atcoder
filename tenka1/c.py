n = int(input())-1
s = [x for x in input()]
count_a = 0

for i in range(len(s)-1):
    if(s[i] == "#" and s[i+1] == "."):
        s[i+1] = "#"
        count_a = count_a + 1

count_b = 0
for i in range(len(s)-1):
    if(s[n-i] == "#" and s[n-(i+1)] == "."):
        s[n-(i+1)] = "."
        count_b = count_b + 1

if count_a >= count_b:
    count = count_a
else:
    count = count_b

print(count)
