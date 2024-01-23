from gle import is_equal, is_greater, is_less
from clean import clean
from operations import abv
import sys

#Subtraction Tables
sub_diff = (("0", "9", "8", "7", "6", "5", "4", "3", "2", "1"),
            ("1", "0", "9", "8", "7", "6", "5", "4", "3", "2"),
            ("2", "1", "0", "9", "8", "7", "6", "5", "4", "3"),
            ("3", "2", "1", "0", "9", "8", "7", "6", "5", "4"),
            ("4", "3", "2", "1", "0", "9", "8", "7", "6", "5"),
            ("5", "4", "3", "2", "1", "0", "9", "8", "7", "6"),
            ("6", "5", "4", "3", "2", "1", "0", "9", "8", "7"),
            ("7", "6", "5", "4", "3", "2", "1", "0", "9", "8"),
            ("8", "7", "6", "5", "4", "3", "2", "1", "0", "9"),
            ("9", "8", "7", "6", "5", "4", "3", "2", "1", "0")
            )

sub_diff_neg = (()
                )



#Takes 2 strings representing numbers as parameters and return d, the difference
#of the 2 strings
def sub(n1, n2):
    try:
        sub_diff[int(n1[0])][int(n2[0])]
    except IndexError:
        print("Cannot perform subtraction with only 1 or less numbers!")
        print("Terminating program")
        sys.exit(1)    
    
    n1 = clean(n1)#
    n2 = clean(n2)#
    
    #If n1 or n2 is negative
    if (is_equal("-", n1[0]) or is_equal("-", n2[0])):
        return nega_sub(n1, n2)
    #If n1 or n2 is a decimal number
    elif (not is_equal("-1", str(n1.find("."))) or 
          not is_equal("-1", str(n2.find(".")))):
        return deci_sub(n1, n2)
    
    #If n1 and n2 are both positive whole numbers
    d = ""
    carry_over = False
    length = ""
    
    #If n1 is less than n2, then subtract n1 from n2 instead, and add a negative
    #sign to the difference at the end
    
    if (is_less(n1, n2)):
        is_neg = True
        n1_char = list(n2)
        n2_char = list(n1)
    else:
        is_neg = False
        n1_char = list(n1)
        n2_char = list(n2)        
    
    #Find the shorter length
    if (is_greater(str(len(n1)), str(len(n2)))):
        length = str(len(n2))
    else:
        length = str(len(n1))
        
    #Subtract digits (Going from right to left)
    r = build_diff(n1_char, n2_char, 0, int(length), carry_over)
    carry_over = r.pop()
    d = "".join(r) + d    
    
    #n1 and n2 had an equal number of digits
    if (is_equal(str(len(n1)), str(len(n2)))):
        if (is_neg):
            d = "-" + d
        return clean(d)
    #n1 has more digits than n2, use the remaining digits to finish making d
    elif (is_greater(str(len(n1)), str(len(n2)))):
        r = build_diff(n1_char, n2_char, int(length), len(n1), carry_over)
        r.pop()
        d = "".join(r) + d         
        return clean(d)
    #n2 has more digits than n1, use the remaining digits to finish making d
    else:
        r = build_diff(n1_char, n2_char, int(length), len(n2), carry_over)
        r.pop()
        d = "".join(r) + d      
        if (is_neg):
            d = "-" + d        
        return clean(d)



#
def nega_sub(n1, n2):
    pass



#
def deci_sub(n1, n2):
    pass



#Helper function for sub(), contains loop for making the difference
def build_diff(n1c, n2c, l1, l2, co):
    d = []
    
    for i in range(l1, l2):
        if (is_equal("0", str(len(n1c)))):
            next_digit = n2c[-1]
        elif (is_equal("0", str(len(n2c)))):
            next_digit = n1c[-1]
        else:
            next_digit = sub_diff[int(n1c[-1])][int(n2c[-1])]
           
        if (co):
            next_digit = sub_diff[int(next_digit)][1]
            #If subtracting 1 from next_digit doesn't result in 9, no carry over
            if (not is_equal(next_digit, "9")):
                co = False
        #
        if (not is_equal(str(len(n1c)), "0") and 
            not is_equal(str(len(n2c)), "0")):
            if (is_less(n1c[-1], n2c[-1])):
                co = True
        if (not is_equal(str(len(n1c)), "0")):
            n1c.pop()
        if (not is_equal(str(len(n2c)), "0")):
            n2c.pop()
        d.insert(0, next_digit)
    
    d.append(co)    
    return d
