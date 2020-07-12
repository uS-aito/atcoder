S = list(input())

def unif(s, i, count):

    s_tmp = s
    # 指定された箇所を排除
    try:
        del s_tmp[i]
        del s_tmp[i]
    except:
        import pdb; pdb.set_trace()
    count += 1

    # 排除しうるところを探す
    removable = []
    for j in range(len(s_tmp)-1):
        if s_tmp[j] != s_tmp[j+1]:
            print(s_tmp[j], s_tmp[j+1])
            removable.append(j)

    # 次を呼ぶ
    results = []
    id_tmp = id(removable)
    print("removable01_id:", id_tmp)
    for j in removable:
        print(count)
        print("removable02_id:", id(removable))
        print(s_tmp, j)
        print(id_tmp, id(removable))
        if(id_tmp == id(removable)):
            results.append(unif(s_tmp, j, count))
    
    if results != []:
        return max(results)
    else:
        return count

removable = []
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        removable.append(i)

results = []
for i in removable:
    results.append(unif(S, i, 0))

print(max(results)*2)