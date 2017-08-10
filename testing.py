import unittest

class TestStringMethods(unittest.TestCase):
    def test_lower(self):
        self.assertEqual('HELLO'.lower(), 'hello')

    def test_islower(self):
        self.assertTrue('hello'.islower())
        self.assertFalse('Hello'.islower())

    def test_splitter(self):
        test_string = 'hello world'
        self.assertEqual (test_string.split(' '), ['hello','world'])

if __name__ == '__main__':
    unittest.main()