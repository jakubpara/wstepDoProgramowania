ulica=['Jagodowa', 'Lipowa', 'Kwiatowa', 'Kasztanowa', 'Polna']
blok= [1, 2, 3, 4, 5,]
mieszkanie=list(range(1,11))

for i in ulica:
    for j in blok:
        for k in mieszkanie:
            print(i,j,'/',k)