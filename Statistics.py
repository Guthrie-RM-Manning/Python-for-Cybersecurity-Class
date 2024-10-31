#statistics.py

#average
def average(fileName:str) -> float:
    #Error Handling 
    try:
    
        #read from file containing numbers
        with open(fileName, 'r', encoding='utf-8') as file_object:
            #assign the contents of the file that is being read to a variable
            contents = file_object.read()
            #make the contents into a list to look at
            n = list(map(float, contents.split()))
            if not n:
                return 0
            #return the average (sum of n / len(n) which is your total/# of values)
            return sum(n) / len(n)
    #handle the error if FileNotFound
    except FileNotFoundError:
            print(f'Sorry, thie file name {fileName} does not exist.')
            return 0

#smallest - putting it into a list to practice making lists of lines from a file
def smallest(fileName:str) -> int:
    #error handling
    try:

        #read from the file
        with open(fileName,'r',encoding='utf-8') as file_object:
            contents = file_object.read()
            number = list(map(int, contents.split))
            return min(number) if number else None
    except FileNotFoundError:
        print(f'sorry, the file name {fileName} does not exist.')
        return None

#largest
def largest(fileName:str) ->int:
    #error Handling
    try:
        #read from the file
        with open(fileName, 'r', encoding='utf-8') as file_object:
            contents = file_object.read()
            n = list(map(int, contents.split()))
        return max(n) if n else None
    except FileNotFoundError:
        print(f'Sorry, the file name {fileName} does not exist')
    

#testFile = <<insert path test file here>>


print(f'the average of the numbers in {testFile} are: ', average(testFile))
print(f'the smallest number in {testFile} is: ', smallest(testFile))
print(f' the largest number in {testFile} is: ', largest(testFile))

        
