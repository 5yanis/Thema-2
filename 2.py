class fiets:
    def __init__(self, nummer, klassiek=False, elektrisch=False, leenbaar=False):
        self.elektrisch=elektrisch
        self.klassiek=klassiek
        self.leenbaar=leenbaar
    def fiets_lenen(self):
        if self.leenbaar:
            print("lenen gelukt!!!!")
        




fiets1=fiets(1,"klassiek")
fiets2=fiets(2,"elektrisch", leenbaar=True)
fiets2.fiets_lenen()


print(type(fiets1))