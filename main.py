#!/usr/bin/python
#-*- coding: utf-8 -*-
import math

#calculate hand position acording to arm rotation

# calc right arm
# set arm root as x = 0, y = 0, z = 0
# x beside horizontal leaving +
# y forward horizontal forward + 
# z vertical upper +
def elbow_pos(l1,w1,t1):
	#1 only wing w1
	# 0 - direct to ground
	# 90 - direct to horizontal

	#2 only rotate t1
	# 0 - direct to ground
	# 90 - direct to forward

	x = l1 * math.sin(w1)
	y = l1 * math.sin(t1)
	z = l1 * (math.cos(w1) - 1) * ( -1 * math.cos(t1))

	return [x,y,z]

def hand_pos(l1,w1,t1,l2,w2,t2)
	#1 calc w1 0 t1 0
	# w2
	# 0 - direct to ground
	# 90 - direct to horizontal
	# t2
	# 0 - direct to myself
	# 90 - direct to forward
	z = l2 * (math.cos(w2) - 1)
	y = l2 * math.sin(t2) * math.sin(w2)
	x = l2 * math.sin(w2) * (-1 * math.cos(t2))

	#1 calc w1  t1 
	# w2
	# 0 - along to l1
	# 90 - right angle to l1
	# t2
	# 0 - direct to myself
	# 90 - direct to forward
	l1_l = elbow_pos(w1,t1)
	l1_x = l1_l[0]
	l1_y = l1_l[1]
	l1_z = l1_l[2]
	
	z = l1_z + l2 * (math.cos(w1-w2) -1) * ( -1 * math.cos(t1))
	y = l1_y + l2 * math.sin(w2-w1) * math.sin(t2) * math.sin(t1)
	x = l1_x + l2 * math.sin(w1-w2) * ( -1 * math.cos(t2))

	return [x,y,z]

def into_radian(x):
	return math.pi * x / 180.0 

#print(hand_pos(1,0,0,0,0,0))
#print(hand_pos(2,0,0,0,0,0))
#print(hand_pos(1,90,0,0,0,0))


