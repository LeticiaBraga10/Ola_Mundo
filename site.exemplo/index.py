somaidade=0
mi=0
nomevelho=0
maioridadehomem=0
totmulher20=0
for k in range(1,3):
    print('='*7, 'PESSOA {}'.format(k),'='*7)
    nome = str(input('NOME:')).strip().capitalize()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [F/M]:'))
    somaidade += idade
    if k == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    else:
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
        elif sexo in 'Ff' and idade<20:
            totmulher20 += 1
print('O número de mulheres com menos de 20 anos é: {}'.format(totmulher20))
print('O homem mais velho é {}, com {} anos'.format(nomevelho,maioridadehomem))
mi+=somaidade/2
print('A média das idades é: {}'.format(mi))