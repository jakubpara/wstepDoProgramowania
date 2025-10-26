#zadanie 4
'''gol=int(input("gole strzelone"))
bonus=float(gol*10)

a=gol//5
b=gol//10
if gol>4:
   bonus+=5*a
if gol>9:
   bonus+=10*b

print(bonus)'''

#zadanie 5

'''with open("notowania_gieldowe.txt","r") as raport:
   print(raport.read())

with open("notowania_gieldowe.txt","a") as raport:
   proba=raport.write("\n ALR, 113.")'''

#zadanie 6



#zadanie 7
'''#Sprawdź, czy podane hasło ma wymaganą długość 11 znaków oraz zwiera znak specjalny '!'. Jeżeli tak,
#wydrukuj do konsoli „Hasło jest poprawne”, w przeciwnym razie „Hasło jest nie poprawne”.
Hasło = 'pk47!jy0893'

if len(Hasło)==11:
   if "!" in Hasło:
        print("Hasło jest poprawne")
   else: 
        print("Hasło nie jest poprawne")
else:
   print("Hasło nie jest poprawne")'''

#zadanie 8
'''text = 'Studiuje-Informatykę'
print(text[0:3])
print(text[-2:])'''

#zadanie 9
text="LEKKI wiatr"
a=text.swapcase()
print(a)
