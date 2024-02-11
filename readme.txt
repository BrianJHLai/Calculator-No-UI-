This is a calculator that has no user interface; as such, it takes in user-typed inputs in the form of mathematical expressions or equations. Upon entering an input, it will be checked by a parser, which will output a response if the input isn't in an accepted format before asking again for an input. 

With the exception of incrementing and decrementing (counting up and down by 1), no built-in mathematical operations and comparison operators are used to perform mathematical computations. Additionally, any math done is with strings rather than integers or floats.

The user can input an equation, an expression or the clear option (c/C). After every input that is an equation or an expression, if accepted, the user will be asked for subsequent inputs. Every subsequent input will build upon the previous expression/result (e.g. Entering "+ 9 =" after a result of "5" will make the equation "5 + 9 =", which will give a result of "14"). 

If an equation or expression is inputted in the starting-symbol format before anything is stored in the calculator, 0 will be taken as the beginning of the inputted equation/expression. Inputting an equation or expression in the starting-number format after the calculator already has a stored expression/result will cause clear to be automatically called before the user is informed that their most recent input was accepted (Clear won't be called if the input wasn't accepted).

Entering c or C will call the clear function, which will immediately delete the stored expression/result (if any has been made) before asking for an input again. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Using x to represent a number or expression, the available operations/number types and their accepted format(s) are:
-Addition: x + x
-Subtraction: x - x
-Multiplication: x * x
-Division: x / x
-Exponate: x ^ x
-Parentheses: (x)
-Absolute value: |x|
-Equals: = or x =
-Clear: c or C
-Negation (x is a number) (Functions for this not yet implemented): -x
-Decimal (x is a number) (Functions for this not yet implemented): x.x; .x; x.

-Expression Example: # + # - #
-Expression EXample (Subsequent): + # - #
-Equation Example: # + # - # =
-Equation Example (Subsequent): + # - # =
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Character Format Guidelines
0-9 (numbers): The term preceding a numerical term must be an operation sign. Can be preceded by an open parentheses, a vertical bar, a negative sign, a decimal or another number. Can be followed by a close parentheses, a vertical bar, a decimal or another number.

+ , -, *, /, ^ (operator signs): Must have a space on both its left and right sides. If not the first term of an input, the preceding term must be a numerical one.

- (as a negative sign): Must be followed by a decimal or a number. Can be preceded by an open parentheses or a vertical bar

. (decimal): Must be preceded or followed by a number. Can be preceded by a number, a negative sign, an open parentheses or a vertical bar. Can be followed by a number, a close parentheses or a vertical bar. 

( (open parentheses): Can be preceded by another open parentheses or a vertical. Can be followed by another open parentheses, a vertical bar, a negative sign, a decimal or a number.

) (close parentheses): Can be preceded by another close parentheses, a vertical bar, a decimal or a number. Can be followed by another close parentheses or a vertical bar.

| (vertical bar [for absolute value]): Can be preceded by another vertical bar, an open parentheses, a close parentheses, a decimal or a number. Can be followed by another vertical bar, an open parentheses, a close parentheses, a negative sign, a decimal or a number. As of this version, cannot have absolute value within another absolute value (e.g. ||1 - 2| -5|).

= (equals sign): Must be the last character of any input. Can only be used at most once in an input. Must be preceded by a space.

c/C (clear): Must be the only character in an input
--------------------------------------------------------------------------------------------------------------------------------------------------------------
v 0.4
-Added the main() function
	-Continously asks the user for an input
-Added the input_parse() function
	-Parses each user input to ensure that the input follows the set guidelines
-Added the calculate() function
	-Calculates the result of a given equation
-Added a few additional elements to equals and symbols tuples
-Removed usage of clean() from is_equal(), is_greater(), is_less(), add(), sub(), mult(), div(), exp(), abv()
	-clean() is applied to numbers in calculate() and its helper functions prior to any mathematical operations
-Dropped idea of clear() due to being obsolete
--------------------------------------------------------------------------------------------------------------------------------------------------------------
To-do next:
-Cleaning up every function through better formatting, better consistency, etc
-Reviewing and adding/amending comments to better explain each function's purpose, as well as the steps taken inside each one
-Further testing of main(), input_parse() and calculate(), as well as various other major functions by extension
-Implement versions of add(), sub(), mult(), div() and exp() that handle negative and/or decimal parameters
-Expand guidelines for absolute value
-Possibly expand guidelines for open parentheses
-Possibly try except blocks for if any parameters aren't strings
-Possibly add commas when outputting a result