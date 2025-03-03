class persoon:
    def __init__(self, naam):
        self.naam=naam
    def krijgnaam(self):
        return self.naam
    def medewerker(self):
        return "False"
        
class medewerker(persoon):
    def medewerker(self):
        return "True"
    
persoon1=persoon("Jan")
medewerker1=medewerker("Yanis")
print(persoon1.krijgnaam(), persoon1.medewerker())
print(medewerker1.krijgnaam(), medewerker1.medewerker())        
