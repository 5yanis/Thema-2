class persoon:
    def __init__(self, voornaam, achternaam):
        self.voornaam=voornaam
        self.achternaam=achternaam
    def __str__(self):
        return "Mijn naam is {} {}".format(self.voornaam, self.achternaam)
class student(persoon):
    def __str__(self):
        return "Welkom {} {}!!!".format(self.voornaam, self.achternaam)

persoon1=persoon("Yanis", "Rabah")
student1=student("Zakaria", "el iraki")
print(persoon1)
print(student1)
