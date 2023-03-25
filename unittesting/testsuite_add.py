import unittest


class TestMultiply(unittest.TestCase):
    def runTest(self):
        self.assertEqual((5*3),16)

class TestSubtract(unittest.TestCase):
    def runTest(self):
        self.assertEqual((12-6),6)

class TestAdd(unittest.TestCase):
    def runTest(self):
        self.assertEqual((90+7), 97)

class SimpleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,1)
        
    @unittest.skip("temporarily skips test")
    def test2(self):
        self.assertEqual(2,2)

    def test3(self):
        self.assertEqual(3,3)

    def test4(self):
        self.assertEqual(4,4)

if __name__=="__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(TestMultiply())
    # suite.addTests([TestSubtract(), TestAdd()])
    suite = unittest.makeSuite(SimpleTest,'test')
    suite.addTests([TestSubtract(), TestAdd(), TestMultiply()])
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print("errors: ", result.errors)
    print('\nfailures: ', result.failures)
    print('\nskipped tests: ', result.skipped)
    print('\nNo. of tests:', result.testsRun)
    print("\nwas it a successful test? ,", result.wasSuccessful())