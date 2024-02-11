from gle import is_equal, is_greater, is_less
from clean import clean#
import sys

"""
The functions below will remove the whitespace from the user input, split the
input into pieces, which will be referred to as term.

(e.g. 1 + 2 has the terms [1, +, 2])

The terms will then be looked over for any formatting mistakes. If none are 
found, the terms will then be joined together to reconstruct the input, but
without whitespace. The whitespace-free input will then be returned to main()
"""

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
symbols = ("+", "-", "*", "/", "^", "(", ")", "|", ".", "=", ">", "<", 
           "c", "C", "X")

#Determine as to whether or not the user's input can be accepted as is
def input_parse(n):
    try:
        n[0]
    except IndexError:
        print("Cannot accept empty input!")
        print("Terminating program")
        sys.exit(1)
        
    #Strip whitespace, but don't immediately reassemble the input
    n_list = n.split()
    
    #Check if the user wishes to clear the calculator
    if ("c" in n_list or "C" in n_list):
        if (is_equal(str(len(n_list)), "1")):
            return n_list[0]
        else:
            print("Cannot accept input.")
            print("Clear is called by inputting c or C alone.")
            return "X"
    
    #If the user used an equals sign by itself, return it
    #Otherwise, make sure the user used an equals sign as the last element of 
    #the input, and that they used it at most once
    if ("=" in n_list):
        if (is_equal(str(len(n_list)), "1")):
            return n_list[0]
        elif (not is_equal(n_list[-1], "=")):
            print("Cannot accept input.")
            print("The equals sign must either be used alone or as the last "
                "character of an input.")                
            return "X"
        elif (not is_equal(str(len(n_list) - 1), str(n_list.index("=")))):
            print("Cannot accept input.")
            print("Only one equals sign may be used, and only by itself or as "
                "the last character of an input.")                
            return "X"
    
    #check_pairs
    if (not check_pairs(n_list)):
        return "X"
    
    #Check if the first element in n_list is an operation symbol or a number
    prev_is_num = False
    
    #If n_list[0] is an operator sign, then a theoretical term before it would
    #have been a numerical term, and vice versa
    if (is_equal(n_list[0], "+") or is_equal(n_list[0], "-") or 
        is_equal(n_list[0], "*") or is_equal(n_list[0], "-") or
        is_equal(n_list[0], "^")):
        prev_is_num = True
    else:
        prev_is_num = False
    
    #Iterate through the input 
    for i in range(len(n_list)):
        if (not check_char(n_list[i], prev_is_num)):
            return "X"
        
        #The terms of an input alternate between operator symbol and 
        #numerical term when formatted correctly
        prev_is_num = not prev_is_num
        
    #If there is no equals sign, then the last term must be a numerical one
    if (not is_equal(n_list[-1], "=") and not prev_is_num):
        print("Cannot accept input.")
        print("If the input has no equals sign, then the last term of the "
            "input must be a numerical one.")
        return "X"
    
    #Return the input after getting rid of the whitespace and reassembling it
    return " ".join(n_list)
        


#Check every character of the input to make sure that each one is in the
#accepted format
def check_char(n, prev):
    for i in range(len(n)):
        #Minus / Negative sign
        if (is_equal(n[i], "-")):
            #The term holding the minus sign must have a length of 1
            if (not is_equal(str(i), "0")):
                print("Cannot accept input.")
                print("An operation sign must be used by itself.")                
                return False              
            #For a negative sign, only a decimal or a number can follow it
            elif (is_less(str(i), str(len(n)-1)) and 
                  is_greater(str(len(n)), "1")):
                if (not is_equal(n[i+1], ".") and n[i+1] not in numbers):
                    print("Cannot accept input.")
                    print("A minus sign can only be used to denote a negative "
                    "number when in front of a decimal or a number.")                
                    return False
            #Minus cannot be the last character of a term with length 2 or more
            elif (is_equal(str(i), str(len(n)-1)) and 
                  is_greater(str(len(n)), "1")):
                print("Cannot accept input.")
                print("A minus sign cannot be the last character of a number.")                
                return False                
        
        #Decimal
        elif (is_equal(n[i], ".")):
            #Decimal cannot be used on its own
            if (is_equal(str(len(n)), "1")):
                print("Cannot accept input.")
                print("A decimal cannot be used by itself.")                
                return False
            #If the first character, it must be followed by a number
            elif (is_equal("0", str(i))):
                if (n[1] not in numbers):
                    print("Cannot accept input.")
                    print("A decimal must have at least one number next to "
                    "itself.")                
                    return False                    
            #If the last character, it must be preceded by a number
            elif (is_equal(str(len(n)-1), str(i))):
                if (n[i-1] not in numbers):
                    print("Cannot accept input.")
                    print("A decimal must have at least one number next to "
                    "itself.")                
                    return False                    
            #If neither first nor last, it must be followed by a number, and
            #preceded by another number or certain characters {-, (, |}
            elif (not is_equal("0", str(i)) and 
                  not is_equal(str(len(n)-1), str(i))):
                if ((n[i-1] not in numbers and not is_equal(n[i-1], "-") and
                     not is_equal(n[i-1], "(") and not is_equal(n[i-1], "|")) 
                     and n[i+1] not in numbers):
                    print("Cannot accept input.")
                    print("A decimal must have one number on its right and "
                    "either another number, a minus, an open parentheses or a "
                    "vertical bar on its left.")
                    return False                    
        
        #Open parentheses
        elif (is_equal(n[i], "(")):
            #Account for | and (
            #Right side must be |, (, - (Must not be last element), ., #
            
            #If the term that preceded the current one is a number, then the
            #current term should be an operator sign, which can't be used with
            #any parentheses
            if (prev):
                print("Cannot accept input.")
                print("An operation sign must occur before a term that has "
                "parentheses.")                
                return False            
            #Open parentheses cannot be used on its own
            elif (is_equal(str(len(n)), "1")):
                print("Cannot accept input.")
                print("An open parentheses cannot be used by itself.")                
                return False
            #Open parentheses cannot be the last character of any term
            elif (is_equal(str(i), str(len(n)-1))):
                print("Cannot accept input.")
                print("An open parentheses cannot be used at the end of "
                "a numerical term.")                
                return False
            #Only certain characters can be on the right or left side
            if (not is_equal(str(i), "0")):
                if (not is_equal(n[i-1], "(") and not is_equal(n[i-1], "|")):
                    print("Cannot accept input.")
                    print("An open parentheses can only directly follow a "
                        "vertical bar or another open parentheses.")
                    return False
                if (is_equal(str(i), str(len(n)-2))):
                    if (n[i+1] not in numbers):
                        print("Cannot accept input.")
                        print("An open parentheses can only be directly "
                            "followed by a number.")
                        return False
            else:
                if (not is_equal(n[i+1], "-") and not is_equal(n[i+1], ".") and
                    not is_equal(n[i+1], "|") and not is_equal(n[i+1], "(") and 
                    n[i+1] not in numbers):
                    print("Cannot accept input.")
                    print("An operation sign cannot directly follow an "
                        "open parentheses.")                
                    return False              
        
        #Close parentheses
        elif (is_equal(n[i], ")")):
            #Account for | and )
            #Symbol other than ., | to the left, anything on right
            #Left side must be |, ), ., #
            
            #If the term that preceded the current one is a number, then the
            #current term should be an operator sign, which can't be used with
            #any parentheses            
            if (prev):
                print("Cannot accept input.")
                print("An operation sign must occur before a term that has "
                "parentheses.")                
                return False            
            #Close parentheses cannot be used on its own
            elif (is_equal(str(len(n)), "1")):
                print("Cannot accept input.")
                print("A close parentheses cannot be used by itself.")                
                return False
            #Close parentheses cannot be the first character of any term
            elif (is_equal(str(i), "0")):
                print("Cannot accept input.")
                print("A close parentheses cannot be used at the start of "
                "a numerical term.")                
                return False
            #Only certain characters can be on the right or left side
            if (not is_equal(str(i), str(len(n)-1))):
                if (not is_equal(n[i+1], ")") and not is_equal(n[i+1], "|")):
                    print("Cannot accept input.")
                    print("A close parentheses can only be followed by a "
                        "vertical bar or another close parentheses.")
                    return False
                if (is_equal(str(i), "1")):
                    if (n[i-1] not in numbers):
                        print("Cannot accept input.")
                        print("A close parentheses can only directly "
                            "preceded by a number.")
                        return False
            else:
                if (not is_equal(n[i-1], ".") and not is_equal(n[i-1], "|") and
                    not is_equal(n[i-1], ")") and n[i-1] not in numbers):
                    print("Cannot accept input.")
                    print("An operation sign cannot be the end of the "
                        "expression contained within parentheses.")                
                    return False                            
        
        #Vertical bar (for absolute value)
        elif (is_equal(n[i], "|")):
            #Symbol on both sides other than - (only to right and not last), ., (, )
            
            #If the term that preceded the current one is a number, then the
            #current term should be an operator sign, which can't be used with
            #any vertical bars          
            if (prev):
                print("Cannot accept input.")
                print("An operation sign must occur before a term that has "
                "vertical bars for absolute value.")                
                return False            
            #Vertical bar cannot be used on its own
            elif (is_equal(str(len(n)), "1")):
                print("Cannot accept input.")
                print("A vertical bar cannot be used by itself.")                
                return False
            #Only certain characters can be on the right side
            if (not is_equal(str(i), str(len(n)-1))):
                if (not is_equal(n[i+1], "-") and not is_equal(n[i+1], ".") and
                    not is_equal(n[i+1], "(") and not is_equal(n[i+1], ")") and
                    n[i+1] not in numbers):
                    print("Cannot accept input.")
                    print("A vertical bar can only be followed by numbers and "
                    "certain characters.")                
                    return False                    
            #Only certain characters can be on the left side
            if (not is_equal(str(i), "0")):
                if (not is_equal(n[i-1], ".") and not is_equal(n[i-1], "(") and 
                    not is_equal(n[i-1], ")") and n[i-1] not in numbers):
                    print("Cannot accept input.")
                    print("A vertical bar can only be preceded by numbers and "
                    "certain characters.")                
                    return False
        
        #Make sure that any equals sign used is as the sole character of an
        #element of the input
        elif (is_equal(n[i], "=")):
            if (not is_equal(str(len(n)), "1")):
                print("Cannot accept input.")
                print("The equals sign must either be used alone or as the "
                      "last character of an input.")                
                return False
            #The last term before the equals sign has to be a numerical term
            if (not prev):
                print("Cannot accept input.")
                print("An equals sign must be preceded by a numerical term.")
                return False            
        
        #c/C can only be used as the sole character of the sole term of an
        #input
        elif (is_equal(n[i], "c") or is_equal(n[i], "C")):
            print("Cannot accept input.")
            print("Clear is called by inputting c or C alone.")
            return False
        
        #If the user attempts to use < or >
        elif (is_equal(n[i], "<") or is_equal(n[i], ">")):
            print("Cannot accept input.")
            print("User is not allowed to use < or >.")
            return False            
        
        #Numbers
        elif (n[i] in numbers):
            #A number can only have certain symbols on either side
            #The current term can't be a number if previous element was a number
            if (prev):
                print("Cannot accept input.")
                print("A numerical term cannot immediately follow another "
                "numerical term.")
                return False
            #Only certain characters can be on the right side
            if (not is_equal(str(i), str(len(n)-1))):
                if (not is_equal(n[i+1], ".") and not is_equal(n[i+1], ")") and
                    not is_equal(n[i+1], "|") and n[i+1] not in numbers):
                    print("Cannot accept input.")
                    print("Number can only be followed by other numbers and "
                    "certain characters.")                
                    return False
            #Only certain characters can be on the left side
            if (not is_equal(str(i), "0")):
                if (not is_equal(n[i-1], "-") and not is_equal(n[i-1], ".") and
                    not is_equal(n[i-1], "(") and not is_equal(n[i-1], "|") and
                    n[i-1] not in numbers):
                    print("Cannot accept input.")
                    print("Number can only be preceded by other numbers and "
                    "certain characters.")                
                    return False
        
        #For operator signs +, *, /, ^
        elif (n[i] in symbols):
            #The current term can't be an operation symbol if the previous was
            #an operator symbol
            if (not prev):
                print("Cannot accept input.")
                print("An operation sign cannot immediately follow another "
                "operation sign.")
                return False
            #The term holding the operator sign must be a length of 1
            elif (not is_equal(str(len(n)), "1")):
                print("Cannot accept input.")
                print("An operation sign must be used by itself.")                
                return False
        
        #For if an undefined character (e.g. @) was inputted
        elif (n[i] not in numbers and n[i] not in symbols):
            print("Cannot accept input.")
            print("Unknown character was used.")
            return False
        
    #All characters of the input are correctly formatted
    return True



#Check to make sure that all parentheses and all absolute values are properly
#closed
def check_pairs(n_list):
    pairs = []
    found_bar = False
    
    for i in range(len(n_list)):
        for j in range(len(n_list[i])):
            #Append any open parentheses found to pairs
            if (is_equal(n_list[i][j], "(")):
                pairs.append(n_list[i][j])
            
            #Append a vertical bar if it would be the left half of two bars
            elif (is_equal(n_list[i][j], "|") and not found_bar):
                found_bar = True
                pairs.append(n_list[i][j])
            
            #Found a close parentheses, or the right half of two bars
            #Pop the last element of pairs, and check that it corresponds to
            #n[i][j] { ( corresponds to ), | to a second | }
            elif (is_equal(n_list[i][j], ")") or 
                  (is_equal(n_list[i][j], "|") and found_bar)):
                if (not is_equal(str(len(pairs)), "0")):
                    p = pairs.pop()
                    if (is_equal(p, "|")):
                        found_bar = False
                        
                    if (is_equal(p, "(") and is_equal(n_list[i][j], "|")):
                        print("Cannot accept input.")
                        print("Absolute value was closed before inner "
                        "parentheses was closed.")
                        return False
                    elif (is_equal(p, "|") and is_equal(n_list[i][j], ")")):
                        print("Cannot accept input.")
                        print("Parentheses was closed before inner absolute "
                        "value was closed.")
                        return False
                else:
                    print("Cannot accept input.")
                    print("Could not close all parentheses, or could not close "
                    "all absolute values.")
                    return False
        
    if (not is_equal(str(len(pairs)), "0")):
        print("Cannot accept input.")
        print("There is at least one open parentheses or at least one vertical "
        "bar that remains unpaired.")
        return False   
    
    return True
