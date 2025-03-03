#klasse aanmaken
class Punten:
    def __init__(self, punt):
        self.punt=punt
    #de berkening van de behaalde punten
    def bereken(self, test):
        return (self.punt/test.max)*test.gewicht
        

#klasse voor de test zelf dus op welke gewicht, max punten.
class Test:
    def __init__(self, max, gewicht):
        self.max=max
        self.gewicht=gewicht


test=Test(25, 20)
jef=Punten(15)
print(jef.bereken(test))
