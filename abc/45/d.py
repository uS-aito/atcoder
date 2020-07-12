#coding:utf-8

# 升目の高さ、幅、塗りつぶし回数
height, width, n = map(int,raw_input().split())

# 升目の生成処理
mass = {}
# 升目の塗りつぶし処理
for i in xrange(n):
	a, b = map(int,raw_input().split())
	if mass.has_key(a-1):
		mass[a-1].append(b-1)
	else:
		mass.update({a-1:[b-1]})

# 計算
result = 0
j = [0]*10

for y in xrange(height-2):
	for x in xrange(width-2):
		for n_y in xrange(y,y+3):
			try:
				for n_x in mass[n_y]:
					if n_x >= x and n_x < x+3:
						result = result + 1
			except:
				pass
		j[result] = j[result] + 1
		result = 0

for i in j:
	print i

# # 升目の生成処理
# mass = [[] for i in xrange(height)]

# # 升目の塗りつぶし処理
# for i in xrange(n):
# 	a, b = map(int, raw_input().split())
# 	if len(mass[a-1]) < b-1:
# 		for i in xrange(b-2-len(mass[a-1])+1):
# 			mass[a-1].append(0)
# 	mass[a-1].append(1)

# # jとresultを定義
# j = [0]*10
# result = 0

# # 塗りつぶした升目をカウント
# for y in xrange(height-2):
# 	for x in xrange(width-2):
# 		for n_y in xrange(y,y+3):
# 			for n_x in xrange(x,x+3):
# 				try:
# 					result = result + mass[n_y][n_x]
# 				except:
# 					pass
# 		j[result] = j[result]+1
# 		result = 0

# for i in j:
# 	print i

# 
# mass = [[0 for i in xrange(width)] for j in xrange(height)]
# for list_ in mass:
# 	print list_
# j = [0]*10

# for i in xrange(n):
# 	y, x = map(int,raw_input().split())
# 	mass[y-1][x-1] = 1
# 	for list_ in mass:
# 		print list_

# result = 0
# for x in xrange(width-2):
# 	for y in xrange(height-2):
# 		for n_x in xrange(x,x+3):
# 			for n_y in xrange(y,y+3):
# 				result = result + mass[n_y][n_x]
# 		j[result] = j[result]+1
# 		result = 0

# for i in j:
# 	print i