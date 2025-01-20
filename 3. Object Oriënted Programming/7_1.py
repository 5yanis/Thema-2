class fiets:
    def __init__(self, nummer, klassiek=False, elektrisch=False, leenbaar=None):
        self.elektrisch=elektrisch
        self.klassiek=klassiek
        self.leenbaar=leenbaar
        self.nummer=nummer
    def fiets_lenen(self):
        if self.leenbaar:
            print("lenen gelukt!!!!")
class fiets22:
    def __init__(self, nummer, klassiek=False, elektrisch=False, leenbaar=None):
        self.elektrisch=elektrisch
        self.klassiek=klassiek
        self.leenbaar=leenbaar
        self.nummer=nummer
    def fiets2_lenen(self):
        if self.leenbaar:
            return "(info: {} )".format(self.nummer,self.leenbaar)
    def __repr__(self):
        return fiets2_lenen
        
        
                  



        




fiets1=fiets(1,"klassiek")
fiets2=fiets22(2,"elektrisch", leenbaar=False)
print(fiets2)


