# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# # test_calculator.py
# import unittest
# from calculator import add, subtract, multiply, divide

# class TestCalculator(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual(add(3, 5), 8)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(0, 0), 0)

#     def test_subtract(self):
#         self.assertEqual(subtract(10, 5), 5)
#         self.assertEqual(subtract(0, 7), -7)
#         self.assertEqual(subtract(-3, -2), -1)

#     def test_multiply(self):
#         self.assertEqual(multiply(4, 5), 20)
#         self.assertEqual(multiply(0, 10), 0)
#         self.assertEqual(multiply(-3, 3), -9)

#     def test_divide(self):
#         self.assertEqual(divide(10, 2), 5)
#         self.assertEqual(divide(-9, 3), -3)
#         self.assertAlmostEqual(divide(7, 3), 2.3333, places=4)
        
#         with self.assertRaises(ValueError):
#             divide(10, 0)

# if __name__ == "__main__":
#     unittest.main()
