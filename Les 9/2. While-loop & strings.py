woord=""
lengte=0
while True:
    lengte=0
    woord=input("Geef een string van 4 letters:")
    for i in woord:
        lengte+=1
    if lengte==4:
        print("Inlezen van correcte string:",woord,"is geslaagd")
        break
    else:
        print(woord,"heeft",lengte,"letters")

