from typing import Any

x=int(input('podaj liczbe gości: '))
x1=[]
n1=[]
xn=[]

for i in range(1,x+1):
    x1.append(i)

for i in range(1,x+1):
    n=int(input(f'podaj liczbe potraw dla {i}: '))
    print(f'ogólnie sprawa taka gość {i} zamówil {n} dan ')
    for j in range(1,n+1):
        n1=(f'osoba {x1[i-1]} danie {j}: ')  #tu dajemy daną osobe i wrzucamy do xn
        xn.append(n1)
print(xn)

licznik=0
ceny=[]


while licznik < len(xn):#w tej petli dla kazdego elementu xn przypisujemy cene
    element=xn[licznik]
    c=float(input(f' {element} cena: '))
    ceny.append(c)

    licznik+=1
print(ceny)

counter=int(0)
#counternext=int(counter+1)
suma=0

print(f'ilosc cen: {len(ceny)}')


while counter < len(ceny):
    suma=suma+ceny[counter]
    counter+=1


srednia=suma/(len(ceny))
print(srednia)


