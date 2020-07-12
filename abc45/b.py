#coding:utf-8

a_list = list(raw_input())
b_list = list(raw_input())
c_list = list(raw_input())

mode = "a"
while(True):
	if mode == "a":
		if len(a_list) == 0:
			print "A"
			break
		mode = a_list.pop(0)
	elif mode == "b":
		if len(b_list) == 0:
			print "B"
			break
		mode = b_list.pop(0)
	elif mode == "c":
		if len(c_list) == 0:
			print "C"
			break
		mode = c_list.pop(0)
	else:
		print "Invalid Input"
		break
