from clean import clean

#Comparison tuples
greater_than = ("9 > 8", "9 > 7", "9 > 6", "9 > 5", "9 > 4", "9 > 3", "9 > 2", 
                "9 > 1", "9 > 0", "8 > 7", "8 > 6", "8 > 5", "8 > 4", "8 > 3", 
                "8 > 2", "8 > 1", "8 > 0", "7 > 6", "7 > 5", "7 > 4", "7 > 3", 
                "7 > 2", "7 > 1", "7 > 0", "6 > 5", "6 > 4", "6 > 3", "6 > 2", 
                "6 > 1", "6 > 0", "5 > 4", "5 > 3", "5 > 2", "5 > 1", "5 > 0", 
                "4 > 3", "4 > 2", "4 > 1", "4 > 0", "3 > 2", "3 > 1", "3 > 0", 
                "2 > 1", "2 > 0", "1 > 0")

greater_than_neg = ("0 > 1", "0 > 2", "0 > 3", "0 > 4", "0 > 5", "0 > 6", 
                    "0 > 7", "0 > 8", "0 > 9", "1 > 2", "1 > 3", "1 > 4", 
                    "1 > 5", "1 > 6", "1 > 7", "1 > 8", "1 > 9", "2 > 3", 
                    "2 > 4", "2 > 5", "2 > 6", "2 > 7", "2 > 8", "2 > 9", 
                    "3 > 4", "3 > 5", "3 > 6", "3 > 7", "3 > 8", "3 > 9", 
                    "4 > 5", "4 > 6", "4 > 7", "4 > 8", "4 > 9", "5 > 6", 
                    "5 > 7", "5 > 8", "5 > 9", "6 > 7", "6 > 8", "6 > 9", 
                    "7 > 8", "7 > 9", "8 > 9")

less_than = ("0 < 1", "0 < 2", "0 < 3", "0 < 4", "0 < 5", "0 < 6", "0 < 7", 
             "0 < 8", "0 < 9", "1 < 2", "1 < 3", "1 < 4", "1 < 5", "1 < 6", 
             "1 < 7", "1 < 8", "1 < 9", "2 < 3", "2 < 4", "2 < 5", "2 < 6", 
             "2 < 7", "2 < 8", "2 < 9", "3 < 4", "3 < 5", "3 < 6", "3 < 7", 
             "3 < 8", "3 < 9", "4 < 5", "4 < 6", "4 < 7", "4 < 8", "4 < 9", 
             "5 < 6", "5 < 7", "5 < 8", "5 < 9", "6 < 7", "6 < 8", "6 < 9", 
             "7 < 8", "7 < 9", "8 < 9")

less_than_neg = ("9 < 8", "9 < 7", "9 < 6", "9 < 5", "9 < 4", "9 < 3", "9 < 2", 
                 "9 < 1", "9 < 0", "8 < 7", "8 < 6", "8 < 5", "8 < 4", "8 < 3", 
                 "8 < 2", "8 < 1", "8 < 0", "7 < 6", "7 < 5", "7 < 4", "7 < 3", 
                 "7 < 2", "7 < 1", "7 < 0", "6 < 5", "6 < 4", "6 < 3", "6 < 2", 
                 "6 < 1", "6 < 0", "5 < 4", "5 < 3", "5 < 2", "5 < 1", "5 < 0", 
                 "4 < 3", "4 < 2", "4 < 1", "4 < 0", "3 < 2", "3 < 1", "3 < 0", 
                 "2 < 1", "2 < 0", "1 < 0")

equals = ("0 = 0", "1 = 1", "2 = 2", "3 = 3", "4 = 4", "5 = 5", "6 = 6", 
          "7 = 7", "8 = 8", "9 = 9", "+ = +", "- = -", "* = *", "/ = /", 
          "^ = ^", "( = (", ") = )", ". = .", "= = =", "> = >", "< = <", 
          "c = c")

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
symbols = ("+", "-", "*", "/", "^", "(", ")", ".", "=", ">", "<", "c")


#Given two parameters, n1 and n2, return true if n1 is equal to n2
def is_equal(n1, n2):
    n1 = clean(n1)
    n2 = clean(n2)
    
    #Compare lengths; if length isn't equal, immediately return false
    if (str(len(n1)) + " = " + str(len(n2)) not in equals):
        return False
    #Length is equal, so next compare digits
    else:
        for i in range(len(n1)):
            if (n1[i] + " = " + n2[i] not in equals):
                return False
    
    #If reaching this point, all digits in n1 matched corresponding digits in n2
    return True
            


#Given two numbers, n1 and n2, return true if n1 is greater than n2
def is_greater(n1, n2):
    n1 = clean(n1)
    n2 = clean(n2)
    
    #Compare signs
    #n1 is positive/0, n2 is negative
    if (not is_equal(n1[0], "-") and is_equal(n2[0], "-")):
        return True
    #n1 is negative, n2 is positive/0
    elif (is_equal(n1[0], "-") and not is_equal(n2[0], "-")):
        return False
    
    #Compare the quantity of whole numbers (digits before the decimal)
    #For postive parameters, the one with more whole numbers is greater
    #For negative, the one with less whole numbers is greater
    n1_whole, n2_whole, start = 0, 0, 0
    is_neg = False
    
    if (is_equal("-", n1[0])):
        start += 1
        is_neg = True
        
    for i in range(start, len(n1)):
        if (is_equal(".", n1[i])):
            break
        n1_whole += 1
    for i in range(start, len(n2)):
        if (is_equal(".", n2[i])):
            break
        n2_whole += 1
        
    if (is_neg):
        if (str(n1_whole) + " > " + str(n2_whole) in greater_than_neg):
            return True
        elif (str(n1_whole) + " < " + str(n2_whole) in less_than_neg):
            return False
    else:
        if (str(n1_whole) + " > " + str(n2_whole) in greater_than):
            return True
        elif (str(n1_whole) + " < " + str(n2_whole) in less_than):
            return False        
        
    #Get the shorter length in preparation for digit comparison
    length = 0
    if (str(len(n1)) + " > " + str(len(n2)) in greater_than):
        length = len(n2)
    else:
        length = len(n1)

    #Compare digits
    if (is_neg):
        for i in range(1, length):
            if (n1[i] + " > " + n2[i] in greater_than_neg):
                return True
            elif (n1[i] + " < " + n2[i] in less_than_neg):
                return False            
    else:
        for i in range(length):
            if (n1[i] + " > " + n2[i] in greater_than):
                return True
            elif (n1[i] + " < " + n2[i] in less_than):
                return False      
        
    #After comparing digits, if n1 and n2 have the same length, they're equal
    if (is_equal(str(len(n1)), str(len(n2)))):
        return False
    #If n1 has more digits while both n1 and n2 are positive, then n1 is greater
    elif (not is_equal(str(len(n1)), str(length)) and not is_neg):
        return True
    #If n1 has less digits while both n1 and n2 are negative, then n1 is greater
    elif (is_equal(str(len(n1)), str(length)) and is_neg):
        return True
    #Either n2 has more digits while both are positive, or
    #n2 has less digits when both are negative, meaning n2 is greater than n1
    else:
        return False



#Given two numbers, n1 and n2, return true if n1 is less than n2
def is_less(n1, n2):
    n1 = clean(n1)
    n2 = clean(n2)
    
    #Compare signs
    #n1 is positive/0, n2 is negative
    if (not is_equal(n1[0], "-") and is_equal(n2[0], "-")):
        return False
    #n1 is negative, n2 is positive/0
    elif (is_equal(n1[0], "-") and not is_equal(n2[0], "-")):
        return True
    
    #Compare the quantity of whole numbers (digits before the decimal)
    #For postive parameters, the one with less whole numbers is lesser
    #For negative, the one with more whole numbers is lesser
    n1_whole, n2_whole, start = 0, 0, 0
    is_neg = False
    
    if (is_equal("-", n1[0])):
        start += 1
        is_neg = True
        
    for i in range(start, len(n1)):
        if (is_equal(".", n1[i])):
            break
        n1_whole += 1
    for i in range(start, len(n2)):
        if (is_equal(".", n2[i])):
            break
        n2_whole += 1
        
    if (is_neg):
        if (str(n1_whole) + " < " + str(n2_whole) in less_than_neg):
            return True
        elif (str(n1_whole) + " > " + str(n2_whole) in greater_than_neg):
            return False
    else:
        if (str(n1_whole) + " < " + str(n2_whole) in less_than):
            return True
        elif (str(n1_whole) + " > " + str(n2_whole) in greater_than):
            return False        
        
    #Get the shorter length in preparation for digit comparison
    length = 0
    if (str(len(n1)) + " > " + str(len(n2)) in greater_than):
        length = len(n2)
    else:
        length = len(n1)

    #Compare digits
    if (is_neg):
        for i in range(1, length):
            if (n1[i] + " < " + n2[i] in less_than_neg):
                return True
            elif (n1[i] + " > " + n2[i] in greater_than_neg):
                return False
    else:
        for i in range(length):
            if (n1[i] + " < " + n2[i] in less_than):
                return True
            if (n1[i] + " > " + n2[i] in greater_than):
                return False
        
    #After comparing digits, if n1 and n2 had the same length, they're equal
    if (is_equal(str(len(n1)), str(len(n2)))):
        return False
    #If n1 has less digits while both n1 and n2 are positive, then n1 is lesser
    elif (is_equal(str(len(n1)), str(length)) and not is_neg):
        return True
    #If n1 has more digits while both n1 and n2 are negative, then n1 is lesser
    elif (not is_equal(str(len(n1)), str(length)) and is_neg):
        return True
    #Either n2 has less digits while both are positive, or
    #n2 has more digits when both are negative, meaning n2 is lesser than n1
    else:
        return False

################################################################################
#Tests

print("Equals test 1:", is_equal("0", "0")) #True
print("Equals test 2:", is_equal("0000", "0")) #True
print("Equals test 3:", is_equal("10", "0")) #False
print("Equals test 4:", is_equal("1023456", "1023457")) #False
print("Equals test 5:", is_equal("-1023456", "-1023456")) #True
print("Equals test 6:", is_equal("-1023456", "1023456")) #False
print("Equals test 7:", is_equal("0.9", "0.9")) #True
print("Equals test 8:", is_equal(".9", "0.9")) #True
print("Equals test 9:", is_equal("0.9", "0.90")) #True
print("Equals test 10:", is_equal("-0.9", "-0.9")) #True
print("Equals test 11:", is_equal("0.9", "-0.9")) #False
print("Equals test 12:", is_equal("+", "+")) #True
print("Equals test 13:", is_equal("+", "-")) #False
print("Equals test 14:", is_equal("(", "(")) #True
print("Equals test 15:", is_equal("-9", "-")) #False
print("Equals test 16:", is_equal("()", "()")) #True
print("Equals test 16:", is_equal("c", "c")) #True

#print("Equals test Empty:", is_equal("-9", "")) #False

print("")

print("Greater test 1:", is_greater("2", "1")) #True
print("Greater test 2:", is_greater("1", "2")) #False
print("Greater test 3:", is_greater("2", "2")) #False
print("Greater test 4:", is_greater("-2", "-1")) #False
print("Greater test 5:", is_greater("-1", "-2")) #True
print("Greater test 6:", is_greater("-2", "-2")) #False
print("Greater test 7:", is_greater("2", "-2")) #True
print("Greater test 8:", is_greater("-2", "2")) #False
print("Greater test 9:", is_greater("2.9", "1")) #True
print("Greater test 10:", is_greater(".2", "1.")) #False
print("Greater test 11:", is_greater("500.0", "500")) #False
print("Greater test 12:", is_greater("500.9", "500")) #True
print("Greater test 13:", is_greater("5000", "500")) #True
print("Greater test 14:", is_greater("5009.", "500")) #True
print("Greater test 15:", is_greater("-500", "-500.0")) #False
print("Greater test 16:", is_greater("-500", "-500.9")) #True
print("Greater test 17:", is_greater("-500", "-5000")) #True
print("Greater test 18:", is_greater("-500", "-5009.")) #True
print("Greater test 19:", is_greater("5", "1000")) #False
print("Greater test 20:", is_greater("509.1", "509.0")) #True

print("")

print("Lesser test 1:", is_less("1", "2")) #True
print("Lesser test 2:", is_less("200", "100.")) #False
print("Lesser test 3:", is_less("-1", "2.")) #True
print("Lesser test 4:", is_less("100", "-2.")) #False
print("Lesser test 5:", is_less("-3.58", "-3.57")) #True
print("Lesser test 6:", is_less("101", "100")) #False
print("Lesser test 7:", is_less("100000", "100100")) #True
print("Lesser test 8:", is_less("100", "10000")) #True
print("Lesser test 9:", is_less("-10000", "-100")) #True
print("Lesser test 10:", is_less("100", "100")) #False