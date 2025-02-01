class figuur:
    def __init__(self, breedte, lengte):
        self.breedte = breedte
        self.lengte = lengte

    def omtrek(self):
        omtrek = 2 * (self.breedte + self.lengte)
        return omtrek

    def oppervlakte(self):
        oppervlakte = self.lengte * self.breedte
        return oppervlakte

    def __repr__(self):
        return "afmetingen: {},{}".format(self.breedte, self.lengte)

    def __str__(self):
        omtrek = self.omtrek()  # Roep de omtrek methode aan
        oppervlakte = self.oppervlakte()  # Roep de oppervlakte methode aan
        return "Omtrek: {} Oppervlakte: {}".format(omtrek, oppervlakte)

# Maak een instantie van de klasse
rechthoek = figuur(5, 2)

# Print de representatie en de string weergave
print(repr(rechthoek))  # Dit gebruikt __repr__
print(rechthoek)         # Dit gebruikt __str__
