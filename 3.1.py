prijs_maaltijd = 20 
 
 
def prijs_bepalen():
    if prijs_maaltijd > 15: 
        korting = 0.1 
        return korting
    else: 

        korting = 0
        return korting 
prijs_bepalen()
totale_prijs = prijs_maaltijd - (prijs_maaltijd * korting) 

print(f"Totale prijs: €{totale_prijs}") 

print("Bon: Bedankt voor uw bestelling!") 