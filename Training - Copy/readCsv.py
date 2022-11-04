from MainApp import readFile, readLineData
from Oras import Oras

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

listaCuOrase = readFile(10, "orase.csv")
numberOfRows = 1000
numberOfVariables = 7
for i in range(0, numberOfRows):
    [x, y, nume, judet, judetAuto, populati, regiune] = readLineData(listaCuOrase, 7)
    oras = Oras(x, y, nume, judet, judetAuto, populati, regiune)
    print("Oras: " + str(oras))