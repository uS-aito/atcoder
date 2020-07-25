n = int(input())
a = list(map(int,input().split()))
genkin = 1000
kabu = 0

kabusaidai = a.index(max(a))
if kabusaidai == 0:
    print(genkin)
    exit(0)

for i in range(kabusaidai):
    # すべて現金
    genkin_tmp = genkin + a[i] * kabu

    # すべて株
    kazu = genkin//a[i]
    kabu_tmp = genkin - kazu * a[i] + kazu * a[i+1]

    if genkin_tmp > kabu_tmp:
        genkin = genkin + kabu * a[i]
        kabu = 0
    elif genkin_tmp < kabu_tmp:
        genkin = genkin - kazu * a[i]
        kabu = kabu + kazu
    
    if i == kabusaidai:
        break

print(genkin + kabu * a[kabusaidai])