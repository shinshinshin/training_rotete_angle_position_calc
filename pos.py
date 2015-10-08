#!/usr/bin/python
#-*- coding: utf-8 -*-
import math

class Pos:
	def __init__(self, x = 0.0, y = 0.0, z = 0.0):
		self.x = round(x,9)
		self.y = round(y,9)
		self.z = round(z,9)
	def pos_print(self):
		print("x:" + self.x +",y:" + self.y + ",z:" + self.z)

def distance(pos1,pos2):
	return math.sqrt(math.pow(pos1.x - pos2.x,2) + math.pow(pos1.y - pos2.y,2) + math.pow(pos1.z - pos2.z,2))

#calculate hand position acording to arm rotation

# calc right arm
# set arm root as x = 0, y = 0, z = 0
# x beside horizontal leaving +
# y forward horizontal forward + 
# z vertical upper +
def elbow_pos(w1,t1):
	l1 = 20
	#1 only wing w1
	# 0 - direct to ground
	# 90 - direct to horizontal

	#2 only rotate t1
	# 0 - direct to ground
	# 90 - direct to forward

	x = l1 * math.sin(w1)
	y = l1 * math.sin(t1) * math.cos(w1)
	z = l1 * (math.cos(w1)) * ( -1 * math.cos(t1))

	return Pos(x,y,z)

def hand_pos(w1,t1,w2,t2):
	l2 = 20
	w1 = into_radian(w1)
	t1 = into_radian(t1)
	w2 = into_radian(w2)
	t2 = into_radian(t2)
	#1 calc w1 0 t1 0
	# w2
	# 0 - direct to ground
	# 90 - direct to horizontal
	# t2
	# 0 - direct to myself
	# 90 - direct to forward

	#1 calc w1  t1 
	# w2
	# 0 - along to l1
	# 90 - right angle to l1
	# t2
	# 0 - direct to myself
	# 90 - direct to forward
	l1_p = elbow_pos(w1,t1)
	
	l2_p = only_hand_pos(w2,t2)

	x = l1_p.x + l2_p.x * math.cos(w1) + l2_p.z * -1 * math.sin(w1)
	y = l1_p.y + l2_p.y * math.cos(t1) + l2_p.z * math.sin(t1) * math.cos(w1)
	z = l1_p.z + l2_p.z * math.cos(w1) * math.cos(t1)

	return Pos(x,y,z)

def only_hand_pos(w2,t2):
	l2 = 20
	x = l2 * math.sin(-w2) * math.cos(t2)
	y = l2 * math.sin(w2) * math.sin(t2)
	z = l2 * math.cos(-w2) * -math.cos(t2)
	return Pos(x,y,z)

def into_radian(x):
	return math.pi * float(x) / 180.0 



