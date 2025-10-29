a=float(input("Podaj pierwszą liczbe: "))
b=float(input("Podaj drugą liczbe: "))
dzialanie=input("Podaj dzialanie")
if dzialanie=="+":
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
   print("nieprawidlowe dzialanie")