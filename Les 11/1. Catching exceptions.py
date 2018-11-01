Aantal_Personen=int(input("Met hoeveel personen gaat u reizen?:"))
try:

    if Aantal_Personen <0:
        print('Delen door negatieve getallen is niet mogelijk')
    else:
        Prijs = 4356 / Aantal_Personen
        print(Prijs)
except ValueError:
    print('Geeft het aantal in cijfers!')
except ZeroDivisionError:
    print('Delen door nul is niet mogelijk')
