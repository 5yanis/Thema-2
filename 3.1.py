#het gegeven
prijs_maaltijd =  20

#bepalen van de korting

def prijs_korting():

    if prijs_maaltijd > 15: 

        korting = 0.1
    else: 

        korting = 0

    return korting
prijs_korting()

#De totale prijs bepalen

def totale(korting):
    totale_prijs=prijs_maaltijd-(prijs_maaltijd*korting)
    print(f"Totale prijs: €{totale_prijs}") 
    print("Bon: Bedankt voor uw bestelling!") 



totale(prijs_korting())