import unittest

def divide(x, y):
    if y == 0:
        raise ValueError("ゼロで割ることはできません")
    return x / y

class TestDivideFunction(unittest.TestCase):

# 1の回答箇所
    def test_divide_normal(self):
        self.assertEqual(divide(6, 3), 2)

# 2の回答箇所
    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()

