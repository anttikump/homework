import recordBatcher
import unittest
import recordBatcher
import random
import string
import sys

class TestDataBatcher(unittest.TestCase):

	def createArrayOfStrings(self, n, length):
		res = []
		for i in range(n):
			res.append(''.join(random.choice(string.ascii_lowercase) for x in range(length)))
		return res

		#self.flattened_array = [item for sublist in self.fullArray for item in sublist]

	def flattenArray(self, array):
		return [item for sublist in array for item in sublist]


	def test_simple(self):
		arr = self.createArrayOfStrings(5, 10)
		print(arr)
		output = recordBatcher.takeInput(arr)
		print(list(output))
		pass

	


if __name__ == "__main__":
	unittest.main()
