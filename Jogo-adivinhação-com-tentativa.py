

numbersecret = 71
numberfalse = 0
numberout = 100
tentativa_max = 5

print ('                                             JOGO ADIVINHAÇÃO')
print ('')
print ('')
print ('                                    Tente adivinhar um número de 1 a 100')
print ('')
print ('')
while numberfalse < tentativa_max:
    addnumberuser = int(input('Coloque o número aqui -->: '))
    numberfalse += 1
    if addnumberuser > numberout or addnumberuser < 1:
        print ('Número fora do permitido, por favor, coloque um número de 1 a 100. Você perdeu 1 das 5 Chances ')
    elif addnumberuser > numbersecret:
        print(f'Numero maior que o número secreto, tente de novo, você usou {numberfalse} das 5 Chances')
    elif addnumberuser < numbersecret:
        print (f'Numero menor que o número secreto, tente de novo, você usou {numberfalse} das 5 Chances')
    else:
        print ('                                             VOCÊ ACERTOU!!!')
        break
    print(f'Chances restantes {tentativa_max - numberfalse}')
else:
    print(f'Acabaram suas chances, o numero era {numbersecret}')
print ('')
