#loops.py
#Write an application named Loops.py and perform the following tasks:
#accept two numbers a and b from command argument list, add all numbers between [a, b] 
#if a<=b, or [b, a] if b < a ;
#then
#(1) print the total (summation);
#(2) count and display how many numbers in the range [a, b] are divisible by 13 
# but not 26 if a<=b or in the range of [b, a] if b<=a

import math
#get input
numberA = int(input('Please enter your first number'))
numberB = int(input('Please enter your second number'))

#set up a counter variable 

divisibleCheck = 0

#find the min and maxes for later calculations 
smallestNumber = min(numberA, numberB)
largestNumber = max(numberA, numberB)

#list numbers and print(checking input at the start)
#for numbers in range(numberA, numberB + 1):
    #print(numbers)


#add
totalNumbers = sum(range(smallestNumber, largestNumber + 1))
print(totalNumbers)

##check if a<b or [b,a] if b<c

if numberA < numberB:
    smallestNumber = numberA
    largestNumber = numberB
else:
    smallestNumber = numberB
    largestNumber = numberA

##check divisible by 26 but not 13

for numbers in range(smallestNumber, largestNumber):
    if numbers % 13 == 0 and numbers % 26 != 0:
        divisibleCheck = divisibleCheck + 1

#Print the output (I wasn't sure if there was a way to make this look better)
print('the amount of numbers in the range of ', numberA, 'and ', numberB, 'that are divisible by 13 but not 26 are: ', divisibleCheck)