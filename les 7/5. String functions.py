def gemiddelde(zin):
    outfile = open('InputZin.txt', "w")
    outfile.write(zin)
    outfile.close()
    infile=open('InputZin.txt', "r")
    regel=infile.readlines()
    letters=0
    for words in regel:
        word= words.split(' ')
        for letter in word:
            letters += len(letter)
        eind=(letters / len(word))
    return eind
zin=input("Schrijf hier je zin:")
print(gemiddelde(zin))