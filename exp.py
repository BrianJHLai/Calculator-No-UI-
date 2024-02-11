from gle import is_equal, is_greater, is_less
from clean import clean
from operations import abv
from sub import sub
from mult import mult
import sys

#Given 2 strings representing numbers as parameters, return the value of the 
#first paramter raised to the power of the second parameter
def exp(n1, n2):
    try:
        n1[0]
        n2[0]
    except IndexError:
        print("Cannot calculate exponent with only 1 or less numbers!")
        print("Terminating program")
        sys.exit(1)
    
    #If n2, the power, is 0, return 1
    if (is_equal(n2, "0")):
        return "1"
    
    #If n1 or n2 is negative
    if (is_equal("-", n1[0]) or is_equal("-", n2[0])):
        return nega_exp(n1, n2)
    
    #If n1 and n2 are both positive whole numbers
    e = n1
    
    for i in range(int(sub(n2, "1"))):
        e = mult(e, n1)
        
    return e



#
def nega_exp():
    pass