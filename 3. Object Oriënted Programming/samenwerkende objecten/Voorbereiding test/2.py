#het aanmaken van de klasse en de constuctor
class Punten:
    def __init__(self, punt):
        self.punt=punt
    

    def Berekenpunt(self, test):
        return self.punt/test.max*test.gewicht



class Test:
    def __init__(self, max, gewicht):
        self.max=max
        self.gewicht=gewicht
    

object1=Punten(15)
object2=Test(25, 20)
print(object1.Berekenpunt(object2))