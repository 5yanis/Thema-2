#aanmaken van de klasse boete
class Boete:
    def __init__(self, niveau, prijs):
        self.niveau=niveau
        self.prijs=prijs
    #het printen van de resultaten.
    def __str__(self):
        return "Je hebt een boete van niveau {}. Je moet {} betalen!".format(self.niveau, self.prijs)
    #het bepalen van hoe erg de overtreding is dus de niveau en boete bepalen
class overtreding:
    #constructor
    def __init__(self, maxSnelheid, geredenSnelheid):
        self.maxSnelheid=maxSnelheid
        self.geredenSnelheid=geredenSnelheid
    def bepaalBoete(self):
        overtreding=self.geredenSnelheid-self.maxSnelheid
        if overtreding<10:
            return Boete(1, 50)
        elif overtreding<20:
            return Boete(2, 100)
        elif overtreding>=20:
            return Boete(3,150)
        else:
            return Boete(0,0)
#de gegeven objecten voor de resultaat te testen.
Jan=overtreding(100,55)
jan_boete=Jan.bepaalBoete()
print(jan_boete)