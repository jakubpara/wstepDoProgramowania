
#s=float(input("droga"))
import random
s=random.randint(1,1000)
print(s,"km")
avburn=float(input("spalanie(l/100km)"))
priceperllitr=float(input("cena paliwa za litr")) #domyslnie 6.5

predictedburn=s*avburn/100
print(f"spalisz łącznie: {predictedburn} litrów")
cost=predictedburn*priceperllitr
print(f"Zapłacisz łącznie: {cost} zł")