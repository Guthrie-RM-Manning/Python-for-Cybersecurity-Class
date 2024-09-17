##Divisible.py
##Write a program called Divisible.py that reads in three numbers from the argument list
##Caluclate and display the remainders of the three numbers after they are divided by 21
##Start by importing sys for the arguments

import sys

firstNumber = int(sys.argv[1])
secondNumber = int(sys.argv[2])
thirdNumber = int(sys.argv[3])

divisionOne = firstNumber % 21 
divisionTwo = secondNumber % 21
divisionThree = thirdNumber % 21

print(str(divisionOne))
print(str(divisionTwo))
print(str(divisionThree))

