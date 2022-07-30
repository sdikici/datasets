import unittest
import import_ipynb #install this if necessary
from assignment import Database


class TestAssignment(unittest.TestCase):

    def setUp(self): #run the code before every test
    #we can create the employees here and remove from the ones below
    # dont forget to add self. , dont use it if no setup
        print("\n")
        print("setUp", end=" ")   
        self.data1 = Database("train.csv","train") 
        self.data2 = Database("ideal.csv","ideal")

    def tearDown(self):#run the code after every test
        print("tearDown")
    
    def test_csvfile(self):
        print("test_csvname",end=" ")
           
        self.assertEqual(self.data1.csvfile, "train.csv")
        self.assertEqual(self.data2.csvfile, "ideal.csv")

        self.data1.csvfile = "john.csv"
        self.data2.csvfile = "jane.csv"

        self.assertEqual(self.data1.csvfile, "john.csv")
        self.assertEqual(self.data2.csvfile, "jane.csv")  
    
    def test_tablename(self):
        print("test_tablename",end=" ")
           
        self.assertEqual(self.data1.tablename, "train")
        self.assertEqual(self.data2.tablename, "ideal")

        self.data1.tablename = "ronaldo"
        self.data2.tablename = "messi"

        self.assertEqual(self.data1.tablename, "ronaldo")
        self.assertEqual(self.data2.tablename, "messi")  