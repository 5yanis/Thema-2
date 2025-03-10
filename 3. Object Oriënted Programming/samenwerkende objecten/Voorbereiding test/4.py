class Meter:
    def __init__(self, waarde):
        self.waarde=waarde


    def __str__(self):
        return "Het object is {}m lang".format(self.waarde)

    
    def naar_centimeter(self):
        return Centimeter(self.waarde*100)





class Centimeter:
    def __init__(self, waarde):
        self.waarde=waarde
    

    def __str__(self):
        return "Het object is {}cm lang".format(self.waarde)


    def naar_meter(self):
        return Meter(self.waarde/100)


object1=Centimeter(14)
object2=Meter(2.5)

