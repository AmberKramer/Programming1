def standaardtarief(afstandKM):
    if afstandKM>=50:
        Rprijs=15+(0.6*afstandKM)
    else:
        Rprijs=0.8*afstandKM
    if Rprijs<=0:
        Rprijs=0
    return Rprijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardtarief(afstandKM)
    if weekendrit=="ja" or weekendrit=="Ja":
        if leeftijd<12 or leeftijd>=65:
           print(0.65*standaardtarief(afstandKM))
        else:
            print(0.6*standaardtarief(afstandKM))
    else:
        if leeftijd<12 or leeftijd>=65:
            print(0.7*standaardtarief(afstandKM))
        else:
            print(standaardtarief(afstandKM))
    return

leeftijd = float(input("Wat is uw leeftijd?: "))
weekendrit = input("Reist u in het weekend?: ")
afstandKM = float(input("Hoeveel kilometer heeft u afgelegd?: "))
ritprijs(leeftijd,weekendrit,afstandKM)
