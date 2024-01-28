from gle import is_equal, is_greater, is_less
from clean import clean
import sys

round_down = ("0", "1", "2", "3", "4")
round_up = ("5", "6", "7", "8", "9")



#Given a string number as a parameter, return its absolute value
def abv(n):
    try:
        n[0]
    except IndexError:
        print("Cannot get the absolute value of an empty string!")
        print("Terminating program")
        sys.exit(1)
    
    n = clean(n) #In place until calculate() is implemented
    
    if (is_equal("-", n[0])):
        return n.replace("-", "")
    else:
        return n



#Given a number string as a parameter, round it by up to 10 decimal digits
def round(n):
    pass