import unittest
from src.main import add_two_integers

class SimpleTest(unittest.TestCase):

	def test(self):
		x = 10
		y = 2
		expected = 10 + 2
		result = add_two_integers(x, y)
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()

