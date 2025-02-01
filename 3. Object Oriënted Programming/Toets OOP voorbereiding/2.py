class fiets:
    def __init__(self, uniek_nummer, type):
        self.type=type
        self.uniek_nummer=uniek_nummer


fiets1=fiets(1, "elektrisch")
fiets2=fiets(2, "klassiek")
print(type(fiets1))