################################################
## Machine Learning Algorithms Library
## By Dingnaam HK
## Started at 17/3/2025
################################################

### Library Importing ###
import numpy as np

### Main Program ###

def xy(*args):
    """
    This function is for user to input the data to be processed.
    Arguments:  x,y pairs in tuple form.
                Every tuple must contain exactly 2 elements.
                x and y in the tuple must be in either int or float type.
    Returns:    a list of tuples

    """
    vData = []  # vector of data
    for i, j in enumerate(args):
        vData.append(j)
        if type(j) is not tuple:
            # Check if every input elements are tuples.
            raise TypeError (f"Tuples are expected for argument of function xy(), but {type(i)} is given.")
        if len(j) != 2:
            # Check if every tuple contains exactly 2 elements.
            raise ValueError (f"Each tuple should contain exactly 2 elements, but {len(i)} is given.")
        if type(args[i][0]) is not int or type(args[i][0]) is not float:
            raise TypeError (f"Elements in tuples are expected to be either int or float, but {type(args[i][0])} is given.")
        if type(args[i][1]) is not int or type(args[i][1]) is not float:
            raise TypeError (f"Elements in tuples are expected to be either int or float, but {type(args[i][1])} is given.")
        
    return vData