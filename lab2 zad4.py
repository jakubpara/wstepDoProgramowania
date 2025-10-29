gol=int(input("gole strzelone"))
bonus=float(gol*10)

a=gol//5
b=gol//10
if gol>4:
   bonus+=5*a
if gol>9:
   bonus+=10*b

print(bonus)
