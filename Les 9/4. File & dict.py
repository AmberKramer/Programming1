infile=open('ticker.txt','r')
inhoud=infile.readlines()
infile.close()

dictionary={}

def ticker(filename):
    for gedeelte in inhoud:
        inhoud_split=gedeelte.split(":")
        dictionary[inhoud_split[0]]=inhoud_split[1].strip()
    return dictionary
print(ticker(dictionary))
test=input("Enter Company name: ")
print('Ticker symbol: '+dictionary[test])
TEST2=input("Enter Ticker symbol: ")
for bedrijf in dictionary.keys():
    if TEST2 == dictionary[bedrijf]:
        print('Company name: '+bedrijf)