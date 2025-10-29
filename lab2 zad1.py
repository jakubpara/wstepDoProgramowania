wynik=float(input("Podaj liczbę punktów: "))

if wynik<50:
    print('egzamin nie zaliczony, trzeba powtórzyć ' )
elif wynik >= 50 and wynik <= 80:
    print('egzamin zaliczony, ale można poprawić')
elif wynik > 80 and wynik <= 100:
    print('egzamin zaliczony w pierwszym terminie')
