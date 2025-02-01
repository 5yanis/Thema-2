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

        self.inside.add_widget(Label(text="e-mail")) 

        self.mail = TextInput(multiline = False) 

        self.inside.add_widget(self.mail) 

    # Inside Rij 3 

        self.inside.add_widget(Label(text="Bericht")) 

        self.bericht = TextInput(multiline = True) 

        self.inside.add_widget(self.bericht) 


    # Hoofdraster rij 2. 

        self.inside.submit = Button(text="Indienen", font_size=40) 

         #Knop binden aan functie pressed. 

        self.inside.submit.bind(on_press = self.pressed) 

        self.inside.add_widget(self.submit) 
    # Functie die actie toevoegt voor wanneer er op de knop gedrukt wordt. 

    def pressed(self, instance): 

        # We halen de tekst uit de inputvelden op. 

        naam = self.naam.text 

        bericht = self.bericht.text 

        mail = self.mail.text 

        print("Naam: {}, E-mail: {}, bericht: {}".format(naam, mail, bericht)) 

        # We maken de velden leeg. 

        self.naam.text = "" 

        self.bericht.text = "" 

        self.mail.text = "" 

class MyApp(App): 

    # Venster met label creëren. 

    def build(self): 

        return MyGrid() 
if __name__ == "__main__": 

    MyApp().run()