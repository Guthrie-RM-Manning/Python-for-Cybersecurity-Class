#set up a dictrionary for the encryption
encryptDict = {
    "one":["_", ",", "@"], 
    "two": ["A","B","C"],
    "three":["D","E","F"],
    "four":["G","H","I"],
    "five":["J","K","L"],
    "six":["M","N","O"],
    "seven":["P","Q","R","S"],
    "eight":["T","U","V"],
    "nine":["W","X","Y","Z"]
}

#function called encrypt that takes the string and looks at each character to convert to a number value based on the keypad
def encrypt(str):
    #empty string to add the #s to
    encryptOutput = []
    for char in str.upper():
        if char.isdigit():
            encryptOutput.append(char)
        elif char in encryptDict["one"]:
            encryptOutput.append("1")
        elif char in encryptDict["two"]:
            encryptOutput.append("2")
        elif char in encryptDict["three"]:
            encryptOutput.append("3")
        elif char in encryptDict["four"]:
            encryptOutput.append("4")
        elif char in encryptDict["five"]:
            encryptOutput.append("4")
        elif char in encryptDict["six"]:
            encryptOutput.append("6")
        elif char in encryptDict["seven"]:
            encryptOutput.append("7")
        elif char in encryptDict["eight"]:
            encryptOutput.append("8")
        elif char in encryptDict["nine"]:
            encryptOutput.append("9")
    return ''.join(encryptOutput)

#input something to encrypt
print(encrypt(input("Please enter what you wish to encrypt:")))
