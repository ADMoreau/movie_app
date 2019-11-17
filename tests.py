import unittest

import app


class MyTestCase(unittest.TestCase):
    def test_something(self):

        a = app.searchIMDB('ladder', movie=True)
        b = app.searchIMDB('ladder', movie=False)

        self.assertIsNotNone(a)
        self.assertIsNotNone(b)
        self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
