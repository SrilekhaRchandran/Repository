# https://www.youtube.com/watch?v=HKTyOUx9Wf4
import unittest

class LearnTest(unittest.TestCase):

    def setUp(self):
        print("SETUP Called....")
        #Arrange called here. Instead of calling 2 times in 2 functions
        self.a= 10
        self.b= 20

    def tearDown(self):
        print("TEARDOWN called....")


    def test_fn1(self):
        print("Function1 Called....")
        #Act
        result = self.a+self.b
        #Assert
        self.assertEqual(result, self.a+self.b)

    def test_fn2(self):
        print("Function2 Called....")
        #Act
        result = self.b+self.a
        #Assert
        self.assertEqual(result, self.b-self.a)


class LearnTest2(unittest.TestCase):
    def fn2(self):
        pass


if __name__ =="__main__":
    unittest.main()
