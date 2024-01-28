from gle import is_equal, is_greater, is_less
from clean import clean
from operations import abv
import sys

#Addition Tables
add_sum = (("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"),
           ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), 
           ("2", "3", "4", "5", "6", "7", "8", "9", "10", "11"), 
           ("3", "4", "5", "6", "7", "8", "9", "10", "11", "12"), 
           ("4", "5", "6", "7", "8", "9", "10", "11", "12", "13"), 
           ("5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), 
           ("6", "7", "8", "9", "10", "11", "12", "13", "14", "15"), 
           ("7", "8", "9", "10", "11", "12", "13", "14", "15", "16"), 
           ("8", "9", "10", "11", "12", "13", "14", "15", "16", "17"), 
           ("9", "10", "11", "12", "13", "14", "15", "16", "17", "18")
           )

add_sum_neg = ((),
           (), 
           (), 
           (), 
           (), 
           (), 
           (), 
           (), 
           (), 
           ()
           )


#Takes 2 strings representing numbers as parameters and return s, the sum of the
#2 strings
def add(n1, n2):
    try:
        add_sum[int(n1[0])][int(n2[0])]
    except IndexError:
        print("Cannot perform addition with only 1 or less numbers!")
        print("Terminating program")
        sys.exit(1)
        
    n1 = clean(n1) #In place until calculate() is implemented
    n2 = clean(n2) #In place until calculate() is implemented
    
    #If n1 or n2 is negative
    if (is_equal("-", n1[0]) or is_equal("-", n2[0])):
        return nega_add(n1, n2)
    #If n1 or n2 is a decimal number
    elif (not is_equal("-1", str(n1.find("."))) or 
          not is_equal("-1", str(n2.find(".")))):
        return deci_add(n1, n2)

    #If n1 and n2 are both positive whole numbers
    s = ""
    n1_char = list(n1)
    n2_char = list(n2)
    carry_over = False
    length = ""
    
    #Find the shorter length
    if (is_greater(str(len(n1)), str(len(n2)))):
        length = str(len(n2))
    else:
        length = str(len(n1))
    
    #Add digits (Going from right to left)
    x = build_sum(n1_char, n2_char, 0, int(length), carry_over)
    carry_over = x.pop()
    s = "".join(x) + s

    #n1 and n2 had an equal number of digits
    if (is_equal(str(len(n1)), str(len(n2)))):
        return s
    #n1 has more digits than n2, use the remaining digits to finish making s
    elif (is_greater(str(len(n1)), str(len(n2)))):
        x = build_sum(n1_char, n2_char, int(length), len(n1), carry_over)
        x.pop()
        s = "".join(x) + s        
        return s
    #n2 has more digits than n1, use the remaining digits to finish making s
    else:
        x = build_sum(n1_char, n2_char, int(length), len(n2), carry_over)
        x.pop()
        s = "".join(x) + s          
        return s



#
def nega_add(n1, n2):
    n1 = clean(n1)
    n2 = clean(n2)
    pass



#
def deci_add(n1, n2):
    n1 = clean(n1)
    n2 = clean(n2)
    pass




#Helper function for add(), contains loop for making the sum
def build_sum(n1c, n2c, l1, l2, co):
    s = []
    
    for i in range(l1, l2):
        if (is_equal(str(len(n1c)), "0")):
            next_digit = n2c.pop()
        elif (is_equal(str(len(n2c)), "0")):
            next_digit = n1c.pop()
        else:
            next_digit = add_sum[int(n1c.pop())][int(n2c.pop())]
            
        #Add 1 to next_digit if carry_over is True
        if (co):
            next_digit = add(next_digit, "1")
            #Check if adding 1 to next_digit resulted in 10 or more
            if (is_equal("10", next_digit) or is_greater(next_digit, "10")):
                #Carry over if n1 or n2 still has more digits to add
                if (not is_equal("0", str(len(n1c))) 
                    or not is_equal("0", str(len(n2c)))):
                        next_digit = next_digit[-1]
            else:
                co = False
        
        #Check if next_digit is equal to 10 or more
        if (is_equal("10", next_digit) or is_greater(next_digit, "10")):
            #Carry over if n1 or n2 still has more digits to add
            if (not is_equal("0", str(len(n1c))) 
                or not is_equal("0", str(len(n2c)))):
                next_digit = next_digit[1]
                co = True
        
        s.insert(0, next_digit)
    
    s.append(co)    
    return s
