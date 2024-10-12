#write a program that takes an input and tells you if it is a palindrome or not. If it is print the palindrome both way
# if not, say "(INPUT is not a palindrome)"

#number1

aStr = input('Please input something to check if it is a palindrome: ')
aStrReverse = aStr[:-1]

print(aStrReverse)
if aStr.lower() == aStrReverse.lower(): 
    print('This is a palindrome! Your palindrome is: ', aStr, aStrReverse)
else: 
    print('This is not a palindrome')
