class persoon:
    def __init__(self, voornaam=None, achternaam=None, schooljaar=2019):
        self.voornaam=voornaam
        self.achternaam=achternaam
        self.schooljaar=schooljaar
    def __str__(self):
        return "Mijn naam is {} {}".format(self.voornaam, self.achternaam)
class student(persoon):
    def __str__(self):
        return "Welkom {} {} bij de klas van {}".format(self.voornaam, self.achternaam, self.schooljaar)
    


Persoon1=persoon("Yanis", "Rabah")
Persoon2=student("Yanis", "Rabah")
print(Persoon1)
print(Persoon2)