#het aanmaken van de klasse en constructor
class Boete:
    def __init__(self, niveau, prijs):
        self.niveau=niveau
        self.prijs=prijs
    def __str__(self):
        return "Je hebt een boete van niveau {}, je moet {} euro betalen.".format(self.niveau, self.prijs)
#het aanmaken van de 2de klasse en de object als resultaat teruggeven
class Overtreding:
    def __init__(self, Maxsnelheid, Geredensnelheid):
        self.Maxsnelheid=Maxsnelheid
        self.Geredensnelheid=Geredensnelheid


    def Bepaalboete(self):
        overtreding=self.Geredensnelheid-self.Maxsnelheid
        if overtreding<0:
            return Boete(0,0)
        elif overtreding<10:
            return Boete(1,50)
        elif overtreding<20:
            return Boete(2,100)
        elif overtreding>=20:
            return Boete(3, 150)
        
object1=Overtreding(50,100)
print(object1.Bepaalboete())