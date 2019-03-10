H, W = [int(x) for x in input().split()]
h, w = [int(x) for x in input().split()]

last = H*W - (H*w + W*h - h*w)
print(last)