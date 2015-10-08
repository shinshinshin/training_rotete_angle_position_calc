#!/usr/bin/python
#-*- coding: utf-8 -*-
import pos

#最急降下法

delta = 0.001 / 2.0
threshold = 0.0001
alfa = 0.1

def func(x):
	return pos.distance(pos.hand_pos(x[0],x[1],x[2],x[3]),b)

#偏微分
def i_df(i,a):
	a_p = list(a)
	a_p[i] = a[i] + delta
	a_m = list(a)
	a_m[i] = a[i] - delta
	f_p = func(a_p)
	f_m = func(a_m)
	return (f_p - f_m) / delta

#微分
def df(a):
	return map(lambda (i,_): i_df(i,a) ,enumerate(a))

#aの更新
def next_a(a):
	return map(lambda (i,a_i): a[i] + alfa * df(a)[i], enumerate(a))

#main

a = [[0,0,0,0]]
b = pos.Pos(40,0,0)
while True:
	a.append(next_a(a[-1]))
	if abs(func(a[-1]) - func(a[-2])) < threshold:
		break
		
print(a[-1])

