class Oras:
    x = ""
    y = ""
    nume = ""
    judet = ""
    judetAuto = ""
    populatie = ""
    regiune = ""

    def __init__(self, x, y, nume, judet, judetAuto, populatie, regiune):
        self.x = x
        self.y = y
        self.nume = nume
        self.judet = judet
        self.judetAuto = judetAuto
        self.populatie = populatie
        self.regiune = regiune

    def __str__(self):
        return str(self.x) + str(self.y) + str(self.nume) + str(self.judet) + str(self.judetAuto) + str(self.populatie) + str(self.regiune)