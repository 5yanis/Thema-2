class gegevens:
    def __init__(self, naam):
        self.naam=naam

    def krijgnaam(self):
        return "{} is een kleinkind".format(self.naam)
class kind(gegevens):
    def __init__(self, leeftijd, naam):
        super().__init__(naam)
        self.leeftijd=leeftijd
    def krijg_leeftijd(self):
        return "van {}".format(self.leeftijd)
class  kleinkind(kind):
    def __init__(self, leeftijd,naam, adres):
        super().__init__(leeftijd,naam)
        self.adres=adres
    def krijg_adres(self):
        return "die in {} woont".format(self.adres)



lana=kleinkind(naam="lana", leeftijd=6, adres="Turnhout")
print(lana.krijgnaam(), lana.krijg_leeftijd(), lana.krijg_adres())

















