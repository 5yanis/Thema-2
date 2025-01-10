class fiets:
    def __init__(self, nummer, klassiek=False, elektrisch=False):
        self.elektrisch=elektrisch
        self.klassiek=klassiek




fiets1=fiets(1,"klassiek")
fiets2=fiets(2,"elektrisch")


print(type(fiets1))