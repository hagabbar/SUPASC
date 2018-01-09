# Code to do various statistical calculations
# Author: Hunter Gabbard
# University of Glasgow

import numpy as np

class Dataset:
    """
    This object will store a dataset and then do simple
    statistical calculations on it
    """

    def __init__(self, data):
        """
        Construct the dataset object
        """
        self.data = data

    def mean(self):
        """
        Calculate the mean of some data
        """
        
        return sum(self.data) / len(self.data)
  
    def std_calc(self):
        """
        Calculate the standard deviation
        """
        
        return np.sqrt(np.var(self.data))


# list of variables
dataset = [1,2,3,4,5]

# store test_data
test_data = Dataset(dataset)

# calculate the standard deviation
print( test_data.std_calc() )

 
