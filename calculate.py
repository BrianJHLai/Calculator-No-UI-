from gle import is_equal, is_greater, is_less
from clean import clean
from operations import abv
from add import add
from sub import sub
from mult import mult
from div import div
from exp import exp

#Calculate the result of a given equation and return it
def calculate(n):
    result = paren_abv_calc(n)
    
    #exp
    result = operations(result.split(), ["^"])
    
    #mult div
    result = operations(result.split(), ["*", "/"])
    
    #add sub
    result = operations(result.split(), ["+", "-"])
    
    return clean(result)



#3 * 4 + (6 / |(1 + 2) - 5|) - 9 =
#Calculate the value of an expression within parentheses, or calculate the 
#absolute value of an expression/number
def paren_abv_calc(n):
    new_n = ""
    inner_n = ""
    paren_count = 0 #+ 1 if inner open paren, - 1 for close paren. calculate(inner_n) upon find close while 0
    
    i = 0
    while (not is_equal(str(i), str(len(n))) or is_less(str(i), str(len(n)))):
        if (is_equal(n[i], "(")):
            j = i + 1
            while(True):#Change condition
                if (is_equal(n[j], "(")):
                    paren_count += 1
                elif (is_equal(n[j], ")") and 
                      not is_equal(str(paren_count), "0")):
                    paren_count -= 1
                elif (is_equal(n[j], ")")):
                    #Increase i by the length of the inner expression plus 1
                    i = int(add(str(i), add(str(len(inner_n)), "2")))
                    new_n = new_n + clean(calculate(inner_n))##########################
                    inner_n = ""
                    break
                
                inner_n = inner_n + n[j]
                j += 1
        elif (is_equal(n[i], "|")):
            j = i + 1
            while(True):
                if (is_equal(n[j], "|")):
                    i = int(add(str(i), add(str(len(inner_n)), "2")))
                    new_n = new_n + clean(abv(calculate(inner_n)))####################
                    inner_n = ""
                    break
                else:
                    inner_n = inner_n + n[j]
                    j += 1
        else:
            new_n = new_n + n[i]
            i += 1
            
    return new_n



#Calculate exponents, product, quotient, sum or difference
def operations(n_list, op_list):
    i, first, second = 0, 0, 0
    did_op = False
    n1, n2 = "", ""
        
    while (not is_equal(str(i), str(len(n_list))) or 
           is_less(str(i), str(len(n_list)))):#####################################
        did_op = False
        
        #The indexes of the numbers the operation will use
        if ("^" in op_list):
            first, second = len(n_list)-i-2, len(n_list)-i
        else:
            first, second = i-1, i+1
            
        #Get the numbers
        if (not is_equal(str(i), "0") and 
            not is_equal(str(i), str(len(n_list)-1))):
            n1, n2 = n_list[first], n_list[second]
        else:
            i += 1
            continue
        
        #Exponents
        if (is_equal(n_list[i], "^") and "^" in op_list):
            n_list[len(n_list)-i-1] = clean(exp(clean(n1), clean(n2)))######################
            did_op = True
        #Multiplication
        elif (is_equal(n_list[i], "*") and "*" in op_list):
            n_list[i] = clean(mult(clean(n1), clean(n2)))#########################
            did_op = True
        #Division
        elif (is_equal(n_list[i], "/") and "/" in op_list):
            n_list[i] = clean(div(clean(n1), clean(n2)))#########################
            did_op = True
        #Addition
        elif (is_equal(n_list[i], "+") and "+" in op_list):
            n_list[i] = clean(add(clean(n1), clean(n2)))#########################
            did_op = True
        #Subtraction
        elif (is_equal(n_list[i], "-") and "-" in op_list):
            n_list[i] = clean(sub(clean(n1), clean(n2)))#########################
            did_op = True
        
        #Operation was or wasn't performed
        if (did_op):
            n_list.pop(second) #Number after op
            n_list.pop(first) #Number before op
        else:
            i += 1
        
    return " ".join(n_list)