#work in progress
print("1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug")
keuze=int(input("Vul hier uw keuze in:"))
infile=open('kluizen.txt', 'r')
def ToonKluizenVrij():
    kluizen=infile.readlines()
    kluizenbezet=0
    kluizenvrij=12
    for i in kluizen:
        kluizenbezet=kluizenbezet+1
        kluizenvrij=12-kluizenbezet
    return int(kluizenvrij)

def NieuweKluis():
    kluizenBezet=infile.readlines()
    KluisNummers=[1,2,3,4,5,6,7,8,9,10,11,12]
    if ToonKluizenVrij() <1:
        for b in kluizenBezet:
            info = b.split(";")
            if int(info[0]) in KluisNummers:
                KluisNummers.remove(int(info[0]))
        NieuweKluis = min(KluisNummers)
        wachtwoord = input("Vul hier het wachtwoord voor de kluis in: ")
        if len(wachtwoord) >= 4:
            outfile = open('kluizen.txt', 'a')
            outfile.write(str(NieuweKluis) + ";" + wachtwoord + '\n')
            print("Uw kluisnummer is", NieuweKluis)
        else:
            print("Vul alstublieft een geldig wachtwoord in")
    else:
        print("Er geen geen lege kluizen meer beschikbaar.")

    return

def OpenKluis():
    KluisNummer=input("Wat is uw kluisnummer?: ")
    wachtwoord=input("Voer uw wachtwoord in: ")
    kluizen = infile.readlines()
    for b in kluizen:
        info = b.split(";")
    if KluisNummer in info[0] and wachtwoord in info[1]:
        print("Kluis "+str(KluisNummer)+" is nu geopend.")
    else:
        print("Verkeerd wachtwoord")
    return




if keuze==1:
    print("Er zijn nog",ToonKluizenVrij(),"kluizen vrij.")
elif keuze==2:
    NieuweKluis()
elif keuze==3:
    OpenKluis()
elif keuze==4:
    print(4)
else:
    print("Voer alstublieft een correct nummer in.")

