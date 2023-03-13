import unittest

from student import Student

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #student instances now created at the class level 
        print('\n setupClass \n')

        cls.student1 = Student("Eddy","Wop",40000)
        cls.student2 = Student("Uhtred","Ragnarson", 47000)
    

    @classmethod
    def tearDownClass(cls):
        print('\n tearDownClass')


    def setUp(self):
        print("\n settupunit")


    def tearDown(self):
        print('teardownunit')


    def test_mail(self):
        print("test mail")
        self.assertEqual(self.student1.mail, "Eddy.Wop@xyz.com")
        self.assertEqual(self.student2.mail, "Uhtred.Ragnarson@xyz.com")


    def test_fullname(self):

        print("test full name")

        self.assertEqual(self.student1.fullname, "Eddy Wop")
        self.assertEqual(self.student2.fullname, "Uhtred Ragnarson")


    def test_applyinghike(self):

        print("test stipend hike")

        self.assertEqual(self.student1.apply_hike(), 42000)
        self.assertEqual(self.student2.apply_hike(), 49350)

if __name__ == "__main__":
    unittest.main()


              