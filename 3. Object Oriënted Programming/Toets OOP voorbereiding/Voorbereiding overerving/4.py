class gegevens:
    def __init__(self, naam):
        self.naam=naam
    def krijgnaam(self):
        return self.naam
class kind(gegevens):
    def __init__(self, naam,leeftijd):
        super(). __init__(naam)
        self.leeftijd=leeftijd
    def krijg_leeftijd(self):
        return self.leeftijd
class kleinkind(kind):
    def __init__(self, naam, leeftijd, adres):
        super(). __init__(naam,leeftijd)
        self.adres=adres
    def krijg_adres(self):
        return self.adres


Lana=kleinkind("Lana", 15, "Turnhout")
print(Lana.krijgnaam(), Lana.krijg_leeftijd(), Lana.krijg_adres())