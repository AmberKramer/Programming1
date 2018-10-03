def seizoen(maand):
    if maand>=13 or maand<=0:
        seizoen="Dat is geen correct seizoens nummer."
    elif maand==12:
        seizoen="Het is winter"
    elif maand>=9:
        seizoen="Het is herfst"
    elif maand>=6:
        seizoen="Het is zomer"
    elif maand>=3:
        seizoen="Het is lente"
    else:
        seizoen="Het is winter"
    return seizoen
maand=int(input("Voer hier het maand nummer in:"))
print(seizoen(maand))
