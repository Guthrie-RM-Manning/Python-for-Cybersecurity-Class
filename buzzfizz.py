#write a python program that prints the numbers 1-100
# for anything divisible by 3, print FIZZ and if multiplier of 5, print BUZZ

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print('FIZZBUZZ')
    elif i % 5 == 0:
        print('BUZZ')
    elif i % 3 == 0:
        print('FIZZ')
    else:
        print(i)
