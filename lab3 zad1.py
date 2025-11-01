paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo>0:
    czas+=1
    paliwo -= paliwo_zużyte_na_s
    print(f'pozostało {paliwo} litrów paliwa')
print('koniec paliwa')

