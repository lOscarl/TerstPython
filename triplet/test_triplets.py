import unittest
from triplets import Triplets

class TestTriplets(unittest.TestCase):
      def setUp(self):
          self.triplets = Triplets( [1,1,1] , [1,1,1] )

# class TestReview(TestTriplets):

	
	#test value range 


class TestInit(TestTriplets):
	#test for array element number
	def test_entry_elements(self):
		#self.asserEqual(len(self.triplets.entry1) , 3)
		with self.assertRaises(Exception): Triplets( [1,1,1,1,1] , [1,1,1,1,1] )

	def test_empty_elements(self):
		with self.assertRaises(Exception): Triplets([] , [])

	def test_correct_elements(self):
		self.triplets = Triplets( [1,1,1] , [1,1,1] )
		self.assertEqual(len(self.triplets.entry1) , 3)
		self.assertEqual(len(self.triplets.entry2) , 3)


class TestLimit(TestTriplets):
	def test_non_zero_entry1(self):
		with self.assertRaises(Exception): Triplets( [0,1,1] , [1,1,1])
		with self.assertRaises(Exception): Triplets( [1,0,1] , [1,1,1])
		with self.assertRaises(Exception): Triplets( [1,1,0] , [1,1,1])
		'''
		for element in self.triplets.entry1:
			element_zero = 0
			with self.assertRaises(Exception): 
				Triplets( [1,1,1] , [1,1,1])
				self.triplets.entry1(element) = element_zero
		'''
	def test_non_zero_entry2(self):
		with self.assertRaises(Exception): Triplets( [1,1,1] , [0,1,1])
		with self.assertRaises(Exception): Triplets( [1,1,1] , [1,0,1])
		with self.assertRaises(Exception): Triplets( [1,1,1] , [1,1,0])

	def test_max_limit_entry1(self):
		with self.assertRaises(Exception): Triplets( [101,1,1] , [1,1,1])
		with self.assertRaises(Exception): Triplets( [1,101,1] , [1,1,1])
		with self.assertRaises(Exception): Triplets( [1,1,101] , [1,1,1])

	def test_max_limit_entry2(self):
		with self.assertRaises(Exception): Triplets( [1,1,1] , [101,1,1])
		with self.assertRaises(Exception): Triplets( [1,1,1] , [1,101,1])
		with self.assertRaises(Exception): Triplets( [1,1,1] , [1,1,101])

class TestComparation(TestTriplets):
	def test_point_for_Alice(self):
		self.triplets = Triplets( [2,1,1] , [1,1,1] )
		self.triplets.review()
		self.assertEqual(self.triplets.score[0], 1)
		self.triplets = Triplets( [1,2,1] , [1,1,1] )
		self.triplets.review()
		self.assertEqual(self.triplets.score[0], 1)
		self.triplets = Triplets( [1,1,2] , [1,1,1] )
		self.triplets.review()
		self.assertEqual(self.triplets.score[0], 1)
	
	def test_point_for_Bob(self):
		self.triplets = Triplets( [1,1,1] , [2,1,1] )
		self.triplets.review()
		self.assertEqual(self.triplets.score[1], 1)
		self.triplets = Triplets( [1,1,1] , [1,2,1] )
		self.triplets.review()
		self.assertEqual(self.triplets.score[1], 1)
		self.triplets = Triplets( [1,1,1] , [1,1,2] )
		self.triplets.review()
		self.assertEqual(self.triplets.score[1], 1)

	def test_no_point(self):
		self.triplets = Triplets( [1,1,1] , [1,1,1] )
		self.triplets.review()
		self.assertEqual(self.triplets.score[0], 0)
		self.assertEqual(self.triplets.score[1], 0)
