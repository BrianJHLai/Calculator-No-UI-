This is a calculator that has no user interface; as such, it takes in user-typed inputs in the form of mathematical expressions or equations. Upon entering an input, it will be checked by a parser, which will output a response if the input  isn't in an accepted format before asking again for an input. 

With the exception of incrementing and decrementing (counting up and down by 1), no built-in mathematical operations and comparison operators are used. Additionally, any math done is with strings rather than integers or floats.

The user can input an equation, an expression or the clear option (c/C). After every input that is an equation or an expression, if accepted, the user will be asked for subsequent inputs. Every subsequent input will build upon the previous expression/result (e.g. Entering "+ 9 =" after a result of "5" will make the equation "5 + 9 =", which will give a result of "14"). 

If an equation or expression is inputted in the starting-symbol format before anything is stored in the calculator, 0 will be taken as the beginning of the inputted equation/expression. Inputting an equation or expression in the starting-number format after the calculator already has a stored expression/result will cause clear to be automatically called before the user is informed that their most recent input was accepted (Clear won't be called if the input wasn't accepted).

Entering c or C will call the clear function, which will immediately delete the stored expression/result (if any has been made) before asking for an input again. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Using x to represent a number or expression, the available operations/number types and their correct format(s) are:
-Addition: x + x
-Subtraction: x - x
-Multiplication: x * x
-Division: x / x
-Exponate: x ^ x
-Parentheses: (x)
-Absolute value: |x|
-Equals: = or x =
-Clear: c or C
-Negation: -x
-Decimal: x.x

-Expression Example: # + # - #
-Expression EXample (Subsequent): + # - #
-Equation Example: # + # - # =
-Equation Example (Subsequent): + # - # =

v 0.2
-Created abv() function
	-Returns the absolute value of its given parameter, which is a string number
-Created add() function
	-Adds two numbers, both of which are strings, and outputs the sum
-Created sub() function
	-Subtracts the second parameter from the first, both of which are numbers represented as strings, and outputs the difference
-Moved all tests to testing.py
-Added try except blocks to clean(), is_equal(), is_greater() and is_less() to handle empty strings

To-do next:
-Add mult()
-Add exp()
-Add div()
-Try except blocks for if any parameters aren't strings