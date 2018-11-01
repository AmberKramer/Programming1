import csv

with open('CSVFileLezen.csv', mode='r') as csv_file:
    scoreboard = csv.reader(csv_file, delimiter=';', quotechar='|')
    winning=0
    winnaar=[]
    for row in scoreboard:
        if int(row[2])>int(winning):
            winning=row[2]
            winnaar=row
    print("De hoogste score is: {} op {} behaald door {}".format(winnaar[2],winnaar[1], winnaar[0]))

