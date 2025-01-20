class Fiets:
    def __init__(self, nummer, klassiek=False, elektrisch=False, leenbaar=None):
        self.elektrisch = elektrisch
        self.klassiek = klassiek
        self.leenbaar = leenbaar
        self.nummer = nummer

    def __str__(self):
        return "Fietsnummer: {}, Klassiek: {}, Elektrisch: {}, Leenbaar: {}".format(self.nummer, self.klassiek, self.elektrisch, self.leenbaar)

# Voorbeeld:
fiets1 = Fiets(1, klassiek=True)
fiets2 = Fiets(2, elektrisch=True, leenbaar=False)

print(fiets1)  # Dit zou de __str__ methode aanroepen
print(fiets2)  # Dit zou de __str__ methode aanroepen
