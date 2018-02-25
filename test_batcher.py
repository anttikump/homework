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


	def test_order(self):
		#test with only small records, no filtering needed
		testArray = self.createArrayOfStrings(500,5)
		output = recordBatcher.takeInput(testArray)

		self.assertEqual(self.flattenArray(output), testArray)

		#test with bigger records in bewtween
		firstOfSmalls = self.createArrayOfStrings(499,5)
		largeRecords = self.createArrayOfStrings(2,1000000)
		secondOfSmalls = self.createArrayOfStrings(10,5)

		testArray = firstOfSmalls + largeRecords + secondOfSmalls
		output = recordBatcher.takeInput(testArray)

		self.assertEqual(self.flattenArray(output), firstOfSmalls + secondOfSmalls)


	def test_batchSizes(self):
		testArray = self.createArrayOfStrings(10000,5)
		output = recordBatcher.takeInput(testArray)

		#test that there is a correct number of batches
		self.assertEqual(len(output), 20)
		testArray+= self.createArrayOfStrings(5,1000000)
		self.assertEqual(len(output), 20)

		#test that no batch is bigger than 5MB, and no record inside them is bigger than 1MB
		for batch in output:
			self.assertTrue(len(batch) <= 500)
			self.assertTrue(sys.getsizeof(batch) <= 5000000)
			for record in batch:
				self.assertTrue(sys.getsizeof(record) <= 1000000)
		

if __name__ == "__main__":
	unittest.main()
