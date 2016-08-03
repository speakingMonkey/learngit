#/usr/bin/python
# -*- coding:utf-8 -*-
###author:lrn
#两个元素个数一样的整数列表，将两个列表的元素互换，使得两个列表的和之差最小
#思路：先将两个列表放在一起排序，最大的元素放列表A，次大的两个放列表B，往后的
# 元素优先放在列表和较小的列表
def listSort(list1,list2):
	list3 = list1 + list2
	list4 = sorted(list3)
	print list4
	print list4[-3:-1]
	list5 = []
	list6 = []
	list5.append(list4[-1])
	list6.append(list4[-2])
	list6.append(list4[-3])
	x = len(list4)-4
	y = len(list1)
	print "sorted before......"
	print '------------------------------'
	for i in range(-4,-len(list4)-1,-1):
		if sum(list5) > sum(list6):
			list6.append(list4[i])
			if len(list6)==len(list5)==len(list1):
				break
		else:
			list5.append(list4[i])
			if len(list5)==len(list6)==len(list1):
				break
	print "list1:",
	print list5
	print "list2:",
	print list6
if __name__ == '__main__':
	list1=[]
	list2=[]
	s1 = raw_input("Please input list A,and by the douHao seperate:")
	s2 = raw_input("Please input list B,and by the douHao separate,the same length to A:")
	listA = s1.split(',')
	listB = s2.split(',')
	for i in listA:
		list1.append(int(i))
	for i in listB:
		list2.append(int(i))
	print list1
	print list2
	listSort(list1,list2)
