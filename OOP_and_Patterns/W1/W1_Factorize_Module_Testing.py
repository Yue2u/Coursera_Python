import unittest


def factorize(x):
    ans = []
    if not isinstance(x, int):
        raise TypeError()
    if x < 0:
        raise ValueError()
    if x == 0 or x == 1:
        ans.append(x)
    d = 2
    while d * d <= x:
        if x % d == 0:
            ans.append(d)
            x //= d
        else:
            d += 1
    if x > 1:
        ans.append(x)
    return tuple(ans)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        with self.subTest(x=1.5):
            self.assertRaises(TypeError, factorize, 1.5)
        with self.subTest(x='string'):
            self.assertRaises(TypeError, factorize, 'string')

    def test_negative(self):
        with self.subTest(x=-1):
            self.assertRaises(ValueError, factorize, -1)
        with self.subTest(x=-10):
            self.assertRaises(ValueError, factorize, -10)
        with self.subTest(x=-100):
            self.assertRaises(ValueError, factorize, -100)

    def test_zero_and_one_cases(self):
        with self.subTest(x=0):
            self.assertEqual((0, ), factorize(0))
        with self.subTest(x=1):
            self.assertEqual((1, ), factorize(1))

    def test_simple_numbers(self):
        with self.subTest(x=3):
            self.assertEqual((3,), factorize(3))
        with self.subTest(x=13):
            self.assertEqual((13,), factorize(13))
        with self.subTest(x=29):
            self.assertEqual((29,), factorize(29))

    def test_two_simple_multipliers(self):
        with self.subTest(x=6):
            self.assertEqual((2, 3), factorize(6))
        with self.subTest(x=26):
            self.assertEqual((2, 13), factorize(26))
        with self.subTest(x=121):
            self.assertEqual((11, 11), factorize(121))

    def test_many_multipliers(self):
        with self.subTest(x=1001):
            self.assertEqual((7, 11, 13), factorize(1001))
        with self.subTest(x=9699690):
            self.assertEqual((2, 3, 5, 7, 11, 13, 17, 19), factorize(9699690))
