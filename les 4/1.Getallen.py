cijferICOR=6
cijferPROG=8
cijferCSN=8
gemiddelde=(cijferICOR+cijferCSN+cijferPROG)/3
beloning=(cijferICOR+cijferCSN+cijferPROG)*30
overzicht='Mijn cijfers(gemiddeld een '+str(gemiddelde)+')leveren mij €'+str(beloning)+' op.'
life='meh'
print(overzicht)
if int(beloning)>500:
   life='You are rich'
else:
    life='You broke...'
print(life)