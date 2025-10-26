"""print(type(1+2))#dodawanie
print(type(1+4.5))#dodawanie ale float nie int
print(type(3/2))#dzielenie float
print(type(4/2)) #dzielenie int
print(type(3//2))#dzielenie calkowite int bo wiadomo calkowita
print(type(-3//2))#int dzielenie z reszta znowu
print(type(11%2))#reszta z dzielenia int
print(type(2**10))#potegowanie int
print(type(8**(1/3)))#potegowanie float"""

'''a=int(3.0) #tylko 3 bez rozwiniecia
b=float(3)  # 3 z miejscami po przecinku
c=float("3") #dalej liczba 3 na której mozna wykonywac dzialania
d=str(12.4) #tekst
e=bool(0) #fałsz(tryb warunkowy)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''


"""zad2
uczelnia="Studiuje na WSIiZ"
print(uczelnia)"""

#zad3
'''
imię = 'Jan'
wiek = 20
wzrost = 178

print("Nazywam się", imię, "i mam",wiek,"lat")
print("Moj wzrost to", wzrost, "cm")'''


#zad4

'''cena=39.99
Rabat=0.2
cena_po_rabacie=cena-(Rabat*cena)
print(f"cena po rabacie: {cena_po_rabacie:.2f}")'''

#zad5
"""
a=input("Podaj długość pierwszego boku:")
b=input("Podaj długość drugiego boku:")
pole= float(a)*float(b)
print(pole)"""


#zad6
'''
#s=float(input("droga"))
import random
s=random.randint(1,1000)
print(s,"km")
avburn=float(input("spalanie(l/100km)"))
priceperllitr=float(input("cena paliwa za litr")) #domyslnie 6.5

predictedburn=s*avburn/100
print(f"spalisz łącznie: {predictedburn} litrów")
cost=predictedburn*priceperllitr
print(f"Zapłacisz łącznie: {cost} zł")'''



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
