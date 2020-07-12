#coding:utf-8 

a = int(raw_input())
b_and_c = map(int, raw_input().split())
s = raw_input()
# print a+sum(b_and_c,0),
# print s
print "{0} {1}".format(a+sum(b_and_c,0),s)