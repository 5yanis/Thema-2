class Gegevens:
    def __init__(self, naam, voornaam, ancienniteit, functie):
        self.naam=naam
        self.voornaam=voornaam
        self.anncienniteit=ancienniteit
        self.functie=functie


    def __str__(self):
        return "{} werkt al {} in ons bedrijf".format(self.naam, self.anncienniteit)

    def berekenOpslag(self):
        return self.anncienniteit*self.functie.Berekenopslagjaar()





class Functie:
    def __init__(self, omschrijving, loon, opslag):
        self.omschrijving=omschrijving
        self.loon=loon
        self.opslag=opslag



    def Berekenopslagjaar(self):
        return self.loon*(self.opslag/100)


Marie=Functie("manager", 2000, 5)
gegeven=Gegevens("Marie Meas", "Marie", 5, Marie)

print(gegeven)
print(Marie.Berekenopslagjaar())
print(gegeven.berekenOpslag())
