numbersecret = 71
numberout = 100
tentativa_max = 5
numberfalse = 0

while numberfalse < tentativa_max:
    addnumberuser = int(input('Coloque o número aqui -->: '))
    numberfalse += 1  # incrementa a tentativa

    if addnumberuser > numberout or addnumberuser < 1:
        print('Número fora do permitido, por favor, coloque um número de 1 a 100')
    elif addnumberuser > numbersecret:
        print('Número maior que o número secreto, tente de novo')
    elif addnumberuser < numbersecret:
        print('Número menor que o número secreto, tente de novo')
    else:
        print(' VOCÊ ACERTOU!!!')
        break
else:
    print('Acabaram suas tentativas! O número secreto era', numbersecret)
print('')
