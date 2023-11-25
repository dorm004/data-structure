import unittest
from bracket_check import bracket_check


class MyTestCase(unittest.TestCase):
    def test_no_error(self):
        test_string = "[{(Hello)}]"
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, False)

    def test_no_error(self):
        test_string = "[{(Hello})]"
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)

    def test_no_error(self):
        test_string = "[{(Hello"
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)

    def test_no_error(self):
        test_string = "Hello)("
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)


if __name__ == '__main__':
    unittest.main()
