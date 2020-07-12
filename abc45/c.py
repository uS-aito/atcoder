#coding:utf-8
import math

data = raw_input()
len_data = len(data)
split_point = []
range_max = 2**(len_data-1)
for i in xrange(range_max):
	split_point.append(format(i,"0"+str(int(math.log(range_max,2)))+"b"))
result = 0
bias = 0
for bit_str in split_point:
	origin = data
	for i in xrange(len(bit_str)):
		if bit_str[i] == "1":
			origin = origin[:i+1+bias] + "+" + origin[i+1+bias:]
			bias = bias+1
	result = result + eval(origin)
	bias = 0
print result