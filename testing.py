from gle import is_equal, is_greater, is_less
from clean import clean
from operations import abv
from add import add
from sub import sub
from mult import mult
from exp import exp
from div import div

################################################################################
#Tests (The comment after each test is the correct result)
#Clean
"""
print("Clean test 1:", clean("000")) #0
print("Clean test 2:", clean("-0")) #0
print("Clean test 3:", clean("-.560")) #-0.56
print("Clean test 4:", clean("-0.0070")) #-0.007
print("Clean test 5:", clean("000500.")) #500
print("Clean test 6:", clean("c")) #c
print("Clean test 7:", clean("+")) #+
print("Clean test 8:", clean("")) #
"""
#Equal to, Greater Than, Less Than
"""
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
#print("Equals test Empty:", is_equal("-9", "")) #Exception and termination

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
#print("Greater test Empty:", is_greater("-9", "")) #Exception and termination

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
#print("Lesser test Empty:", is_less("-9", "")) #Exception and termination
"""
#Absolute Value
"""
print("AbsV test 1:", abv("00")) #0
print("AbsV test 2:", abv("10")) #10
print("AbsV test 3:", abv("-10")) #10
print("AbsV test 4:", abv("-1.4")) #1.4
print("AbsV test 5:", abv("-.4")) #0.4
print("AbsV test Empty:", abv("")) #Exception and termination
"""
#Addition, Subtraction
"""
print("Add test 1:", add("10", "2")) #12
print("Add test 2:", add("1", "23")) #24
print("Add test 3:", add("543", "321")) #864
print("Add test 4:", add("999", "1")) #1,000
print("Add test 5:", add("1", "9999")) #10,000
print("Add test 6:", add("45", "55")) #100
print("Add test 7:", add("615", "23546")) #24,161
print("Add test 8:", add("0", "0")) #0
print("Add test 9:", add("14", "14")) #28
print("Add test 10:", add("0", "48")) #48
print("Add test 11:", add("36", "0")) #36
#print("Add test Empty:", add("", "14")) #Exception and termination

print("")

print("Subtraction test 1:", sub("10", "2")) #8
print("Subtraction test 2:", sub("104", "5")) #99
print("Subtraction test 3:", sub("2", "7")) #-5
print("Subtraction test 4:", sub("4", "15")) #-11
print("Subtraction test 5:", sub("5", "246")) #-241
print("Subtraction test 6:", sub("1000", "255")) #745
print("Subtraction test 6:", sub("365278", "1643782")) #-1,278,504
print("Subtraction test 8:", sub("27", "27")) #0
print("Subtraction test 9:", sub("0", "0")) #0
print("Subtraction test 10:", sub("98", "0")) #98
print("Subtraction test 11:", sub("0", "26")) #-26
#print("Subtraction test Empty:", sub("", "0")) #Exception and termination

print("")

#print("Negative Add test 1:", add("-10", "-2")) #-12

print("")

#print("Decimal Add test 1:", add("10.5", "2.5")) #13

print("")

#print("Negative Subtraction test 1:", add("-10", "-2")) #

print("")

#print("Decimal Subtraction test 1:", add("10.5", "2.5")) #
"""
#Multiplication, Division, Exponents

print("Multiply test 1:", mult("3", "4")) #12
print("Multiply test 2:", mult("24", "16")) #384
print("Multiply test 3:", mult("456", "3")) #1,368
print("Multiply test 4:", mult("6", "789")) #4,734
print("Multiply test 5:", mult("134", "0")) #0
print("Multiply test 6:", mult("0", "0")) #0
print("Multiply test 7:", mult("0", "7")) #0
print("Multiply test 8:", mult("26436", "36690")) #969,936,840
#print("Multiply test Empty:", mult("", "15")) #Exception and termination

print("")

print("Divide test 1:", div("10", "2")) #5
print("Divide test 2:", div("2", "5")) #0.4
print("Divide test 3:", div("0", "6")) #0
print("Divide test 4:", div("10", "3")) #3.3333333333
print("Divide test 5:", div("10", "7")) #1.4285714285
print("Divide test 6:", div("34467", "23")) #1,498.5652173913
print("Divide test 7:", div("54", "174385")) #0.0003096596
#print("Divide test Zero:", div("7", "0")) #Exception and termination
#print("Divide test Empty:", div("24", "")) #Exception and termination

print("")

print("Exponent test 1:", exp("4", "10")) #1,048,576
print("Exponent test 2:", exp("8", "1")) #8
print("Exponent test 3:", exp("12", "0")) #1
print("Exponent test 4:", exp("12", "4")) #20,736
print("Exponent test 5:", exp("0", "145")) #0
print("Exponent test 6:", exp("0", "0")) #1
print("Exponent test 7:", exp("125", "12")) #14,551,915,228,366,851,806,640,625
#print("Exponent test Empty:", exp("", "6")) #Exception and termination

