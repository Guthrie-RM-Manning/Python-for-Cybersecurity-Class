#Write a program named RandomNumber.py that generates 
# 3 numbers between [50, 200], then determine and display if they are 
# divisible by 21 Once you completed, please run your program several times 
# and observe the results.

import random

firstNumber = random.randint(1, 100)
secondNumber = random.randint(1, 100)
thirdNumber = random.randint(1,100)

print(firstNumber)
print(secondNumber)
print(thirdNumber)

#check if they are divisible by 21

if firstNumber % 21 != 0: 
    print(firstNumber, ' is not divisible by 21')
else:
    print(firstNumber, ' is divisible by 21')

if secondNumber % 21 != 0:
    print(secondNumber, ' is not divisible by 21')
else:
    print(secondNumber, ' is divisible by 21')

if thirdNumber % 21 != 0:
    print(thirdNumber, ' is not divisible by 21')
else:
    print(thirdNumber, ' is divisible by 21')

