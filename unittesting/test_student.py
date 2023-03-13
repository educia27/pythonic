import unittest

from student import Student


class TestStudent(unittest.TestCase):

    def test_mail(self):
        student1 = Student("Eddy","Wop",5678)
        student2 = Student("Uhtred","Ragnarson", 4642)

        self.assertEqual(student1.mail, "Eddy.Wop@xyz.com")
        self.assertEqual(student2.mail, "Uhtred.Ragnarson@xyz.com")

        student1.first = "Magne"
        student2.first = "Isolde"

        self.assertEqual(student1.mail, "Magne.Wop@xyz.com")
        self.assertEqual(student2.mail, "Isolde.Ragnarson@xyz.com")

    def test_fullname(self):
        student3 = Student("Green", "Velvet", 78900)
        student4 = Student("Harry","Potter", 30000)

        self.assertEqual(student3.fullname, "Green Velvet")
        self.assertEqual(student4.fullname, "Harry Potter")

    def test_applyhike(self):
        student5 = Student("Mike", "Velvedere", 52000)
        student6 = Student("Emmanuel", "Scott", 35000)

        self.assertEqual(student5.apply_hike(), 54600)

        self.assertEqual(student6.apply_hike(), 36750)



if __name__ == "__main__":
    unittest.main()