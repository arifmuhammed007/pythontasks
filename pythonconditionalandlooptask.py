#1)Leap Year Checker: Write a Python program that checks if a given year is a leap year.

def is_leapyear(year):
    if(year % 4 == 0) and (year %100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    

year = int(input("Enter a year:"))    

if is_leapyear(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")    


#2) Grade Calculator: Write a program that converts a score (0-100) into a corresponding letter grade (A, B, C, D, F).

def lettergrade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score'
    
score = int(input("Enter you score (0-100):"))

grade = lettergrade(score)

print(f"Your grade is: {grade}")

#3)Temperature Conversion: Write a Python program that converts a temperature from Fahrenheit to Celsius or vice versa, based on user input.

def fahr_to_cel(f):
    return (f-32)*5/9

def cel_tofahr(c):
    return (c * 9/5) + 32

print("Temperature converter")
print("1. fahrenheit to celsius")
print("2. celsius to fahrenheit")
choice = int(input("Choos convertion type:"))

if choice == 1:
    f = float(input("Enter value in fahrenheit:"))
    c = fahr_to_cel(f)
    print(f"tempreture in celsius is :{c}")
elif choice == 2:
    c = float(input("Enter tempreture in celsius:"))
    f = cel_tofahr(c)
    print(f"Temperature in fahrenheit:{f}")    
else:
    print("please enter 1 or 2")    


#4)Triangle Type Checker: Write a Python program that determines whether a triangle is equilateral, isosceles, or scalene based on its side lengths.


def trangletype(a,b,c):
    if (a + b > c) and (a + c > b) and (c + b > a):
        if a == b == c:
            return "Equilateral"
        elif a == b or c == a or c == b:
            return "isosceles"
        else:
            return "Scalene"
    else:
        print("not a valid tarangle")    

a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))
c = float(input("Enter length of side C: "))

result = trangletype(a,b,c)

print("Result:",result)


#5)Factorial Calculation: Write a Python program to calculate the factorial of a given number using a for loop.

value = int(input("Enter a positive number:"))

factoreal = 1 
for i in range(1,value+1):
    factoreal *= i
print("the factoreal of value is is :",factoreal)    

#6)Multiplication Table: Write a Python program that prints the multiplication table for a given number up to 10.

number = int(input("Enter a number:"))

for i in range(1,11):
    print(i,"x",number,"=",i*number)

#7)Reversing a String: Write a Python program that takes a string as input and prints the reversed string using a for loop.

text = input("Enter a word:")
length = len(text)
r_word = ""

for i in range(length):
    r_word = text[::-1]

print(r_word)    

#8)Count Vowels in a String: Write a Python program that counts the number of vowels in a given string using a for loop

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = "Hello, how are you?"
vowel_count = count_vowels(input_string)
print(f"Number of vowels in the string: {vowel_count}")


#9)star pattern

print("\n star pattern")

row = 5 
for i in range(1,row+1):
    print("*"*i)

#10)find totalmark

marks_dict = {
    "Mathematics": 95,
    "English": 88,
    "Science": 92,
    "History": 85,
    "Geography": 90
}

total_mark = sum(marks_dict.values())
print("total mark",total_mark)    










