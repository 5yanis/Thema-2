class persoon:
    def __init__(self, voornaam, achternaam):
        self.voornaam=voornaam
        self.achternaam=achternaam
    def __str__(self):
        return "Mijn naam is {} {}".format(self.voornaam, self.achternaam)
class student(persoon):
    def __init__(self, voornaam, achternaam, studiejaar):
        super(). __init__(voornaam, achternaam)
        self.studiejaar=studiejaar
            
    def welkom(self):
        return "in de klas van {}".format(self.studiejaar)

    def __str__(self):
        return "Welkom {}, {}".format(self.voornaam, self.achternaam)

student1= student("Mike", "Olsen", 2019)
print(student1, student1.welkom())
