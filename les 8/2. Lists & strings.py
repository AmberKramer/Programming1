list=(input("Geef lijst met minimaal 10 strings: "))
outfile = open("strings.txt", "w")
outfile.write(list)
outfile.close()
infile=open("strings.txt",'r')
regel=infile.readlines()
for words in regel:
    woord=words.split("\", \"")
    print(woord)
    for letter in woord:
        if len(letter) == 4:
            print(letter)