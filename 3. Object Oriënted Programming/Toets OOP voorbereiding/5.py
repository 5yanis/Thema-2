class fiets:
    def __init__(self, uniek_nummer, type, lening=False):
        self.type=type
        self.lening=lening
        self.uniek_nummer=uniek_nummer
    def lenen(self):
        if self.lening:
            print("lening gelukt!!")
    


fiets1=fiets(20, "elektrisch")
fiets2=fiets(22, "klassiek", True)
fiets3=fiets(32, "klassiek")
fiets2.lenen()




