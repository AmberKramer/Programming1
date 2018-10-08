dictionary={}
def namen():
    if naam in dictionary:
        dictionary[naam]+=1
    else:
        dictionary[naam]=1
    return dictionary



while True:
    naam = input("Voer hier een naam in: ")
    if naam=="":
        for naam in dictionary:
            print(naam, dictionary[naam])
        break
    else:
        namen()