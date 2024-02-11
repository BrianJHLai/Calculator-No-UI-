#If parser accepts input, print out new resulting expression/result
from input_parse import input_parse
from calculate import calculate
from gle import is_equal

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
symbols = ("+", "-", "*", "/", "^", "(", ")", "|", ".", "=", ">", "<", 
           "c", "C", "X")

def main():
    #The expression or result currently stored in the calculator
    expression = ""
    
    while (True):
        #Get user input
        user_input = input("Enter an expression/equation: ")
        
        parsed_input = input_parse(user_input)
        
        #Invalid input
        if (is_equal(parsed_input, "X")):
            continue
        
        #User wants to clear the calculator
        elif (is_equal(parsed_input, "c") or is_equal(parsed_input, "C")):
            expression = ""
        
        #User wants to calculate the result of the stored expression, without
        #adding anything else to the stored expression beforehand
        elif (is_equal(parsed_input, "=")):
            if (is_equal(str(len(expression)), "0")):
                expression = "0"
            else:
                expression = calculate(expression)
                
            print(expression)
        
        #User adds to the stored expression, and may wish to calculate a result
        else:
            #If the first character of the input was an open parentheses
            if (is_equal(parsed_input[0], "(")):
                #Make a copy of the input, then check the first 
                #non-parentheses character
                temp = list(parsed_input).copy()
                temp.pop(0)
                    
                while (is_equal(temp[0], "(")):
                    temp.pop(0)
                        
                #Determine what to do with the input
                #Refer to the below elif and else for what happens to the input
                if (parsed_input[0] in numbers or 
                (parsed_input[0] in symbols and 
                 not is_equal(parsed_input[1], " "))):
                    expression = parsed_input
                else:
                    if (is_equal(str(len(expression)), "0")):
                        expression = "0 " + parsed_input
                    else:
                        expression = expression + parsed_input                  
                
            #If the beginning of the input is a number, set the input as the 
            #stored expression
            elif (parsed_input[0] in numbers or 
            (parsed_input[0] in symbols and 
             not is_equal(parsed_input[1], " "))):
                expression = parsed_input
                
            #If the beginning of the input is an operational symbol 
            #(Not including absolute value)
            else:
                #If the stored expression is empty, add a 0 to the front of the 
                #input, then set the input as the stored expression
                if (is_equal(str(len(expression)), "0")):
                    expression = "0 " + parsed_input
                
                #If the stored expression isn't empty, add the input to the end 
                #of the stored expression
                else:
                    expression = expression + " " + parsed_input
               
            #If the last character of the input was an equals sign, calculate
            #the result
            if (is_equal(parsed_input[-1], "=")):
                print(expression)
                expression = calculate(expression[0:-2])
                
            print(expression)
                
                

#Starting calculator
main()