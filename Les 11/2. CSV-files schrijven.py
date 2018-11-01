import datetime
import csv

bestand = 'inloggers.csv'

while True:
    naam = input("Wat is je achternaam? ")
   # print (naam)
    if naam != "" or "Einde":
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
    else:
        break



#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file