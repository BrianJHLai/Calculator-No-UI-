from gle import is_equal, is_greater, is_less
from clean import clean
from operations import abv
from add import add
import sys

#Multiplication Tables
mult_prod = (("0", "0", "0", "0", "0", "0", "0", "0", "0", "0"),
             ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"),
             ("0", "2", "4", "6", "8", "10", "12", "14", "16", "18"),
             ("0", "3", "6", "9", "12", "15", "18", "21", "24", "27"),
             ("0", "4", "8", "12", "16", "20", "24", "28", "32", "36"),
             ("0", "5", "10", "15", "20", "25", "30", "35", "40", "45"),
             ("0", "6", "12", "18", "24", "30", "36", "42", "48", "54"),
             ("0", "7", "14", "21", "28", "35", "42", "49", "56", "63"),
             ("0", "8", "16", "24", "32", "40", "48", "56", "64", "72"),
             ("0", "9", "18", "27", "36", "45", "54", "63", "72", "81")
             )

mult_prod_neg = ()



#Takes 2 strings representing numbers as parameters and return p, the product of
#the 2 strings
def mult(n1, n2):
    try:
        n1[0]
        n2[0]
    except IndexError:
        print("Cannot perform multiplication with only 1 or less numbers!")
        print("Terminating program")
        sys.exit(1)
        
    n1 = clean(n1) #In place until calculate() is implemented
    n2 = clean(n2) #In place until calculate() is implemented
    
    #If n1 or n2 is negative
    if (is_equal("-", n1[0]) or is_equal("-", n2[0])):
        return nega_mult(n1, n2)
    #If n1 or n2 is a decimal number
    elif (not is_equal("-1", str(n1.find("."))) or 
          not is_equal("-1", str(n2.find(".")))):
        return deci_mult(n1, n2)
    
    #If n1 and n2 are both positive whole numbers
    p = "0"
    n1_char = list(n1)
    n2_char = list(n2)
    sums = []
    s = []
    zeroes = ""

    #Multiply digits (Using long multiplication)
    for i in range(len(n2_char)):
        carry_over = "0"
        temp = n1_char.copy()
        
        for j in range(len(n1_char)):
            next_digit = mult_prod[int(temp.pop())][int(n2_char[-1])]
            
            #Add carry_over to next_digit if carry_over isn't 0
            if(not is_equal("0", carry_over)):
                next_digit = add(next_digit, carry_over)
                #Check if adding carry_over to next_digit resulted in 10 or more
                if (is_equal("10", next_digit) or is_greater(next_digit, "10")):
                    #Carry over if n1 (temp) still has digits to multiply by
                    if (not is_equal("0", str(len(temp)))):
                        carry_over = next_digit[0]
                        next_digit = next_digit[1]
                else:
                    carry_over = "0"
            
            #Check if next_digit is equal to 10 or more
            if (is_equal("10", next_digit) or is_greater(next_digit, "10")):
                #Carry over if n1 (temp) still has digits to multiply by
                if (not is_equal("0", str(len(temp)))):           
                    carry_over = next_digit[0]
                    next_digit = next_digit[1]
            
            s.insert(0, next_digit)
            
        n2_char.pop()
        sums.insert(0, "".join(s))
        s.clear()
        zeroes = zeroes + "0"
        s.insert(0, zeroes)
    
    #Add up the sums to get the product
    for i in range(len(sums)):
        p = add(p, sums[i])
    
    return p
    


#
def nega_mult():
    pass



#
def deci_mult():
    pass
