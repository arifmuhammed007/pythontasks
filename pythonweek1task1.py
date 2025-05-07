#1) Find the last digit of 7^35.

print("the last digit is:",7**35%10)

#2)Find the remainder when 987654321 is divided by 123456789.
 
print("the reminder is:",987654321%123456789)

#3) Predict the output of the following lines:
"""
print(5 - 3)
print(5 - - 3)
print(5 - - - 3)
print(5 - - - - 3)
print(5 - - - - - 3)

"""
print("\n output:")
print(5 - 3)          # Output: 2
print(5 - - 3)        # Output: 8
print(5 - - - 3)      # Output: 2
print(5 - - - - 3)    # Output: 2
print(5 - - - - - 3)  # Output: 8

#4)Parenthesize this expression so that the result is zero: 
#    2 ** 2 - 2 - 2 / 2

print("Result:",2**2-2-2)

#5 Predict the output of the following expression: 
#   0 == 0 < 1 < 2 < 3 > 2 > 1 > 0 == 0

print("output:", 0 == 0 < 1 < 2 < 3 > 2 > 1 > 0 == 0)

#6)If s is a string of length n, how many characters does n *s have, where n is some positive integer?

s = "abc"   
n = 4
result = n * s  
print(result)        
print(len(result))   
#7)What will be the outcome of the following expression if x and y are two strings?
 #len(x) + len(y) == len(x + y)

print("ans: is true")

#8)What does the following code do? 
# print(input())
 # ans)It takes user input from the keyboard.

#Then prints that input back to the screen.
#9)Consider the following code snippet. If the output of the code snippet given above is 123, what is the sequence of inputs entered by the user?
#print(input() + input() + input())

#ans)
print("1", "2", "3")

#10)Find the number of digits in 7**100. Treat this as a programming question and not as a mathematical question. You should be able to do this using the concepts you have learned.

num = len(str(7**100))
print("number of digits",num)

#11)Accept a positive integer, x, as input from the user. Without using the * symbol anywhere in your code, print 10 * x, i.e., the product of the integer input and the number 10.

X = int(input("Enter a positive intiger:"))
sum = 0
for i in range(10):
    sum += X

print("result is:",sum)    

#12) Accept the length and breadth of a rectangle as input and compute its area. 

def area():
    l = int(input("Enter length:"))
    b = int(input("Enter breadth:"))
    return l*b

print("Area of reactangle is:",area())

#13)Accept a positive real number x as input and print the greatest integer less than or equal to x. Hint: floor function


import math

x = float(input("Enter a positive real number:"))
result = math.floor(x)
print("The greatest integer is less than or equal to :",x ,"is",result)

#14) Accept a positive real number x as input and print the smallest integer greater than or equal to x. Hint: ceil function

def printsmallest():
    import math
    z = float(input("Enter a positive real number:"))
    result = math.ceil(z)
    return result
print(printsmallest())

"""
15) A user enters two integers as input and this is the output returned by the code:
a = int(input())
b = int(input())
print(0 < a < b < 10)
print(b - a == 1) 


How many different pairs (a, b) of inputs are possible for such a scenario?
"""
for a in range(1,9):
    b = a + 1
    if 0 < a < b < 10 and b - a == 1:
        print(a,b)

#16)Accept a two-digit number as input and print the sum of its digits ( Hint : Use modulus and division)

twodigit = int(input("Enter a two digit number:"))

firstdigit = twodigit//10
secdigit = twodigit%10

print(firstdigit+secdigit)