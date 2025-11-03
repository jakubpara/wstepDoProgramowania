
with open("notowania_gieldowe.txt","r") as raport:
   print(raport.read())

with open("notowania_gieldowe.txt","a") as raport:
   zmiana=raport.write("\n ALR, 113.")
print(zmiana)