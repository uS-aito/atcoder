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