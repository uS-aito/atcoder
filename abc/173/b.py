n = int(input())

results = []
for i in range(n):
    results.append(input())

print("AC x",results.count("AC"))
print("WA x",results.count("WA"))
print("TLE x",results.count("TLE"))
print("RE x",results.count("RE"))