class persoon:
    def __init__(self, voornaam=None, achternaam=None):
        self.voornaam=voornaam
        self.achternaam=achternaam
    def __str__(self):
        return "Mijn naam is {},{}".format(self.voornaam, self.achternaam)
class student(persoon):
    def __str__(self):
        return "Welkom {},{}".format(self.voornaam, self.achternaam)
    