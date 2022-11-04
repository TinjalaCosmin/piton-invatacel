class Duck:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Duck name " + self.name + " " + "duck age " + str(self.age)
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def macane(self):
        return "Rata " + self.name + " macane si are varsta: " + self.age

    def calculateTypeOfMacanire(self):
        if(self.name == "Emil Boc"):
            return "Ba baiatule"
        else:
            return "Ba ghioorghe"