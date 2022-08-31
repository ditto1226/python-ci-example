import unittest

from main import hello

class MainTest(unittest.Testcase):
    def tset_hello(self):
        self.assertEqual(hello(), "hello World")

if __name__ == "__main__":
    unittest.main()