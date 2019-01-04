import manager
import unittest

class waiter(unittest.TestCase):
    def test_ReadDict(self):
        self.assertEqual(manager('Matan_La',1234),True)

if __name__ == '__main__':
   unittest.main()
