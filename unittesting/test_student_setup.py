import unittest

from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass START\n")

    @classmethod
    def tearDownClass(cls):
        print("\n tearDownClass COMPLETE")


    def setUp(self):
        print("\n setting up")
        self.student1 = Student("Eddy","Wop",40000)
        self.student2 = Student("Uhtred","Ragnarson", 47000)

    def tearDown(self):
        print('running tear down method')
        
        

    def test_mail(self):
        print("testing mail")
        self.assertEqual(self.student1.mail, "Eddy.Wop@xyz.com")
        self.assertEqual(self.student2.mail, "Uhtred.Ragnarson@xyz.com")

        self.student1.first = "Magne"
        self.student2.first = "Isolde"

        self.assertEqual(self.student1.mail, "Magne.Wop@xyz.com")
        self.assertEqual(self.student2.mail, "Isolde.Ragnarson@xyz.com")

    def test_fullname(self):
        
        print("testing name")
        self.assertEqual(self.student1.fullname, "Eddy Wop")
        self.assertEqual(self.student2.fullname, "Uhtred Ragnarson")

    def test_applyhike(self):
        print("testing operation")
        self.assertEqual(self.student1.apply_hike(), 42000)

        self.assertEqual(self.student2.apply_hike(), 49350)



if __name__ == "__main__":
    unittest.main()