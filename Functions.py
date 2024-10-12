#Functions.py
#Write an application named Functions.py and implement the following functions:
# 1. countEvenDigits(num), it counts and returns the number of even digits in the num.
#  for example, calling countEvenDigits(12346) should return 3, because there are 3 even 
# digits: 2, 4, and 6
#
# 2. countEvenDigitsInString(aStr), it counts and returns the number of even 
# digits in the String: aStr.
# For example, calling countEvenDigitsInString("22346") should return 4, 
# because there are 4 even digits:2, 2, 4, and 6
#
# 3. isRightTriangle(a, b, c), it evaluates if the three numbers 
# (integers): a, b, and c can form a right triangle,
#  returns true if yes, otherwise, returns false.
# Once completed, run your application by passing numbers through argument
#  list to test all three functions.

#Function 1countEvenDigits(num)

def countEvenDigits(num):
    nonZeroNumber = num
    #counter initialization
    counterEven = 0
    ##converting the number to a string so I can iterate with a loop
    numberAsString = str(num)

    #if loop to ensure its not 0
    if nonZeroNumber == 0:
        print('Please input a number that is not zero')

    #for loop that iterates to check each digit in the number
    for digit in numberAsString:
        digit = int(digit)
        if digit % 2 == 0:
            counterEven = counterEven + 1
        digit = digit // 10
    return('the number of even numbers in this number are: ', counterEven)

#Define evenDigitsInString(aStr)
def evenDigitsInString(aStr):
    #get input
    nonZeroNumber = aStr
    #counter initialization
    counterEven = 0

    #for loop that iterates to check each digit in the number
    for digit in aStr:
        digit = int(digit)
        if digit % 2 == 0:
            counterEven = counterEven + 1
        digit = digit // 10

    return('the number of even numbers in this number are: ', counterEven)

def isRightTriangle(a, b, c):
   #pythagorasss! (a**2) + (b**2) = (c**2) check it

    if a**2 + b**2 == c**2:
        area = 0.5 * a * b
        return('The area of this trinagle that these numbers make is: ', area)
    else:
        return('these cannot make a right triangle')


# get inputs to check

num = input('please enter a number that is not zero: ')
aStr = num
a = int(input('please enter the length of side A for a triangle '))
b = int(input('please enter the length for side B of a triangle '))
c = int(input('please enter the length for side C on your Triangle '))

resultsEvenDigits = countEvenDigits(num)
resultsString = evenDigitsInString(aStr)
resultsTriangle = isRightTriangle(a,b,c)

print(resultsEvenDigits)
print(resultsString)
print(resultsTriangle)

