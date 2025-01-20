class klassen:
    def __init__(self, naam=None, leerlingnummer=None, klas=None, status=None):
        self.naam=naam
        self.leerlingnummer=leerlingnummer
        self.klas=klas
        self.status=status
    def inschrijving(self):
        if self.status=="ingeschreven":
            print("leerling is ingeschreven")
        else:
            print("leerling uitgeschreven")
            status=""
            print(status)



leerling1=klassen(klas="1C",status="ingeschreven")
leerling2=klassen(status="uitgeschreven")
leerling2.inschrijving()