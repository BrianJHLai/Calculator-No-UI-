This is a calculator that has no user interface; as such, it takes in user-typed inputs in the form of mathematical expressions or equations. Upon entering an input, it will be checked by a parser, which will output a response if the input  isn't in an accepted format before asking again for an input. 

With the exception of incrementing and decrementing (counting up and down by 1), no built-in mathematical operations and comparison operators are used to perform mathematical computations. Additionally, any math done is with strings rather than integers or floats.

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
-Negation (Functions for this not yet implemented): -x
-Decimal (Functions for this not yet implemented): x.x

-Expression Example: # + # - #
-Expression EXample (Subsequent): + # - #
-Equation Example: # + # - # =
-Equation Example (Subsequent): + # - # =
--------------------------------------------------------------------------------------------------------------------------------------------------------------
v 0.3
-Added mult() function
	-Multiplie two numbers that are strings and returns their product
-Added exp() function
	-Given two string number, returns the value of the first number raised to the power of the second number
-Added div() function
	-Given two string numbers, returns the quotient where the first number is the dividend and the second is the divisor
-Added minor notes regarding usage of clean() in is_equal(), is_greater(), is_less(), add(), sub() and abs()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
To-do next:
-reader **: Function that parses an input. It will inform the user if the input cannot be accepted as is and states which part and what should be adjusted. Otherwise, it will either add the input to the end of the currently stored expression (and hand the updated stored expression to calculate() if an equals sign was at the end of the input), replace the stored expression, or just clear the stored expression
-calculate(): Function for calculating the result of an equation
-clear(): Erases the value of the stored expression variable
-Implement versions of add(), sub(), mult(), div() and exp() that handle negative and/or decimal parameters
-Possibly try except blocks for if any parameters aren't strings
-Possibly add commas when outputting a result