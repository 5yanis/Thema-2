class leerling:
    def __init__(self, naam, leerlingnummer, klas=None, status=None):
        self.naam=naam
        self.leerlingnummer=leerlingnummer
        self.klas=klas
        self.status=status
    

leerling1=leerling("Jan Janssens", 7)
leerling2=leerling("Marie Mariën", 10, "1A")
leerling3=leerling("Bert Balders", klas="1B")
