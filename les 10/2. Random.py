import random
count=0
def monopolyworp(count):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    som = die1+die2
    print (die1,"+",die2,"=",som)
    if die1==die2:
        count += 1
        if count==3:
            print("Ga naar de gevangenis")
        else:
            monopolyworp(count)

monopolyworp(count)
