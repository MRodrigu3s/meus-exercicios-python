

numbersecret = 71
numberfalse = 0
numberout = 100
print ('                                             JOGO ADIVINHAÇÃO')
print ('')
print ('')
print ('                                    Tente adivinhar um número de 1 a 100')
print ('')
print ('')
while numberfalse != numbersecret or numberout:
    addnumberuser = int(input('Coloque o número aqui -->: '))
    if addnumberuser > numberout:
        print ('Número fora do permitido, por favor, coloque um número de 1 a 100')
    elif addnumberuser > numbersecret:
        print('Numero maior que o número secreto, tente de novo')
    elif addnumberuser < numbersecret:
        print ('Numero menor que o número secreto, tente de novo')
    else:
        print ('                                             VOCÊ ACERTOU!!!')
        break
print ('')
