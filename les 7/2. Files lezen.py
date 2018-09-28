infile=open('kaartnummers.txt',"r")
regels=infile.readlines()
infile.close()
for regel in regels:
    info=regel.split(',')
    print("{} heeft kaart nummer: {}".format (info[1].strip(),info[0]))
