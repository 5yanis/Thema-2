# Kivy library importeren 

import kivy 

# Klassen app en label importeren. Hierdoor kunnen we hier sneller naar verwijzen. 

from kivy.app import App 

from kivy.uix.label import Label 

import kivy 

# De klassen die we willen gebruiken importeren. 

from kivy.app import App 

from kivy.uix.label import Label 

from kivy.uix.gridlayout import GridLayout 

from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 

# We maken een klasse aan voor onze app.  

# Dit is een subklasse van de klasse App van Kivy zelf. 

# Hierdoor kunnen we alle attributen en methodes van App gebruiken,  

# maar hier ook eigen dingen aan toevoegen. 
         
# Kivy library importeren. 
# Klasse MyGrid aanmaken. Dit is een subklasse van GridLayout. 

class MyGrid(GridLayout): 

    # Constructor met variabele aantal attributen (kwargs). 

    def __init__(self, **kwargs): 

        super(MyGrid, self).__init__(**kwargs) 

    # Hoofdraster met 1 kolom. 

        self.cols = 1 

    # 2 kolommen in het hoofdraster.  

    # Dit raster geven we de naam inside. 

        self.inside = GridLayout() 

        self.inside.cols = 2 

 

    # Inside Rij 1 

        self.inside.add_widget(Label(text="Naam: ")) 

        self.naam = TextInput(multiline = False) 

        self.inside.add_widget(self.naam) 

    # Inside Rij 2 

        self.inside.add_widget(Label(text="Achternaam")) 

        self.achternaam = TextInput(multiline = False) 

        self.inside.add_widget(self.achternaam) 

    # Inside Rij 3 

        self.inside.add_widget(Label(text="E-mail")) 

        self.mail = TextInput(multiline = False) 

        self.inside.add_widget(self.mail) 

    # De 3 rijen van inside als eerste rij in het hoofdraster invoegen. 

        self.add_widget(self.inside) 

        # Hoofdraster rij 2. 

        self.submit = Button(text="Indienen", font_size=40) 

        self.add_widget(self.submit) 

class MyApp(App): 

    # Venster met label creëren. 

    def build(self): 

        return MyGrid() 
if __name__ == "__main__": 

    MyApp().run()