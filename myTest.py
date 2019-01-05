import unittest
import checking_functions

class functionTest(unittest.TestCase):
    def test_ReadDict(self):
        self.assertEqual(checking_functions.ReadDict('Matan_La', 1234), {3:12345678})
        self.assertRaises(ValueError,checking_functions.ReadDict,1,1)

    def test_ChangeWorkSchedule(self):
        self.assertEqual(checking_functions.ChangeWorkSchedule(),{'FirstName': 'Matan', 'LastName': 'Lazimi',
                             'ID': 123456789, 'Appl': 'I want to replace'})
    def test_PersonalInformation(self):
        self.assertEqual(checking_functions.PersonalInformation1(),{'FirstName': 'Matan', 'LastName': 'Lazimi',
                                                                    'ID': 123456789,'PhoneNumber': '052-3256626',
                                                                    'EmailAddress': 'Matan@gmail.com'})
        self.assertRaises(ValueError,checking_functions.PersonalInformation2)
    def test_insert_days_to_work(self):
        self.assertEqual(checking_functions.Insert_days_to_work(),[1,6])
        self.assertRaises(ValueError,checking_functions.Insert_days_to_work)
    def test_feedback(self):
        self.assertEqual(checking_functions.feedback1(),{'22/12/2018':'Good Job'})
        self.assertRaises(ValueError,checking_functions.feedback2)
    def test_Dismis_Work_Day(self):
        self.assertRaises(ValueError,checking_functions.Dismis_Work_Day,9)
        self.assertEqual(checking_functions.Dismis_Work_Day(2),2)
    def test_request_manpower(self):
        self.assertRaises(ValueError,checking_functions.request_manpower,-8)
        self.assertEqual(checking_functions.request_manpower(25),{"22/11/2019":25})
    def teat_request_from_manager(self):
        self.assertEqual(checking_functions.request_from_manager("Fire me"),"Fire me")
        self.assertRaises(ValueError,checking_functions.request_from_manager,123)
    def test_show_details_of_waiters(self):
        self.assertEqual(checking_functions.show_details_of_waiters([]),False)
        self.assertEqual(checking_functions.show_details_of_waiters(['Matan Lazimi, 123456789',
                                                             'Moshe Tagaya, 123123123']),True)
    def test_insert_event1(self):
        self.assertEqual(checking_functions.insert_event(10),True)
        self.assertEqual(checking_functions.insert_event("123"), False)
    def test_insert_event2(self):
        self.assertRaises(ValueError,checking_functions.insert_event,102)
        self.assertEqual(checking_functions.insert_event("error input"), False)
        self.assertEqual(checking_functions.insert_event(76), True)

if __name__ == '__main__':
   unittest.main()
