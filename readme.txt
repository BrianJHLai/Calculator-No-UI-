This is a calculator that has no user interface; as such, it takes in user-typed inputs in the form of mathematical expressions or equations. Upon entering an input, it will be checked by a parser, which will output a response if the input  isn't in an accepted format before asking again for an input. 

With the exception of incrementing and decrementing (counting up and down by 1), no built-in mathematical operations and comparison operators are used. Additionally, any math done is with strings rather than integers or floats.

If the entered input is an equation, the result will be calculated immediately. If the entered input is an expression, the user can 1) enter an equals sign to turn the expression into an equation, or 2) add onto the inputted expression with another expression to create a larger expression. To add on another expression, the expression must start with an operation symbol (+, -, *, /, ^). Inputting an expression starting with a string number, open parentheses, vertical bar or period will clear the stored expression.

Entering c or C will clear (both the stored expression and the result).

Using x to represent a number or expression, the available operations/numeral systems and their correct format(s) are:
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

v 0.1
-Created is_equal() function
	-A function to be used in lieu of the == comparison operator
-Created is_greater() function
	-A function to be used in lieu of the > comparison operator
-Created is_less() function
	-A function to be used in lieu of the < comparison operator
-Created clean() helper function
	-A helper function to format string representing numbers 
		-No leading or trailing 0's
		-String floats that are between 0 and 1 or -1 will have a 0 placed just before the decimal if the string doesn't already have that
		-Any string floats that has all of its decimal digits be 0 will be turned into a string integer (i.e. The decimal and decimal digits will 		be removed)