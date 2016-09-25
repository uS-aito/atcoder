#coding:utf-8

height, width, n = map(int,raw_input().split())
mass = [[0 for i in xrange(width)] for j in xrange(height)]
for list_ in mass:
	print list_
j = [0]*10

for i in xrange(n):
	y, x = map(int,raw_input().split())
	mass[y-1][x-1] = 1
	for list_ in mass:
		print list_

result = 0
for x in xrange(width-2):
	for y in xrange(height-2):
		for n_x in xrange(x,x+3):
			for n_y in xrange(y,y+3):
				result = result + mass[n_y][n_x]
		j[result] = j[result]+1
		result = 0

for i in j:
	print i