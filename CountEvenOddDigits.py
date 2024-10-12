#Problem 2:Write a program named CountEvenOddDigits.py that accept a number (non-zero digit) from 
# command argument list, then count and display the number of odd and even digit in the number.
#For example, for number 123456, there are 3 even digits and 3 odd digits. 

#get input
nonZeroNumber = int(input('please input a number greater than 0: '))

#counter initialization
counterEven = 0
counterOdd = 0

##converting the number to a string so I can iterate with a loop
numberAsString = str(nonZeroNumber)

#if loop to ensure its not 0
if nonZeroNumber == 0:
    print('Please input a number that is not zero')

#for loop that iterates to check each digit in the number
for digit in numberAsString:
    digit = int(digit)
    if digit % 2 == 0:
        counterEven = counterEven + 1
    else:
        counterOdd = counterOdd + 1
    digit = digit // 10

print('The number ', nonZeroNumber, ' has ', counterEven, ' even numbers and ', counterOdd, ' odd numbers')