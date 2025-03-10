#aanmaken van de klasse en de constructor
class Product:
    def __init__(self, naam , categorie):
        self.naam=naam
        self.categorie=categorie
    
    def behoortTotCategorie(self, Categorie):
        return self.categorie==Categorie.naam



class Categorie:
    def __init__(self, naam):
        self.naam=naam



object1=Product("Banaan", "fruit")
object2=Categorie("groenten")
print(object1.behoortTotCategorie(object2))