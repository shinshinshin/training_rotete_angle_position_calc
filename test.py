#!/usr/bin/python
#-*- coding: utf-8 -*-

import unittest

import pos

# x beside horizontal leaving +
# y forward horizontal forward + 
# z vertical upper +
r_2 = 1.41421356
r_3 = 1.7320508
class Test_Hand_Pos(unittest.TestCase):
	def setup(self):
		pass

	def test_elbow_pos_1(self):
		expected = pos.Pos(0,0,-20)
		actual = pos.elbow_pos(0,0)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_elbow_pos_2(self):
		expected = pos.Pos(0,20,0)
		w1 = pos.into_radian(0)
		t1 = pos.into_radian(90)
		actual = pos.elbow_pos(w1,t1)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_elbow_pos_3(self):
		expected = pos.Pos(20,0,0)
		w1 = pos.into_radian(90)
		t1 = pos.into_radian(0)
		actual = pos.elbow_pos(w1,t1)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_elbow_pos_4(self):
		expected = pos.Pos(r_2/2.0*20,0,-r_2/2.0*20)
		w1 = pos.into_radian(45)
		t1 = pos.into_radian(0)
		actual = pos.elbow_pos(w1,t1)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_elbow_pos_5(self):
		expected = pos.Pos(0,r_2/2.0*20,-1 * r_2/2.0*20)
		w1 = pos.into_radian(0)
		t1 = pos.into_radian(45)
		actual = pos.elbow_pos(w1,t1)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_elbow_pos_6(self):
		expected = pos.Pos(1.0/2.0*20,0,-1 *r_3/2.0*20)
		w1 = pos.into_radian(30)
		t1 = pos.into_radian(0)
		actual = pos.elbow_pos(w1,t1)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_elbow_pos_7(self):
		expected = pos.Pos(1.0/2.0*20,r_3/2.0*r_3/2.0*20,-1 * r_3/2.0*20/2.0)
		w1 = pos.into_radian(30)
		t1 = pos.into_radian(60)
		actual = pos.elbow_pos(w1,t1)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

# x beside horizontal leaving +
# y forward horizontal forward + 
# z vertical upper +
	def test_only_hand_pos_1(self):
		w2 = pos.into_radian(0)
		t2 = pos.into_radian(0)
		expected = pos.Pos(0,0,-20)
		actual = pos.only_hand_pos(w2,t2)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_only_hand_pos_2(self):
		w2 = pos.into_radian(90)
		t2 = pos.into_radian(90)
		expected = pos.Pos(0,20,0)
		actual = pos.only_hand_pos(w2,t2)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_only_hand_pos_3(self):
		w2 = pos.into_radian(90)
		t2 = pos.into_radian(0)
		expected = pos.Pos(-20,0,0)
		actual = pos.only_hand_pos(w2,t2)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_only_hand_pos_4(self):
		w2 = pos.into_radian(30)
		t2 = pos.into_radian(0)
		expected = pos.Pos(-1.0/2.0* 20,0,-r_3/2.0*20.0)
		actual = pos.only_hand_pos(w2,t2)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_hand_pos_1(self):
		expected = pos.Pos(0,0,-40)
		actual = pos.hand_pos(0,0,0,0)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_hand_pos_2(self):
		expected = pos.Pos(0,20,-20)
		actual = pos.hand_pos(0,0,90,90)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_hand_pos_3(self):
		expected = pos.Pos(40,0,0)
		actual = pos.hand_pos(90,0,0,0)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_hand_pos_4(self):
		expected = pos.Pos(20,0,-20)
		actual = pos.hand_pos(0,0,90,180)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_hand_pos_5(self):
		expected = pos.Pos(20,20,0)
		actual = pos.hand_pos(90,0,90,90)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	"""
	def test_hand_pos_6(self):
		expected = pos.Pos(1.0/2.0*40,0,-r_3/2.0*40)
		actual = pos.hand_pos(0,30,0,0)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)

	def test_hand_pos_7(self):
		expected = pos.Pos(1.0/2.0*40,r_3/2.0*r_3/2.0*40,-r_3/2.0*40/2.0)
		actual = pos.hand_pos(30,60,0,0)
		self.assertEqual(expected.x, actual.x)
		self.assertEqual(expected.y, actual.y)
		self.assertEqual(expected.z, actual.z)
	"""


if __name__ == "__main__":
	    unittest.main()
