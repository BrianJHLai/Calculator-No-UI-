from gle import is_equal, is_greater, is_less
from clean import clean
from operations import abv
from add import add
from sub import sub
import sys

#Given 2 strings representing numbers as parameters, return the quotient of the
#first parameter divided by the second
def div(n1, n2):
    try:
        n1[0]
        n2[0]
    except IndexError:
        print("Cannot perform division with only 1 or less numbers!")
        print("Terminating program")
        sys.exit(1)
    
    #Check if n2, the divisor, is 0
    if (is_equal("0", n2)):
        print("Cannot divide by 0!")
        print("Terminating program")
        sys.exit(1)
        
    #If n1 or n2 is negative
    if (is_equal("-", n1[0]) or is_equal("-", n2[0])):
        return nega_div(n1, n2)
    #If n1 or n2 is a decimal number
    elif (not is_equal("-1", str(n1.find("."))) or 
          not is_equal("-1", str(n2.find(".")))):
        return deci_div(n1, n2)
    
    #If n1 and n2 are both positive whole numbers
    q = []
    dividend = "" 
    
    #Divide digits
    for i in range(len(n1)):
        dividend = dividend + n1[i]
        q_digit = "0"
        #Continously subtract the divisor from the dividend until the dividend
        #is less than the divisor. Add 1 to q_digit for every subtraction
        while (is_greater(dividend, n2) or is_equal(dividend, n2)):
            q_digit = add(q_digit, "1")
            dividend = sub(dividend, n2)
        q.append(q_digit)
            
    #If n1 is not fully divisble by n2, append a decimal to q and 0s
    if (not is_equal("0", dividend)):
        q.append(".")
        cut_off = "0"
        #Divide until either the dividend is 0 or the quotient has 10 digits
        #after the decimal
        while (not is_equal("0", dividend) and not is_equal(cut_off, "10")):
            dividend = dividend + "0"
            q_digit = "0"
            while (is_greater(dividend, n2) or is_equal(dividend, n2)):
                q_digit = add(q_digit, "1")
                dividend = sub(dividend, n2)
            q.append(q_digit)
            cut_off = add(cut_off, "1")
        
    return clean("".join(q))



#
def nega_div(n1, n2):
    pass



#
def deci_div(n1, n2):
    pass
