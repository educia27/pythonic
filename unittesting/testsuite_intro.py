import unittest

class TestString(unittest.TestCase):
    def runTest(self):
        self.assertEqual("b"*4, "bbbb")

class TestUpper(unittest.TestCase):
    def runTest(self):
        self.assertEqual('yezzir'.upper(), "YEZZIR")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestString("runTest"))
    suite.addTest(TestUpper("runTest"))
    return suite

if __name__== "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())