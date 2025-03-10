class Boek:
    def __init__(self, titel, auteur):
        self.titel=titel
        self.auteur=auteur


    def toonInformatie(self):
        return "{} is geschreven door {}".format(self.titel, self.auteur.naam)



class Auteur:
    def __init__(self, naam, geboortedatum):
        self.naam=naam
        self.geboortedatum=geboortedatum
    
object2=Auteur("J.K Rowling", "31 juli 1965")
object1=Boek("Harry Potter", object2)
print(object1.toonInformatie())

