import unittest
import import_ipynb #install this if necessary
from assignment import Database
from assignment import Visualization
from unittest import mock
from bokeh.plotting import figure
import numpy as np


class TestDatabase(unittest.TestCase):

    def setUp(self):
 
        self.data1 = Database("train.csv","train") 
        self.data2 = Database("ideal.csv","ideal")

    def tearDown(self):#run the code after every test
        pass

    def test_csvfile(self):
        print("Tests are : test_csvname",end=", ")
           
        self.data1.csvfile = "john.csv"
        self.data2.csvfile = "jane.csv"

        self.assertEqual(self.data1.csvfile, "john.csv")
        self.assertEqual(self.data2.csvfile, "jane.csv")  
    
    def test_tablename(self):
        print("test_tablename",end=", ")
           
        self.data1.tablename = "xavi"
        self.data2.tablename = "iniesta"

        self.assertEqual(self.data1.tablename, "xavi")
        self.assertEqual(self.data2.tablename, "iniesta")  



class TestVisual(unittest.TestCase):

    def test_visualization(self):
        print("test_visualization",end=" ")
        x = np.arange(1,10,0.1)
        y = np.arange(11,20,0.1)
        model = Visualization(x,y,4,"title")
        plot = model.train()
        self.assertEqual(str(type(plot)),"<class 'bokeh.plotting.figure.Figure'>")

if __name__=="__main__":
    unittest.main()