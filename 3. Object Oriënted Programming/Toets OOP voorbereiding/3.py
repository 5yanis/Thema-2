class fiets:
    def __init__(self, uniek_nummer, type):
        self.type=type
        self.uniek_nummer=uniek_nummer


fiets1=fiets(20, "elektrisch")
fiets2=fiets(31, "klassiek")
fiets3=fiets(32, "klassiek")
print(type(fiets1))