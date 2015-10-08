#!/usr/bin/python
#-*- coding: utf-8 -*-

import unittest

import main

class Test_Hand_Pos(unittest.TestCase):
	def setup(self):
		self.hand_pos = main.hand_pos

	def test_hand_pos(self):
		expected = 1 
		actual = self.hand_pos(1,0,0,0,0,0)
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	    unittest.main()
