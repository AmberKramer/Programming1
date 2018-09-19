age=int(input("What is your age?: "))
paspoort=input("Do you own a valid Dutch **?: ")
if age >= 18 and paspoort== "yes":
    print("You are allowed to vote")
else:
    print("You ar not allowed to vote, sorry")