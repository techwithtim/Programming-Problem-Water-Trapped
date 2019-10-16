import unittest
import time
from water_trapped import water
from Solution import solution
import random

class TestWaterTrapped(unittest.TestCase):
	"""
	Test cases for the water pipe problem
	"""

	def test_one(self):
		case = [4,2,4]
		ans = water(case)
    	self.assertEqual(ans, 2, f"{ans} Should be 2")

	def test_two(self):
		case = [5,2,5,5]
		ans = water(case)
		self.assertEqual(ans, 3, f"{ans} Should be 3")

	def test_three(self):
		case = [1,2]
		ans = water(case)
		self.assertEqual(ans, 0, f"{ans} Should be 0")

	def test_four(self):
		case = [10,5,5,5,7,8,7,9,2,2,3]
		ans = water(case)
		self.assertEqual(ans, 19, f"{ans} Should be 19")

	def test_five(self):
		case = [2,1,1,1,2,7,9,7,3,4,10,2,1,3]
		ans = water(case)
		self.assertEqual(ans, 19, f"{ans} Should be 19")

	def test_six(self):
		case = [2,2,2,2,2]
		ans = water(case)
		self.assertEqual(ans, 0, f"{ans} Should be 0")

	def test_random(self):
		"""
		50 random tests
		"""
		for _ in range(50):
			case = [random.randint(3,20) for _ in range(random.randint(4,100))]
			sol = solution(case)
			ans = water(case)
			self.assertEqual(ans, sol, f"{ans} Should be {sol}")


if __name__ == "__main__":
	unittest.main()