import datetime
outfile=open('Hardlopers.txt',"a")
name=input("What is your name?: ")
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, "+name+'\n')
outfile.write(s)
outfile.close

