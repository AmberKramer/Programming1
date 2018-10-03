invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen=invoer.split("-")
volgorde=getallen.sort()
getallen1 = [int(i) for i in getallen]
som= sum(getallen1)

print('Gesorteerde list van ints: '+str(getallen1)+'\nGrootste getal: '+str(max(getallen1))+' en Kleinste getal: '+str(min(getallen1)))
print('Aantal getallen: '+str(len(getallen1))+' en Som van de getallen: '+str(som))
print('Gemiddelde: '+str(som / len(getallen1)))