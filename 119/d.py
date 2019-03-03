A, B, Q = [int(x) for x in input().split(" ")]
s = []
t = []
q = []

# 神社の座標
for i in range(A):
    s.append(int(input()))
# 寺の座標
for i in range(B):
    t.append(int(input()))
# 問題の座標
for i in range(Q):
    q.append(int(input()))

def saitika(current, zahyo):
    for i in range(len(zahyo)):
        try:
            if zahyo[i] <= current and current <= zahyo[i+1]]:
                hidari = i
                migi = i+1
                return (hidari, migi)
        except IndexError:
            hidari = i
            migi = None
            return (hidari, migi)

# 現在位置(current)から、指定された左右(sayu)の、指定された神社か寺(dotti)への距離を返す
def idou(current, sayu, dotti):
    if sayu == "hidari" and dotti == "tera":
        hidari, migi = saitika(current, t)
        kyori = current - t[hidari]
        return kyori
    elif sayu == "migi" and dotti == "tera":
        hidari, migi = saitika(current, t)
        if not migi is None:
            kyori = t[migi] - current
            return kyori
    elif sayu == "hidari" and dotti = "jinja":
        hidari, migi = saitika(current, s)
        kyori = current - s[hidari]
        return kyori
    elif sayu == "migi" and dotti = "jinja":
        hidari, migi = saitika(current, s)
        if not migi is None:
            kyori = s[migi] - current
            return kyori

def result(start):
    import copy

    houkou = ["hidari","migi"]
    dotti = ["tera", "jinja"]

    for i in houkou:
        for j in dotti:
            dotti_tmp = copy.deepcopy(dotti)
            dotti_tmp.remove(j)
            houkou_tmp = copy.deepcopy(houkou)
            for k in houkou_tmp:
                for l in dotti_tmp:
                    print(i,j,"->",k,l)        