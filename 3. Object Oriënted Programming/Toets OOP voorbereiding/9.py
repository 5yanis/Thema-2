class auto:
    def __init__(self,kleur, prijs):
        self.kleur=kleur
        self.prijs=prijs
    def prijs_vergelijker(self, waarde):
        prijsverschil=waarde-self.prijs
        return "prijsverschil: {}".format(prijsverschil)
    

auto1=auto("rood", 12000)
print(auto1.prijs_vergelijker(20000))
