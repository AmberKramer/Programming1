invoerstring=input("Test: ")
def code(invoerstring):
    test =""
    for letter in invoerstring :
        test+=chr(ord(letter) + 3)
    print(test)
code(invoerstring)