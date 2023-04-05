import unittest
"""
Module practising for unittest. generated by chatgpt
"""

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test class for different test scenarios
    """
    
    def test_empty_list(self):
        """test_empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_positive_numbers(self):
        """test positive numbers"""
        self.assertEqual(max_integer([11, 12, 13, 14]), 14)
    
    def test_negative_numbers(self):
        """test negative numbers"""
        self.assertEqual(max_integer([-11, -2, -33, -14]), -2)
    
    def test_mixed_numbers(self):
        """test mixed numbers"""
        self.assertEqual(max_integer([-10, -2, 0, 44]), 44)
    
    def test_duplicate_numbers(self):
        """test duplicate numbers"""
        self.assertEqual(max_integer([1, 12, 12, 13]), 13)
    
    def test_single_number(self):
        """test single numbers"""
        self.assertEqual(max_integer([23]), 23)
    
            
if __name__ == '__main__':
    unittest.main()
