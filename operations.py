from gle import is_equal, is_greater, is_less
from clean import clean
import sys

def abv(n):
    try:
        n[0]
    except IndexError:
        print("Cannot get the absolute value of an empty string!")
        print("Terminating program")
        sys.exit(1)
    
    n = clean(n)
    
    if (is_equal("-", n[0])):
        return n.replace("-", "")
    else:
        return n



def round(n):
    pass
