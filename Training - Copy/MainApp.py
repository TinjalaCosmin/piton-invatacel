from Duck import Duck

def readFile(numberOfRows, filename):
    file = open(filename, "r")
    arrayWithFileContent = [0] * numberOfRows

    for i in range(0, numberOfRows):
        arrayWithFileContent[i] = file.readline()
    
    file.close()
    return arrayWithFileContent

def readLineData(fileRowData, numberOfVariablesInsideClass):
    arr = [0] * numberOfVariablesInsideClass
    word = ''
    j = 0

    for i in range(0, len(fileRowData)):
        letter = fileRowData[i]

        if letter == ",":
            word = ''
            j = j + 1
        else:
            word = word + letter 

        arr[j] = word           

    return arr

numberOfRows = 3
duckNumberOfVariables = 2
ducksFileArray = readFile(numberOfRows, "duckInfo.txt")
ducksArray = [0] * numberOfRows
for i in range(0, numberOfRows):
    [name, age] = readLineData(ducksFileArray[i], duckNumberOfVariables)
    duck = Duck(name, age)
    print(duck.macane())
    ducksArray[i] = Duck(name, age)