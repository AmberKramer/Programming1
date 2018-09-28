def convert(tempC):
    tempF=tempC*1.8+32
    return (tempF)

def tabel(temp):
    print("   {:5} {:5}".format("F","C"))
    for t in temp:
        print("{:5} {:5}".format(convert(t),t))

temp=range(-30,41,10)
tabel(temp)
