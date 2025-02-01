class leerling:
    def __init__(self, naam, leerlingnummer=None, klas=None, status=None):
        self.naam=naam
        self.leerlingnummer=leerlingnummer
        self.klas=klas
        self.status=status

    def inschrijvingen(self,aanpassing):
        self.aanpassing=aanpassing
        self.klas=aanpassing
        return "klas: {}".format(self.klas)
    def uitschrijven(self):
        if self.status=="uitgeschreven":
            self.klas=""
            return "klas: {}".format(self.klas)
        

leerling1=leerling("Jan Janssens", leerlingnummer=7)
leerling2=leerling("Marie Mariën", 10, "1A", status="uitgeschreven")
leerling3=leerling("Bert Balders", klas="1B")
print(leerling1.inschrijvingen("1C"))
print(leerling2.uitschrijven())
