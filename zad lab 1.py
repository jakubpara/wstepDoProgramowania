"""print(type(1+2))#dodawanie
print(type(1+4.5))#dodawanie ale float nie int
print(type(3/2))#dzielenie float
print(type(4/2)) #dzielenie int
print(type(3//2))#dzielenie calkowite int bo wiadomo calkowita
print(type(-3//2))#int dzielenie z reszta znowu
print(type(11%2))#reszta z dzielenia int
print(type(2**10))#potegowanie int
print(type(8**(1/3)))#potegowanie float"""

"""a=int(3.0)
b=float(3)
c=float("3")
d=str(12.4)
e=bool(0)
print(a)
print(b)
print(c)
print(d)
print(e)"""

"""zad2
uczelnia="Studiuje na WSIiZ"
print(uczelnia)"""

"""zad3
imię = 'Jan'
wiek = 20
wzrost = 178

print("Nazywam się", imię, "i mam",wiek,"lat")
print("Moj wzrost to", wzrost, "cm")"""


"""
cena=39.99
Rabat=0.2
print("Po zastosowaniu rabatu:",round(((1-Rabat)*cena),2))
#round(co ma zaokrąglić, do ilu miejsc)
"""

"""
#zad5
a=input("Podaj długość pierwszego boku:")
b=input("Podaj długość drugiego boku:")
pole= float(a)*float(b)
print(pole)"""

#kalkulator
'''if dzialanie=="+":
   print(a+b)
elif dzialanie=="-":
   print(a-b)
elif dzialanie=="*":
   print(a*b)
elif dzialanie=="/":
   if b!=0:
      print(a/b)
   else:
      print("nie dziel przez 0")
elif dzialanie=="^":
   print(a**b)
else:
   print("nieprawidlowe dzialanie")'''
#zadanie z drogą
'''
#zad6
#s=float(input("droga"))
import random
s=random.randint(1,1000)
print(s,"km")
avburn=float(input("spalanie(l/100km)"))
priceperllitr=float(input("cena paliwa za litr")) #domyslnie 6.5

predictedburn=s*avburn/100
print(f"spalisz łącznie: {predictedburn} litrów")
cost=predictedburn*priceperllitr
print(f"Zapłacisz łącznie: {cost} zł")    '''  

#Sprawdź, czy podane hasło ma wymaganą długość 11 znaków oraz zwiera znak specjalny '!'. Jeżeli tak,
#wydrukuj do konsoli „Hasło jest poprawne”, w przeciwnym razie „Hasło jest nie poprawne”.
Hasło = 'pk47!jy0893'

if len(Hasło)==11
    if"!" in Hasło
        print("Hasło jest poprawne")
    else: 
        print("Hasło nie posiada wymaganego znaku")
else:
    print("Hasło nie posiada wymaganej długości znaków")

