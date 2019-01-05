import unittest
import waiter

class MyTestCase(unittest.TestCase):
    def test_ReadDict(self):
        self.assertEqual(waiter.ReadDict('Matan_La', 1234), True)

    def test_PersonalInformation(self):
        self.assertRaises(ValueError,waiter.PersonalInformation(),None)
        pass

if __name__ == '__main__':
   unittest.main()
