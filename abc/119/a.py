import datetime

s = input()

# 閾値
th =  datetime.datetime.strptime("2019/04/30","%Y/%m/%d")
dt = datetime.datetime.strptime(s,"%Y/%m/%d")

if dt <= th:
    print("Heisei")
else:
    print("TBD")