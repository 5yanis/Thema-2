class persoon:
    def __init__(self, naam):
        self.naam=naam
        self.medewerker=medewerker
    def krijg_naam(self):
        return "naam: {}".format(self.naam)
    def isMedewerker(self, medewerker=False):
        self.medewerker=medewerker
        return "Klasse: {}".format(self.medewerker)




class medewerker(persoon):
    def krijg_naam(self):
        return "naam: {}".format(self.naam)
    def isMedewerker(self):
        self.medewerker=True
        return "Klasse: {}".format(self.medewerker)


persoon1=persoon("Jan")
medewerker1=medewerker("Ben")
print(persoon1.krijg_naam(), persoon1.isMedewerker())
print(medewerker1.krijg_naam(), medewerker1.isMedewerker())