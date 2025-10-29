#Napisz skrypt w Pythonie, który sprawdza, czy litera wprowadzona przez użytkownika jest duża
#czy mała

tekst= str(input('wprowadx litere: '))
if len(tekst)==1:
    if tekst.isalpha():
        if tekst.isupper():
            print('duża litera')
        else:
            print('mała litera')
    else:
        print('to nie litera')
else:
    print('tekst zbyt długi')
