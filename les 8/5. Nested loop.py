list=[1,2,3,4,5,6,7,8,9,10] +
number2=0
for number1 in list:
    number1=number2
    for number in number2:
        print(number1+"*"+number2+"="+(number1*number2))

        