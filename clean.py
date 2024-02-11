import sys

equals = ("0 = 0", "1 = 1", "2 = 2", "3 = 3", "4 = 4", "5 = 5", "6 = 6", 
          "7 = 7", "8 = 8", "9 = 9", "+ = +", "- = -", "* = *", "/ = /", 
          "^ = ^", "( = (", ") = )", ". = .", "= = =", "> = >", "< = <", 
          "c = c")

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
symbols = ("+", "-", "*", "/", "^", "(", ")", "|", ".", "=", ">", "<", 
           "c", "C", "X")


#Helper function to make it easier to check number parameters by having every
#number look nice (i.e. no leading 0 for integers, a leading 0 for floats 
#between 1 and -1, no trailing 0 in floats, turning floats into ints if the
#decimal digits are all 0)
def clean(n):
    try:
        n[0]
    except IndexError:
        print("Won't be able to do any calculations with an empty string!")
        print("Terminating program")
        sys.exit(1)
    
    #Determine if parameter is a standalone symbol or space
    if(n[0] in symbols and str(len(n)) + " = 1" in equals):
        return n
    
    #Check if n is neither an int nor a float; if so, return n without change
    has_deci = False
    if (n[0] + " = -" not in equals and n[0] + " = ." not in equals and 
        n[0] in symbols):
        return n
    else:
        if (n[0] + " = ." in equals):
            has_deci = True        
    
    for i in range(1, len(n)):
        if (n[i] in symbols):
            if (n[i] + " = ." in equals and not has_deci):
                has_deci = True
            elif (n[i] + " = ." in equals and has_deci):
                return n
            else:
                return n                
    
    #Check if float
    if ("." in n):
        deci_at = 0
        #Look for the decimal
        for i in range(len(n)):
            if (n[i] + " = ." in equals):
                deci_at = i
        #Check if the digits after the decimal are not all 0
        for i in range(deci_at, len(n)):
            if (n[i] + " = ." in equals):
                continue
            elif (not n[i] + " = 0" in equals):
                return str(float(n))
        #
        return str(int(float(n)))
    #Check if int or a mix
    else:
        return str(int(n))
