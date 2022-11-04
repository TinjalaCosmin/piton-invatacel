class Person:
    firstName = "ionel"
    lastName = "marioara"
    age = ""
#-----------------------------------------------------------------------------
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return "Person named " + self.firstName + " " + self.lastName + " is " + str(self.age) + " years old"

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAge(self):
        return self.age
#----------------------------------------------------------------------------

def readFile(n, filename):
    f = open(filename, "r")
    arr = [0] * n

    for i in range(0, n):
        arr[i] = f.readline()

    f.close()

    return arr
#-----------------------------------------------------------------------------

def readLineData(str):
    n = 3
    arr = [0] * n
    word = ''
    i = 0
    j = 0

    for i in range(0, len(str)):
        letter = str[i]

        if ord(letter) == 44:
            word = ''
            j = j + 1
        else:
            word = word + letter

        arr[j] = word

    return arr
#-----------------------------------------------------------------------------------

def sortByAge(arr, n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i].age > arr[j].age:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux

    return arr

#-------------------------------------------------------------------------------
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i])

#----------------------------------------------------------------------------------
n = 5
data = readFile(n, "2022-10-27_Practice/file.txt")
persons = [0] * n

for i in range(0, n):
    [firstName, lastName, age] = readLineData(data[i])

    persons[i] = Person(firstName, lastName, int(age))

orderedPersons = sortByAge(persons, n)
printArray(orderedPersons)