infile=open('kaartnummers.txt',"r")
regels=infile.readlines()
infile.close()
count=0
hoogst=0
for regel in regels:
    info = regel.split(',')
    count=count+1
    if int(info[0])>int(hoogst):
       hoogst=info[0]
print("Deze file telt "+format(count)+" regels.")
print("Het grootste kaartnummer is {} en staat in lijn {}.".format((int(hoogst)),(int(max(regel[0]))+1)))

