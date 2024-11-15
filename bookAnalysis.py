#bookAnalysis.py
import string
from plotly.graph_objs import Bar, Layout
import matplotlib.pyplot as plt
from collections import Counter
from plotly import offline
import sys
import os

#this code has two nested functions. 
#the first one will count the frequency of letters in a provided text file and return it as a graph in terminal
#The second function will count the frequency of letters as well, and then plot them on a graph as well as provide
#a bar graph showing the frequency
#it accepts any text file (converts to utf-8)
#Messing around with nested functions a bit here as well as different methods of data visualization



#this is a nested function combining the first two. 
#this will count the frequency of the text file provided
#then it will pass to the printedLettersInTerminal function and print a bar graph using * 
#into the terminal

def charFreqAndPrint(fileName):

#this takes it and returns it purely as an int list
    def charFreq(fileName):
        file=open(fileName,'r', encoding='utf-8') #ensuring that it can read any format (not just ascii)
        res=[0]*26
        for line in file:
            line=line.upper()
            for c in line:
                index= ord(c) - 65
                if index>= 0 and index <26:
                    res[index]+=1
        file.close()
        return res

    def printedLettersInTerminal(charFreq):
        scale = 60
        maxLength = max(charFreq)
        for index in range(len(charFreq)):
            stars = int(charFreq[index]/maxLength * scale)
            if stars == 0:
                stars == 0
            print(chr(65+index),': ', end = '')
            for i in range(stars):
                print('*', end=' ')
            print()

    freqList = charFreq(fileName)
    printedLettersInTerminal(freqList)

#This is a nested function that will produce a bar chart and a plotted graph
#dictating the frequency of letters in the text document provided

def graphicalBarAndPlotGraphs(fileName, graphType='both'):
    def charFreq(fileName):
        #create a dictionary for the Alphanet in lowercase and uppercase
        #set up the dictionary of each letter
        #using the string.ascii_lowercase which holds 26 values a-z
        alphabetDict = {letter: 0 for letter in string.ascii_lowercase}
        #open file
        with open(fileName,'r', encoding='utf-8') as file:
            data = file.read().lower()
        #then look through each character in the fileName and increment the appropriate letter 
        #return all the results for each letter   
            for c in data :
                if c in alphabetDict:
                    alphabetDict[c] += 1

        return alphabetDict


    #pass the charFre function into the barChart
    #then for each letter found, give 2 *(Asteriks) to it in the graph to show (might change this to 1)
    #from here return the entire Alphabet A:a-Z:z as a graph with the stars 
    #maybe combine lower and upper case into one for ease of viewing
    #see if there is any other fun graphs we can use as well - line graph?


    def barChart(charFreq):
        letters = list(charFreq.keys())
        frequency = list(charFreq.values())
        data = [Bar(x=letters,y=frequency)]
        #set up the graph
        x_axis_config = {'title': 'Letters'}
        y_axis_config = {'title': 'Frequency of Letter'}
        #pass the data to the layout
        my_layout = Layout(
            title='Frequency of each letter in the file',
            xaxis=x_axis_config,
            yaxis=y_axis_config
            )
        #create the output file (need to make sure you import os for this to work)
        output_path = 'output/letter_frequency.html'
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)  
        offline.plot({'data': data, 'layout': my_layout}, filename=output_path)


    '''
        print('Letter Frequency')
        for letter in string.ascii_lowercase:
            freq = alphabetDict[letter]
            #printing the Letter: how many ****s, and then a total count at the end for clarity (not ideal for big text files)
            print(f"{letter.upper()}:{'*' * freq} ({freq})")
    '''

    def scatterPlotCharFreq(lettersCount, fileName):
        #count the frequency of each letter 
        
        letters = sorted(lettersCount.keys())
        frequencies = [lettersCount[letter] for letter in letters]

        #tells you the size of the overall image
        plt.figure(figsize=(10,6))
        #Sets the data for X, Y and then specifies the color of the dots
        plt.scatter(letters, frequencies, color='red')
        #Adding lines to it for fun
        #passing arguments of X, Y, color, line, label
        plt.plot(letters, frequencies, color='purple', linestyle=':', label='connecting line')
        #set the title of the graph
        plt.title(f'Frequency of Letters in {fileName}')
        #These are pretty self explanitory
        plt.xlabel('Letters')
        plt.ylabel('Frequency')
        #Puts a grid on it if you want
        plt.grid(True)
        #displays it on the screen
        plt.show()
    
    freqDict = charFreq(fileName)
    if graphType == 'bar':
        barChart(freqDict)
    elif graphType == 'plot':
        scatterPlotCharFreq(freqDict, fileName)
    elif graphType == 'both':
        barChart(freqDict)
        scatterPlotCharFreq(freqDict, fileName)

#get the user input to see how they wish to view this information
#either can see it printed in terminal using * or through a bar graph or plot graph
def getUserInput(fileName):
    inTerminal=input('if you would like to run the character frequency count and display results in your terminal, please press Y ')
    if inTerminal == 'y' or inTerminal== 'Y':
        charFreqAndPrint(fileName)
        graphType = input('Would you like to also see it in a bar graph or plot? Please specify which (or both for both) by typing bar, plot, or both')
        if graphType.lower() in ['bar','plot','both']:
            graphicalBarAndPlotGraphs(fileName, graphType=graphType.lower())
            continueAgain = input('Would you like to see it the other way? y/n')
            if graphType.lower()=='bar' and (continueAgain=='y' or continueAgain=='Y'):
                graphicalBarAndPlotGraphs(fileName, graphType='plot')
            elif graphType.lower()=='plot' and (continueAgain=='y' or continueAgain=='Y'):
                graphicalBarAndPlotGraphs(fileName, graphType='bar')

    else:
        GraphicalVisualization = input('Do you wish to see it in a different format? Y/n: ')
        if GraphicalVisualization == 'y' or GraphicalVisualization == 'Y':
            graphType=input('Please enter how you wish to see this data. your options are: bar, plot, or both: ')
            
            if graphType.lower()=='bar':
                graphicalBarAndPlotGraphs(fileName, graphType='bar')
                continueAgain = input('Would you like to see it in a plot graph as well? y/n')
                if continueAgain == 'y' or continueAgain == 'Y':
                    graphicalBarAndPlotGraphs(fileName, graphType='plot')
            elif graphType.lower()== 'plot':
                graphicalBarAndPlotGraphs(fileName,graphType='plot')
                continueAgain = input('would you like to see it in a bar graph as well? y/n')
                if continueAgain == 'y' or continueAgain == 'Y':
                    graphicalBarAndPlotGraphs(fileName, graphType='bar')
            elif graphType.lower() =='both':
                graphicalBarAndPlotGraphs(fileName, graphType='both')
        else:
            print('No other visualization has been selected.')
   
fileName = sys.argv[1]
getUserInput(fileName)


