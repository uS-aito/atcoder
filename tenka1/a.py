zahyo = [int(x) for x in input().split()]
zahyo_sorted = sorted(zahyo)

if zahyo_sorted.index(zahyo[2]) == 1:
    print("Yes")
else:
    print("No")