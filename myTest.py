import unittest
import waiter

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
        #self.assertEqual(waiter.PersonalInformation(),False)

    def test_PersonalInformation(self):
        self.assertRaises(ValueError,waiter.PersonalInformation())


if __name__ == '__main__':
    unittest.main()
